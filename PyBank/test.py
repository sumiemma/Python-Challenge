import csv


csvpath = "Resources/budget_data.csv"


# lists to separate the two columns
date = []
pl = []


with open(csvpath,"r") as csvhandler:
    csvreader = csv.reader(csvhandler,delimiter=",")
    csvreaders = next(csvreader)
   
    for row in csvreader:
        date.append(row[0])
        pl.append(row[1])
   
    print(str(len(date)))