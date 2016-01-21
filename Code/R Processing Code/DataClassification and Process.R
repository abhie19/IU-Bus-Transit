
library(dplyr)
library(lubridate)

data1 <- read.csv("D:/Bus_Data/Out_X.csv")
weatherD <- read.csv("D:/Bus_Data/DailyWeather.csv")
weatherD$EDT <- NULL

TotalSet<- stopSubset[0,]

for (stopC in unique(data1$StopCombo))
{
  #stopC <- "8_10"
  stopSubset <- subset(data1, data1$StopCombo == stopC)
  
  dc <- kmeans(stopSubset$TimeDiffer, 5)

  stopSubset<-cbind(stopSubset,clusterTD=dc$cluster)
  
  d <- aggregate(stopSubset$TimeDiffer, by= list(stopSubset$clusterTD), FUN = mean)
  
  #ds <- count(stopSubset, clusterno1)
  #ds
  
  d1 <- d[order(d$x, decreasing = TRUE),]
  d1
  stopSubset$Status[stopSubset$clusterTD == d1[1,1]] <- "VERY_EARLY"
  stopSubset$Status[stopSubset$clusterTD == d1[2,1]] <- "EARLY"
  stopSubset$Status[stopSubset$clusterTD == d1[3,1]] <- "ON_TIME"
  stopSubset$Status[stopSubset$clusterTD == d1[4,1]] <- "LATE"
  stopSubset$Status[stopSubset$clusterTD == d1[5,1]] <- "VERY_LATE"
  
  stopSubset$M_Status[stopSubset$clusterTD == d1[1,1]] <- "NOT_LATE"
  stopSubset$M_Status[stopSubset$clusterTD == d1[2,1]] <- "NOT_LATE"
  stopSubset$M_Status[stopSubset$clusterTD == d1[3,1]] <- "NOT_LATE"
  stopSubset$M_Status[stopSubset$clusterTD == d1[4,1]] <- "LATE"
  stopSubset$M_Status[stopSubset$clusterTD == d1[5,1]] <- "LATE"
  
  TotalSet <- rbind(TotalSet, stopSubset)  

}

d_timeStamp <- as.POSIXct(TotalSet$TimeStamp, format="%m/%d/%Y %H:%M:%S")
TotalSet$DOW <- weekdays(d_timeStamp)
TotalSet$HOD <- hour(d_timeStamp)

TotalSet$date <- as.Date(as.POSIXct(d_timeStamp, origin="1970-01-01"))
weatherD$Date1 <- as.Date(as.POSIXct(weatherD$Date, origin="1970-01-01"))

data2 <- merge(TotalSet, weatherD, by.x = "date", by.y = "Date1")
colnames(data2)

write.csv(data2[,-23], "D:/Bus_Data/OUT_X_Final.csv", row.names = FALSE)
