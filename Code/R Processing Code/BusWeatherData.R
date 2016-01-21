library(weatherData)

getStationCode("Bloomington", region="IN")

wData <- getSummarizedWeather("KBMG", "2014-05-05", "2015-06-06",
                     station_type = "airportCode", opt_temperature_columns = TRUE,
                     opt_all_columns = FALSE, opt_custom_columns = TRUE,
                     custom_columns = c(1,16,20,21,22), opt_verbose = FALSE)

write.csv(file="D:/Bus_Data/DailyWeather.csv", x=wData, row.names = FALSE)

checkDataAvailabilityForDateRange("KBMG", "2015-01-01", "2015-06-06")

dt <- colnames(wDataDetail)
dt

wDataDetail <- getWeatherForDate("KBMG", "2014-05-05", "2015-06-06",
                  station_type = "airportCode", opt_detailed = TRUE,
                  opt_write_to_file = FALSE, opt_temperature_columns = TRUE,
                  opt_all_columns = FALSE, opt_custom_columns = TRUE,
                  custom_columns = c(4,6,10,11,12), opt_verbose = FALSE, daily_min = FALSE,
                  daily_max = FALSE)

write.csv(file="D:/Bus_Data/DailyDetailedWeather.csv", x=wDataDetail, row.names = FALSE)
 