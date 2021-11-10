# Rivers Fetch
Input Data From the USGS water API to mariadb

## Env Variables
All of these variables will trigger if python thinks their value is truthy. I'd recommend just not setting if you want false, and setting to some nonspecial string if you want true.

- CREATE_DATABASE - Set to create rivers database if not exists
- CREATE_TABLES - Set to create site and observation tables if not exists
- INSERT_SITES - Set to get site data from the api and try inserting it. Runs per site.
- INSERT_OBSERVATIONS - Set to get observation data from the api and try inserting it. Runs per observation per site. Probably not prepared to handle duplicates well.
- PRINT_DATA - Set to print a summary of ALL records in the observation and site tables.

## My Gripes
This isn't _good_, this was made quickly. Ideally, I'd have more things like URIS and credentials as env variables, and a better system for table creation and whatnot. But as this is NOT THE FOCUS OF THE PROJECT, so I went with quick and dirty over good practices.

Maybe revisit this later?
