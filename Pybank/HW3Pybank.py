#import methods
import os
import csv
import operator
import statistics
#create absolute path
b1_csv = os.path.join("Resources", "budget_data_1.csv")
b2_csv = os.path.join("Resources", "budget_data_2.csv")
#Use the script in the specified csv_files
for csv_file in (b1_csv, b2_csv):
    #define a list that  will collect the result of the loop through the Date column and adds to mon =[]
    mon =[]
    #efine a list that  will collect the result of the loop through the Revenue column and adds to rev =[]
    rev =[]
#open and read csv file
    with open(csv_file, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #print (csv_file)
        #skip first title row
        next(csvreader, None)
        #create loops that goes along the rows of the Date and Revenue and appends those values to mon =[] and rev =[], respectively
        for row in csvreader:
            mon.append(row[0])
            rev.append(int(row[1]))
    #print(len(mon))
    #print (rev)
            #calculate the number of months by calculating the length of the Date column, now in mon = [], using len()
            total_mon = len(mon)
            #calculate the total revenue by summing all elements of Revenue column now in rew = []
            total_rev = sum(rev)
        #print (total_mon)   
        #print (total_rev)
    # revdiff create a  loop that goes along the rev list and substracts the rev value of month(i+1) - rev value of month (i) 
        revdiff = [rev[i+1]-rev[i] for i in range(len(rev)-1)] #stops before the last value
    #print (revdiff)
    #calculate the average of the revenue difference
    avrrevdiff = (sum(revdiff))/(len(revdiff))
    #print (avrrevdiff)
    #the greatest increase in revenue amount over the entire period
    greatinc =  max (revdiff)
    #print (greatinc)
     #the date of the greatest increase in revenue date over the entire period
    #list.index(elem) -- searches for the given element from the start of the list and returns its index.
    greatincindex = revdiff.index(greatinc)
    #print (greatincindex)
    #need to add 1 to include all the month values
    greatincmonindex = greatincindex + 1
    #from the mon list using the index value, obtain the corresponding month
    greatincmon = mon[greatincmonindex]
    #print (greatincmonindex)
    #the greatest decrease in revenue amount over the entire period
    greatdec =  min (revdiff)
    #print (greatdec)
    #list.index(elem) -- searches for the given element from the start of the list and returns its index.
    greatdecindex = revdiff.index(greatdec)
    #need to add 1 to include all the revenue values
    greatdecmonindex = greatdecindex +1
    #print (greatdecmonindex)
    #from the mon list using the index value, obtain the corresponding revenue
    greatdecmon = mon[greatdecmonindex]
    #print (greatdecmon)
    #output the Data requested
    text = ("Financial Analysis" + "\n" 
    "----------------------------" + "\n" 
    "Total Months: " + str (total_mon) + "\n"
    "Total Revenue: " + str (total_rev) + "\n"
    "Average Revenue Change: " +  str(avrrevdiff) + "\n" +
    "Greatest Increase in Revenue: " + str(greatincmon) + " (" + str (greatinc)+ ")" +"\n"
    "Greatest Decrease in Revenue: " + str (greatdecmon) + " (" + str (greatdec) + ")" +"\n")
    print(text)
    if total_mon == 41:
        f = open("HW3Pybanktest1.txt","w") #opens file with name of "test.txt"
        f.write(text)
        f.close()
    else:
        f = open("HW3Pybanktest2.txt","w") #opens file with name of "test.txt"
        f.write(text)
        f.close()
    #I wanted to use the script below, but with the 'w', it overwrites the results from b1_csv
    # with open('Pybank.txt' , 'w') as f: 
        #f.write(str (text)) #only the data from b2_csv shows up