# script to test data calls only w/o interfacing with db

import WaterServices

# list of site numbers from /somewhere/
# this list for now
# - run data each

sites = ["02336300"]
print([WaterServices.getData(x) for x in sites])
print([WaterServices.getSite(x) for x in sites])
