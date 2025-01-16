import os
import time
import datetime as dt


#It's a function incase you want to import it instead of running it directly
def timer(timeRemaining):
    #Some basic dependencies
    import os
    import time
    import datetime as dt

    #Makes or imports the module to clear the console
    while True:
        try:
            from clear import clear
            print("\rClear module successfully detected!")
            clear()
            break
        except:
            print("\rHang tight, creating clear module")
            with open("clear.py", "w") as amogus:
                amogus.write(r'''import os
    import platform

    sys = platform.system()

    def clear():
        if sys == "Windows":
            os.system("cls")
        elif sys == "Linux":
            os.system("clear")
        else:
            print("The clear function is not supported for %s" % sys)''')
    
    timeStarted = str(dt.datetime.now()).split(" ")
    
    dateStarted = timeStarted[0].split("-")
    
    dateStarted[0] = int(dateStarted[0])
    dateStarted[1] = int(dateStarted[1])
    dateStarted[2] = int(dateStarted[2])
    
    timeStarted.remove(timeStarted[0])
    
    timeStarted = timeStarted[0].split(":")

    timeStarted[0] = int(timeStarted[0])
    timeStarted[1] = int(timeStarted[1])
    timeStarted[2] = float(timeStarted[2])
    
    willFinishAt = timeRemaining.copy()

    timeRemaining[0] = int(timeRemaining[0])
    timeRemaining[1] = int(timeRemaining[1])
    timeRemaining[2] = float(timeRemaining[2])

    willFinishAt[0] = int(willFinishAt[0])
    willFinishAt[1] = int(willFinishAt[1])
    willFinishAt[2] = float(willFinishAt[2])

    #These are for the date which will be calculated below
    willFinishAt.append(dateStarted[1])
    willFinishAt.append(dateStarted[2])
    willFinishAt.append(dateStarted[0])

    #These are all for calculating if any of the time values should roll over to the next one, ie. 60 seconds = 1 minute
    if willFinishAt[2] + timeStarted[2] >= 60:
        willFinishAt[1] += 1
        willFinishAt[2] = willFinishAt[2] + timeStarted[2] - 60
        while willFinishAt[2] >= 60:
            willFinishAt[1] += 1
            willFinishAt[2] -= 60
    else:
        willFinishAt[2] = willFinishAt[2] + timeStarted[2]
    
    
    if willFinishAt[1] + timeStarted[1] >= 60:
        willFinishAt[0] += 1
        willFinishAt[1] = willFinishAt[1] + timeStarted[1] - 60
        while willFinishAt[1] >= 60:
            willFinishAt[0] += 1
            willFinishAt[1] -= 60
    else:
        willFinishAt[1] = willFinishAt[1] + timeStarted[1]

    
    if willFinishAt[0] + timeStarted[0] >= 25:
        willFinishAt[4] += 1
        willFinishAt[0] = willFinishAt[0] + timeStarted[0] - 24
        while willFinishAt[0] >= 25:
            willFinishAt[4] += 1
            willFinishAt[0] -= 24
    else:
        willFinishAt[0] = willFinishAt[0] + timeStarted[0]

    #For calculating day, month, and year rollovers *visibly shudders*
    runAgain = True
    runAgain2 = True
    runAgain3 = True
    calcMonth = dateStarted[1]

    while runAgain == True or runAgain2 == True or runAgain3 == True:
        if willFinishAt[4] >= 32 and calcMonth in [1, 3, 5, 7, 8, 10, 12]:
            willFinishAt[3] += 1
            willFinishAt[4] -= 31
            runAgain = True
            calcMonth += 1
        else:
            runAgain = False
        
        
        if willFinishAt[4] >= 31 and calcMonth in [4, 6, 9, 11]:
            willFinishAt[3] += 1
            willFinishAt[4] -= 30
            runAgain2 = True
            calcMonth += 1
        else:
            runAgain2 = False
        

        if calcMonth == 2:
            
            if list(dateStarted)[len(list(dateStarted)) - 1] == 0 and list(dateStarted)[len(list(dateStarted)) - 2] == 0 and list(dateStarted)[len(list(dateStarted)) - 3] == 0:
                thousandYear = True
            else:
                thousandYear = False

            if (dateStarted[0]/4).is_integer() == True and thousandYear == False:
                if willFinishAt[4] >= 30:
                    willFinishAt[3] += 1
                    willFinishAt[4] -= 29
                    runAgain3 = True
                    calcMonth += 1
                else:
                    runAgain3 = False
            
            else:
                if willFinishAt[4] >= 29:
                    willFinishAt[3] += 1
                    willFinishAt[4] -= 28
                    runAgain3 = True
                    calcMonth += 1
                else:
                    runAgain3 = False
        
        else:
            runAgain3 = False
    
        if willFinishAt[3] >= 13:
            willFinishAt[3] = willFinishAt[3] - 12
            willFinishAt[5] += 1
            calcMonth = 1
            runAgain, runAgain2, runAgain3 = True, True, True

    
    #These are to convert the month from a number to a word
    if dateStarted[1] == 1:
        dateStarted[1] = "January"
    elif dateStarted[1] == 2:
        dateStarted[1] = "February"
    elif dateStarted[1] == 3:
        dateStarted[1] = "March"
    elif dateStarted[1] == 4:
        dateStarted[1] = "April"
    if dateStarted[1] == 5:
        dateStarted[1] = "May"
    elif dateStarted[1] == 6:
        dateStarted[1] = "June"
    elif dateStarted[1] == 7:
        dateStarted[1] = "July"
    elif dateStarted[1] == 8:
        dateStarted[1] = "August"
    if dateStarted[1] == 9:
        dateStarted[1] = "September"
    elif dateStarted[1] == 10:
        dateStarted[1] = "October"
    elif dateStarted[1] == 11:
        dateStarted[1] = "November"
    elif dateStarted[1] == 12:
        dateStarted[1] = "December"


    #These are to convert the month from a number to a word (again)
    if willFinishAt[3] == 1:
        willFinishAt[3] = "January"
    elif willFinishAt[3] == 2:
        willFinishAt[3] = "February"
    elif willFinishAt[3] == 3:
        willFinishAt[3] = "March"
    elif willFinishAt[3] == 4:
        willFinishAt[3] = "April"
    if willFinishAt[3] == 5:
        willFinishAt[3] = "May"
    elif willFinishAt[3] == 6:
        willFinishAt[3] = "June"
    elif willFinishAt[3] == 7:
        willFinishAt[3] = "July"
    elif willFinishAt[3] == 8:
        willFinishAt[3] = "August"
    if willFinishAt[3] == 9:
        willFinishAt[3] = "September"
    elif willFinishAt[3] == 10:
        willFinishAt[3] = "October"
    elif willFinishAt[3] == 11:
        willFinishAt[3] = "November"
    elif willFinishAt[3] == 12:
        willFinishAt[3] = "December"


    if dateStarted[2] == 1:
        dateStarted[2] = "1st"
    elif dateStarted[2] == 2:
        dateStarted[2] = "2nd"
    elif dateStarted[2] ==3:
        dateStarted[2] = "3rd"
    else:
        dateStarted[2] = str(dateStarted[2]) + "th"

    if willFinishAt[4] == 1:
        willFinishAt[4] = "1st"
    elif willFinishAt[4] == 2:
        willFinishAt[4] = "2nd"
    elif willFinishAt[4] ==3:
        willFinishAt[4] = "3rd"
    else:
        willFinishAt[4] = str(willFinishAt[4]) + "th"
    
    def rightNow():
        currentTime = str(dt.datetime.now()).split(" ")
        currentDate = currentTime[0].split("-")
        
        currentDate[0] = int(currentDate[0])
        currentDate[1] = int(currentDate[1])
        currentDate[2] = int(currentDate[2])
        
        #These are to convert the month from a number to a word (please be the last time)
        if currentDate[1] == 1:
            currentDate[1] = "January"
        elif currentDate[1] == 2:
            currentDate[1] = "February"
        elif currentDate[1] == 3:
            currentDate[1] = "March"
        elif currentDate[1] == 4:
            currentDate[1] = "April"
        if currentDate[1] == 5:
            currentDate[1] = "May"
        elif currentDate[1] == 6:
            currentDate[1] = "June"
        elif currentDate[1] == 7:
            currentDate[1] = "July"
        elif currentDate[1] == 8:
            currentDate[1] = "August"
        if currentDate[1] == 9:
            currentDate[1] = "September"
        elif currentDate[1] == 10:
            currentDate[1] = "October"
        elif currentDate[1] == 11:
            currentDate[1] = "November"
        elif currentDate[1] == 12:
            currentDate[1] = "December"

        if currentDate[2] == 1:
            currentDate[2] = "1st"
        elif currentDate[2] == 2:
            currentDate[2] = "2nd"
        elif currentDate[2] ==3:
            currentDate[2] = "3rd"
        else:
            currentDate[2] = str(currentDate[2]) + "th"

        currentTime.remove(currentTime[0])
        currentTime = currentTime[0].split(":")
        currentTAD = currentDate.copy()
        currentTAD.append(currentTime[0])
        currentTAD.append(currentTime[1])
        currentTAD.append(float(currentTime[2]))
        return currentTAD

    #These two loops make sure that the seconds and minutes are below 60 before the actual timer starts (purely cosmetic)
    while timeRemaining[2] >= 60:
        timeRemaining[2] -= 60
        timeRemaining[1] += 1

    while timeRemaining[1] >= 60:
        timeRemaining[1] -= 60
        timeRemaining[0] += 1

    #This is for avoiding cummulative delay for the time it's running.
    iterationCount = 0

    def findError(EX, A):

        error = min((abs(EX-A))/A, 0.99)
        # print(error)
        return error


    timerStart = time.time()

    while True:
        beggining = time.time()

        clear()

        now = rightNow()

        
        print('''
Timer started at:     %s:%s:%s, %s %s, %s
Timer will finish at: %s:%s:%s, %s %s, %s

Current exact time: %s:%s:%s, %s %s, %s

Generic clock:

%s:%s:%s

Total time remaining:
    
    Years:   %s
    Months:  %s
    Weeks:   %s
    Days:    %s
    Hours:   %s
    Minutes: %s
    Seconds: %s''' % (timeStarted[0], timeStarted[1], timeStarted[2], dateStarted[1], dateStarted[2], dateStarted[0], willFinishAt[0], willFinishAt[1], willFinishAt[2], willFinishAt[3], willFinishAt[4], willFinishAt[5], now[3], now[4], now[5], now[1], now[2], now[0], timeRemaining[0], timeRemaining[1], timeRemaining[2], (((timeRemaining[0] * 60) + timeRemaining[1] + (timeRemaining[2] / 60))/525600), (((timeRemaining[0] * 60) + timeRemaining[1] + (timeRemaining[2] / 60))/43800), (((timeRemaining[0] * 60) + timeRemaining[1] + (timeRemaining[2] / 60))/10080.000008284931513658847819446), (((timeRemaining[0] * 60) + timeRemaining[1] + (timeRemaining[2] / 60))/1440), (((timeRemaining[0] * 60) + timeRemaining[1] + (timeRemaining[2] / 60))/60), ((timeRemaining[0] * 60) + timeRemaining[1] + (timeRemaining[2] / 60)), (((timeRemaining[0] * 60) + timeRemaining[1] + (timeRemaining[2] / 60))*60)))
        
        if timeRemaining[0] == 0 and timeRemaining[1] == 0 and timeRemaining[2] < 1:
            time.sleep(timeRemaining[2])
            timeRemaining[2] = -1
        
        else:
            timeRemaining[2] -= max(min(1 - (time.time() - (timerStart + iterationCount)), 1), 0.0001)
            # print((time.time() - beggining))

            
            nowSeconds = time.time()

            error = findError((nowSeconds), (timerStart + iterationCount))

            if nowSeconds > timerStart + iterationCount:
                offBy = 0
                time.sleep(max(1 - (10000000000 * error) - offBy, 0.001))
                offBy = ((time.time() - beggining) % 1)
                # print(time.time() - beggining)
            else:
                offBy = 0
                time.sleep(min(1 + (10000000000 * error) - offBy, 1.005))
                offBy = ((time.time() - beggining) % 1)
                # print(time.time() - beggining)
    


            iterationCount += 1


            if timeRemaining[1] < 0 and timeRemaining[0] > 0 or timeRemaining[2] < 0 and timeRemaining[1] == 0 and timeRemaining[0] > 0:
                timeRemaining[1] += 60
                timeRemaining[0] -= 1

            if timeRemaining[2] < 0 and timeRemaining[1] > 0:
                timeRemaining[2] += 60
                timeRemaining[1] -= 1


        
        if timeRemaining[0] == 0 and timeRemaining[1] == 0 and timeRemaining[2] <= -1:
            print("\nTimer finished")
            break

if __name__ == "__main__":
    time = input("Please input the length of your timer in hours:minutes:seconds\n\n> ")
    while True:
        try:
            time = time.split(":")
            if len(time) == 3 and int(time[0]) >= 0 and int(time[1]) >= 0 and float(time[2]) >= 0:
                break
            else:
                raise Exception("Invalid input")
        except:
            time = input("Please input the length of your timer in hours:minutes:seconds\n\n> ")
    timer(time)