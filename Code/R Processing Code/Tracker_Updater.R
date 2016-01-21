
dataTracker <- read.csv("D:/Bus_Data/Tracker_X.csv")
stopData <- read.csv("D:/Bus_Data/RouteToStopMap.csv")

stopData <- subset.data.frame(stopData,stopData$Route == "X")

dT <- merge(dataTracker, stopData[, c("Stop_ID", "StopIndex", "Name")], by.x = "ToStop_Name", by.y = "Name")

dT$StopCombo <- paste(dT$FromStop_ID, dT$Stop_ID, sep="_") 
dT$Mode[dT$FromStop_ID == dT$Stop_ID] <- 0
dT$Mode[dT$FromStop_ID != dT$Stop_ID] <- 1

setdiff(unique(stopData$Name), unique(dT$ToStop_Name))
 

library(stringr)
library(dplyr)

write.table(file=paste("D:/Bus_Data/Out_X.csv"), x=t(colnames(out)), row.names = FALSE, col.names = FALSE, quote = FALSE, sep= ",", append = TRUE)

for (i in unique(dT$StopCombo)) 
{

  d<-subset(dT,dT$StopCombo==i)
  rcount <- nrow(d)
  if(rcount > 100)
  {
    fit<- kmeans(d$Time,4)
    
    out<-cbind(d,clusterno=fit$cluster)
    
    d <- aggregate(out$Time, by= list(out$clusterno), FUN = mean)
    ds <- aggregate(out$Time, by= list(out$clusterno), FUN = sum)
    d1 <- count(out, clusterno)
    d2 <- cbind(d1, d, ds)
    
    d2 <- d2[order(d2$n, decreasing = TRUE),]
    meanValue <- d2[1,4]
    f1 <- d2[1,2]
    f2 <- d2[2,2]
    diff <- f1*0.25
    if((f1-f2)< diff)
    {
      meanValue <- (meanValue + d2[2,4])/2
    }
    
    out$MeanTime <- meanValue
    out$TimeDiffer <- (meanValue - out$Time)
     
    
    write.csv(file=paste("D:/Bus_Data/E/Out_X_",".csv",sep=i), x=out, row.names = FALSE)
    write.csv(file=paste("D:/Bus_Data/E/Out_X_","_Summary.csv",sep=i), x=d2, row.names = FALSE)
    
    write.table(file=paste("D:/Bus_Data/Out_X.csv"), x=out, row.names = FALSE, col.names = FALSE, quote = FALSE, sep= ",", append = TRUE)
  }
  
}


