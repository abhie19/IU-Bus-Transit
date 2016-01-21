import csv
from datetime import datetime


def annotateData(tripFile, busTrackerFile):
    with open('TRACKER_W_TRIP_ID_new.csv', 'a') as csvfile2:
        spamwriter = csv.writer(csvfile2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    #     spamwriter.writerow("a,b,c")
       
        with open(tripFile, 'r') as csvfile1:
            spamreader1 = csv.reader(csvfile1, delimiter=',', quotechar='"')
            #row1 = spamreader1.next()
            for row1 in spamreader1:
                trip_id = row1[0]
                bus_id = row1[2]
                route_id = row1[3]
                #date_object = datetime.strptime('Jun 1 2005  1:33PM', "%-m/%-d/%Y %-I:%M:%S %p")
                #1/12/2015  7:19:58 AM
                time_s = datetime.strptime(row1[4], "%m/%d/%Y %H:%M:%S %p")
                time_e = "" 
                with open(tripFile, 'r') as csvfile3:
                    spamreader2 = csv.reader(csvfile3, delimiter=',', quotechar='"')
                    for  row2 in spamreader2:
                        bus_id2 = row2[2]
                        route_id2 = row2[3]
                        time2 = datetime.strptime(row2[4], "%m/%d/%Y %H:%M:%S %p")
                        if(bus_id == bus_id2 and route_id == route_id2 and time_s < time2):
                            time_e = time2
                            break   
                if(time_e != ""):  
                    with open(busTrackerFile, 'r') as csvfile:
                        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                        for row in spamreader:
                            if(bus_id == row[5] and time_s <= datetime.strptime(row[7], "%m/%d/%Y %H:%M:%S %p") < time_e):
                                row.append(trip_id)
                                spamwriter.writerow(row)
                else:
                    print("NO FINISHTIME FOR", trip_id)
                #csvfile2.flush()
                print("Finished", trip_id, " TIme:", datetime.utcnow())
    return

#annotateData("TRIP_A.csv", "BusTracker_A.csv")
#annotateData("TRIP_B.csv", "BusTracker_B.csv")      
#annotateData("TRIP_E.csv", "BusTracker_E.csv")      
annotateData("TRIP_X.csv", "BusTracker_X.csv")             
