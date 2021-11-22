# WEATHER DATA VALIDATION
### DATA
Weather data gives us temperature information for each country in region level.
### DATA VALIDATION STEPS
Performing the validation process for the input source data provided.
- Reading the data and aligning with the defined datatypes.

| Column names | timedesc | state | avgtemp | maxtemp | mintemp | prcp |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | 
| **Data type** | date | string | float | float | float | float |
- Standardizing the headers.
- Convert all categorical columns into lower case.
- Removing any special characters in the numerical columns in the data.
- Encoding and decoding string values and retaining only english characters / words.
- Checking the date column and fomatting as YYYY-MM-DD
- Removing the rows of data which exceeds the current date.
- Removing leading and trailing spaces if any for all the categorical columns.

### WORKFLOW

- Once the data have been arrived into the centralised data storage, the validation script gets triggered in **azure databricks** automatically from the **azure data factory** pipeline.
      - Data ingestion-  ../country/weather_data/weather_data.csv
- The parameters which are passed from the ADF are : input file path, output file path, log path, country name, source name
- Processing all the validation functions by leveraging the capabilities of unified configuration file of weather data.
- Once the execution gets successfully completed the validated data will be saved in the output path as current and history folder.
- All the necessary logs from each validation function will be saved in the log file which is maintained at date level as error log, debug log, info log, critical log, warning log.
- Upon failure of the validation script due to error or data mismatch or any other common issues then an email will be triggered with a notification and that particular error log file with the message will be attached to the concerned team.

### INPUT CREDENTIALS
- **country** - Name of the country for which the validation should happen
- **data source** - weather_data
- **source data storage container name** - analyticsdata
- **input file path** - <analytics data mountpoint>/mmm_de/output/<country_name>/
weather_data/weather_data.csv
- **output data storage container name** - gacmartechanalyticsstor
- **current output file path** - <gacmartechanalyticsstor mountpoint>/mmm_de/output/
<country_name>/weather_data/current/<hash>_<country>_weather_data.csv.gzip
- **history output file path** - <gacmartechanalyticsstor mountpoint>/mmm_de/output/
<country_name>/weather_data/history/<hash>_<country>_weather_data.csv.gzip
- **critical log path** - <gacmartechanalyticsstor mountpoint>/mmm_de/logs/all_logs/
weather_data/<country>/critical_log/weather_data_<country>_<date>__app.critical.log
- **debug log path** - <gacmartechanalyticsstor mountpoint>/mmm_de/logs/all_logs/
weather_data/<country>/debug_log/weather_data_<country>_<date>__app.debug.log
- **error log path** - <gacmartechanalyticsstor mountpoint>/mmm_de/logs/all_logs/
weather_data/<country>/error_log/weather_data_<country>_<date>__app.error.log
- **info log path** - <gacmartechanalyticsstor mountpoint>/mmm_de/logs/all_logs/
weather_data/<country>/info_log/weather_data_<country>_<date>__app.info.log
- **warning log path** - <gacmartechanalyticsstor mountpoint>/mmm_de/logs/all_logs/
weather_data/<country>/warning_log/weather_data_<country>_<date>__app.warning.log
- **config path** - <gacmartechanalyticsstor mountpoint>/config/weather_data_config.json
