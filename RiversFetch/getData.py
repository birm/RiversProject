# script to get new data

import WaterServices

# list of site numbers from /somewhere/
# this list for now
# - run data each

sites = ["02336300"]
print(WaterServices)
res = [WaterServices.getData(x) for x in sites]
print(res)
