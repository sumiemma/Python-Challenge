import csv

csvpath = "Resources/budget_data.csv"

# lists to separate the two columns
date = []
pl = []

#read csv
with open(csvpath,"r") as csvhandler:
    csvreader = csv.reader(csvhandler,delimiter=",")
    csvreaders = next(csvreader)

    total_profit_loss = 0

    for row in csvreader:
        
        #counting total number of months included in the data set
        date.append(row[0])
        pl.append(row[1])
        
        #finding net total amount of p/l over the entire period
        total_profit_loss += int(row[1])


    #finding the mean change
    total_monthly_change =  int(pl[-1]) - int(pl[0])
    number_of_data = len(pl) - 1
    average_change = round((total_monthly_change) / (number_of_data),2)        

    #printing out the total months
    print ("Total Months: " + str(len(date)))

    #printing out the total profit/loss
    print ("Total: $" + str(total_profit_loss))

    #printing out the mean change
    print ("Average Change: $" + str(average_change))


    #Putting monthly changes to a list
    monthly_change = []
    for i in range(1,len(pl)):
        monthly_change.append(int(pl[i]) - int(pl[i-1]))
        max_increase = max(monthly_change)
        min_increase = min(monthly_change)

    #looking for the max of monthly changes  
    for i in range(0,len(monthly_change)):
        if monthly_change[i] == max_increase:
            print("Greatest Increase in Profits: " + str(date[i+1]) + " ($" + str(monthly_change[i]) + ")")
        if monthly_change[i] == min_increase:
            print("Greatest Decrease in Profits: " + str(date[i+1]) + " ($" + str(monthly_change[i]) + ")")


