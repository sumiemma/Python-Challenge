import csv

csvpath = "Resources/election_data.csv"

#creating lists for columns
voter_id = []
county = []

#setting vote count for each candidate to zero
ccs = 0
dd = 0
rad = 0

#read csv
with open(csvpath,"r") as csvhandler:
    csvreader = csv.reader(csvhandler,delimiter=",")
    csvreaders = next(csvreader)

    for row in csvreader:
        #counting total number of votes in the data set
        voter_id.append(row[0])
        county.append(row[1])

        #counting votes for each candidate
        if row[2] == "Charles Casper Stockham":
            ccs += 1        
        elif row [2] == "Diana DeGette":
            dd += 1
        else:
            rad += 1

    #calculating percentage of votes for each candidate
    ccs_percentage = round(ccs / len(voter_id) * 100, 3)
    dd_percentage = round(dd / len(voter_id) * 100, 3)
    rad_percentage = round(rad / len(voter_id) * 100, 3)


    #printing out results according to format
    print("Election Results")

    
    #printing out results according to format
    print("-------------------------")
    
    #printing out the total number of votes
    print ("Total Votes: " + str(len(voter_id)))

    #printing out results according to format
    print("-------------------------")

    #print out the name, percentage and number of votes for each candidate
    print("Charles Casper Stockham: " + str(ccs_percentage) + "%  (" + str(ccs) + ")")
    print("Diana DeGette: " + str(dd_percentage) + "%  (" + str(dd) + ")")
    print("Raymon Anthony Doane: " + str(rad_percentage) + "%  (" + str(rad) + ")")

    #printing out results according to format
    print("-------------------------")

    #printing out the winner's name
    if ccs > dd and ccs>rad:
        print("Winner: Charles Casper Stockham")
    elif dd > ccs and dd > rad:
        print("Winner: Diana Degette")
    else:
        print("Winner: Raymon Anthony Doane")

    #printing out results according to format
    print("-------------------------")