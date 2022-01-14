import requests
import datetime
import RDBHandler

# Handlers for the water services "api" to python

# description of the format: https://waterdata.usgs.gov/nwis/?tab_delimited_format_info

# api bases
dataUrlBase = "https://waterdata.usgs.gov/ga/nwis/uv"
siteUrlBase = "https://waterservices.usgs.gov/nwis/site"
# params are encoded. Use a dict for storage and translation
paramCodes = {
    "00010": "Temperature",
    "00045": "Precipitation",
    "00060": "Discharge",
    "00065": "GageHeight",
    "00095": "Conductance",
    "00300": "DO",
    "00400": "pH",
    "63680": "Turbidity"
    }

def getData(siteNo, period=1):
    # * siteNo - site number from usgs
    # * period - number of days back to go from today
    url = dataUrlBase + "?format=rdb&site_no=" + str(siteNo) + "&period=" + str(period)
    print(url)
    # let an exception here halt this
    data = requests.get(url).text
    return RDBHandler.readDict(data, paramCodes)

def getSite(siteNo):
    # * siteNo - site number from usgs
    url = siteUrlBase + "?format=rdb&sites=" + str(siteNo) + "&siteOutput=expanded&siteStatus=all"
    data = requests.get(url).text
    return RDBHandler.readDict(data)

# publish our apis and useful struct
WaterServices = {}
WaterServices['paramCodes'] = paramCodes
WaterServices['getSite'] = getSite
WaterServices['getData'] = getData
__all__ = ["paramCodes", "getSite", "getData"]
