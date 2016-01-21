from graphics import *
from time import *
import csv


def drawL(x1,y1,x2,y2,win):
    l = Line(Point(x1,y1), Point(x2,y2))
    l.setWidth(10)
    l.draw(win)
    return l   

def drawRect(x,y,win):
    r = Rectangle(Point(x,y), Point(x,y))
    r.setWidth(10)
    r.setOutline("Blue")
    r.draw(win)
    
   
    
def drawStop(x,y,side, stop_id, win):
    offset = 12
    x= int(x)
    y = int(y)
    if(side == "X+"):
        drawRect(x+offset, y, win)
        t = Text(Point(x+(3*offset),y), str(stop_id))
        t.draw(win)
    elif(side == "X-"):
        drawRect(x-offset, y, win)
        t = Text(Point(x-(3*offset),y), str(stop_id))
        t.draw(win)
    elif(side == "Y+"):
        drawRect(x, y+offset, win)
        t = Text(Point(x,y+(3*offset)), str(stop_id))
        t.draw(win)
    elif(side == "Y-"):
        drawRect(x, y-offset, win)
        t = Text(Point(x,y-(3*offset)), str(stop_id))
        t.draw(win)
    
    
def main():
    win = GraphWin('Bus Simulator', 800, 800) # give title and dimensions
    win.height = 800;
    win.width = 800;
    #win.yUp() # make right side up coordinates!
    drawL(30, 10, 30, 70, win)
    drawL(25, 70, 350, 70, win)
    drawL(350, 65, 350, 300, win)
    drawL(345, 300, 410, 300, win)
    drawL(410, 295, 410, 630, win)
    drawL(415, 630, 60, 630, win)
    drawL(60, 635, 60, 465, win)
    drawL(55, 465, 170, 465, win)
    drawL(170, 470, 170, 300, win)
    drawL(165, 300, 355, 300, win)
    
    stopMap = {}
      
    with open("D:/Bus_Data/StopVisual.csv", 'r') as csvfile:
        spamreader1 = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row1 in spamreader1:
            stop_id = row1[0]
            stop_name = row1[2]
            stop_X = row1[4]
            stop_Y = row1[5]
            stop_DIR = row1[6]
            stop_side = row1[7]
            drawStop(stop_X, stop_Y, stop_side, stop_id, win)
            stopMap[stop_id] = [stop_name, stop_X, stop_Y, stop_DIR, stop_side]
            #print(stop_DIR)
            #print(stop_side)
    
    head = Circle(Point(30,10), 10) # set center and radius
    head.setFill("Red")
    head.draw(win)
    
    label_X = 560
    X_offset = 100
    time_label = Text(Point(label_X,30), "TIME: ")
    time_text = Text(Point(label_X + X_offset,30), "1/12/2015  7:40:56 AM")
    
    trip_ID_label = Text(Point(label_X,60), "Trip ID: ")
    trip_ID_text = Text(Point(label_X + X_offset,60), "A_1")
    
    prevStop_label = Text(Point(label_X-20,90), "Previous Stop: ")
    prevStop_text = Text(Point(label_X + X_offset-20,90), "")
    
    nextStop_label = Text(Point(label_X-20,120), "Next Stop: ")
    nextStop_text = Text(Point(label_X + X_offset -20,120), "")
    
    onTime_label = Text(Point(label_X-20,150), "Not-Late Count: ")
    onTime_text = Text(Point(label_X + X_offset -20,150), "")
    
    LateTime_label = Text(Point(label_X-20,180), "Late Count: ")
    LateTime_text = Text(Point(label_X + X_offset -20,180), "")
    
    efficiency_label = Text(Point(label_X-20,210), "Efficiency/Hit Rate: ")
    efficiency_text = Text(Point(label_X + X_offset -20,210), "")
    
    time_label.draw(win)
    time_text.draw(win)
    trip_ID_label.draw(win)
    trip_ID_text.draw(win)
    prevStop_label.draw(win)
    prevStop_text.draw(win)
    nextStop_label.draw(win)
    nextStop_text.draw(win)
    onTime_label.draw(win)
    onTime_text.draw(win)
    
    LateTime_label.draw(win)
    LateTime_text.draw(win)
    
    efficiency_label.draw(win)
    efficiency_text.draw(win)
    
    late_count = 0
    notLate_count = 0
    efficiency = 0
    
    with open("D:/Bus_Data/BusVisualData_A.csv", 'r') as csvfile:
        spamreader1 = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row1 in spamreader1:
            fromStop_ID = row1[0]
            toStop_ID = row1[6]
            
            to_X = int(stopMap[toStop_ID][1])
            to_Y = int(stopMap[toStop_ID][2])
            from_Dir = int(stopMap[fromStop_ID][3])
            
            from_name = stopMap[fromStop_ID][0]
            to_name = stopMap[toStop_ID][0]
            
            prevStop_text.setText(from_name)
            nextStop_text.setText(to_name)
            time_text.setText(row1[4])
            
            status = row1[11]
            mode = row1[9]
            if(mode == "1"):
                if(status == "LATE"):
                    late_count = late_count + 1
                else:
                    notLate_count = late_count + 1
                    
                efficiency = notLate_count /(late_count+notLate_count)
                
                LateTime_text.setText(str(late_count))
                onTime_text.setText(str(notLate_count))
                efficiency_text.setText(str(round(efficiency,2)))
        
            while((head.getCenter().getX() != to_X ) and (head.getCenter().getX() != to_Y)):
                dx = to_X - head.getCenter().getX()
                dy = to_Y - head.getCenter().getY()
                print(dx)
                print(dy)
                if(from_Dir == 1 or dy == 0):    
                    while(dx != 0):
                        head.move(dx/abs(dx),0)
                        dx = to_X - head.getCenter().getX()
                        sleep(0.05)
                if(from_Dir == 2 or dx == 0):    
                    while(dy != 0):
                        head.move(0,dy/abs(dy))
                        dy = to_Y - head.getCenter().getY()
                        sleep(0.05)
                

    head.draw(win)
    for i in range(60):
       head.move(0, 1)
       sleep(0.05)
    for i in range(230):
       head.move(1, 0)
       sleep(0.05)           

    
    win.getMouse()
    win.close()

main()