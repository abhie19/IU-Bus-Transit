import csv
  
with open('TRIP_A.csv', 'w') as csvfileA:
     spamwriterA = csv.writer(csvfileA, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
     with open('TRIP_B.csv', 'w') as csvfileB:
         spamwriterB = csv.writer(csvfileB, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
          
         with open('TRIP_E.csv', 'w') as csvfileE:
            spamwriterE = csv.writer(csvfileE, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
              
            with open('TRIP_X.csv', 'w') as csvfileX:
                spamwriterX = csv.writer(csvfileX, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
                with open("Trip_ID_1.csv", 'r') as csvfile:
                                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                                header = spamreader.next()
                                for row in spamreader:
                                    if(row[3] == "A"):
                                        spamwriterA.writerow(row)
                                    elif(row[3] == "B" ):
                                        spamwriterB.writerow(row)
                                    elif(row[3] == "E" ):
                                        spamwriterE.writerow(row)
                                    elif(row[3] == "X" ):
                                        spamwriterX.writerow(row)