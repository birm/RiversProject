# script to get new data

import WaterServices
import mariadb
import os

# list of site numbers from /somewhere/
# this list for now
# - run data each

# mapping helper function
def mapData(mapping, data):
    return {v:data.get(k) for (k,v) in mapping.items()}


sites = ["02336300", "02336030", "02336093", "02336106"]
print(WaterServices)
res = [WaterServices.getData(x) for x in sites]
# print(res)
print([WaterServices.getSite(x) for x in sites])

# connect to db

# clear db if asked
if (os.environ.get('CLEAR_DATABASE_FIRST')):
    print("Trying to clear database...")
    try:
        conn = mariadb.connect(
            user="root",
            password="toor",
            host="rivers-db",
            port=3306
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    cur = conn.cursor()
    # create db and tables (TODO -- better way to do db patching than editing python code)
    try:
        cur.execute("DROP DATABASE rivers")
    except mariadb.Error as e:
        print(f"Error: {e}")
    cur.close()
    conn.close()

# create db if not exists
if (os.environ.get('CREATE_DATABASE')):
    print("Trying to create database...")
    try:
        conn = mariadb.connect(
            user="root",
            password="toor",
            host="rivers-db",
            port=3306
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    cur = conn.cursor()
    # create db and tables (TODO -- better way to do db patching than editing python code)
    try:
        cur.execute("CREATE DATABASE IF NOT EXISTS rivers COMMENT 'version 1'")
    except mariadb.Error as e:
        print(f"Error: {e}")
    cur.close()
    conn.close()

# create tables if not exist
if (os.environ.get('CREATE_TABLES')):
    print("Trying to create tables...")
    try:
        conn = mariadb.connect(
            user="root",
            password="toor",
            host="rivers-db",
            port=3306,
            database="rivers"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    cur = conn.cursor()
    # create db and tables (TODO -- better way to do db patching than editing python code)
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS observation (
        id INT NOT NULL AUTO_INCREMENT,
        site VARCHAR(8) NOT NULL,
        datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
        Temperature FLOAT,
        Precipitation FLOAT,
        Discharge FLOAT,
        gage_height FLOAT,
        Conductance FLOAT,
        DO FLOAT,
        pH FLOAT,
        Turbidity FLOAT,
        PRIMARY KEY (id),
        INDEX (site)
        )""")
        cur.execute("""CREATE TABLE IF NOT EXISTS site (
        site VARCHAR(8) NOT NULL,
        name VARCHAR(50),
        latitude FLOAT,
        longitude FLOAT,
        PRIMARY KEY (site)
        )""")
        cur.execute("""CREATE TABLE IF NOT EXISTS prediction (
        id INT NOT NULL AUTO_INCREMENT,
        site VARCHAR(8) NOT NULL,
        datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
        Temperature FLOAT,
        Precipitation FLOAT,
        Discharge FLOAT,
        gage_height FLOAT,
        Conductance FLOAT,
        DO FLOAT,
        pH FLOAT,
        Turbidity FLOAT,
        PRIMARY KEY (id),
        INDEX (site)
        )""")
    except mariadb.Error as e:
        print(f"Error: {e}")
    cur.close()
    conn.close()

if (os.environ.get('INSERT_SITES')):
    print("Trying to insert sites...")
    # fields mapping for sites
    mapping = {"site_no": "site", "station_nm": "name", "dec_lat_va": "latitude", "dec_long_va": "longitude"}
    data = [mapData(mapping, WaterServices.getSite(x)[-1]) for x in sites]
    try:
        conn = mariadb.connect(
            user="root",
            password="toor",
            host="rivers-db",
            port=3306,
            database="rivers",
            autocommit=True
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    cur = conn.cursor()
    for record in data:
        try:
            sql_str = "INSERT INTO site (" + ",".join(record.keys()) + ") VALUES (" + ",".join(["?"]*len(record.keys())) + ")"
            cur.execute(sql_str, tuple(record.values()))
        except mariadb.Error as e:
            print(f"Error: {e}")
    cur.close()
    conn.close()

if (os.environ.get('INSERT_OBSERVATIONS')):
    print("Trying to insert observations...")
    # fields mapping for sites
    mapping = {"site_no": "site", "datetime": "datetime", "Discharge": "Discharge",
               "GageHeight": "gage_height" , "Temperature": "Temperature",
               "Conductance": "Conductance", "DO": "DO", "pH": "pH",
               "Turbidity": "Turbidity", "Precipitation": "Precipitation"}
    # flatten and map
    data = [item for sublist in [[mapData(mapping, y) for y in WaterServices.getData(x)] for x in sites] for item in sublist]
    try:
        conn = mariadb.connect(
            user="root",
            password="toor",
            host="rivers-db",
            port=3306,
            database="rivers",
            autocommit=True
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    cur = conn.cursor()
    for record in data:
        try:
            sql_str = "INSERT INTO observation (" + ",".join(record.keys()) + ") VALUES (" + ", ".join(["?"]*len(record.keys())) + ")"
            cur.execute(sql_str, tuple(record.values()))
        except mariadb.Error as e:
            print(f"Error: {e}")

    cur.close()
    conn.close()
if (os.environ.get('PRINT_DATA')):
    try:
        conn = mariadb.connect(
            user="root",
            password="toor",
            host="rivers-db",
            port=3306,
            database="rivers"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    cur = conn.cursor()
    cur.execute("SELECT site,name FROM site")
    for site, name in cur:
        print(site, name)
    cur.execute("SELECT datetime,site FROM observation")
    for datetime, site in cur:
        print(datetime, site)
    cur.close()
    conn.close()
