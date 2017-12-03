#import methods
import os
import csv
import operator
import statistics
import collections
#create absolute path
e1_csv = os.path.join("Resources", "election_data_1.csv")
e2_csv = os.path.join("Resources", "election_data_2.csv")
#Pybank_txt = os.path.join("Resources","Pybank.txt")
#Use the script in the specified csv_files
for csv_file in (e1_csv, e2_csv):
    #define a list that  will collect the result of the loop through the Voters ID column and adds to voters =[]
    voters =[]
    #county =[ not needed for this exercise], define a list that  will collect the result of the loop through the county column and adds to county =[]
    #county =[]
    #define a list that  will collect the result of the loop through the Candidate column and adds to candidate =[]
    candidate =[]
    #open and read csv file
    with open(csv_file, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #print (csv_file)
        #skip first title row
        next(csvreader, None)
        #create loops that goes along the columns of the VoterID, County and candidate and appends those values to voters =[], county =[] and candidate =[], respectively
        for row in csvreader:
            voters.append(row[0])
            #county.append((row[1]))
            candidate.append(row[2])
        #we can calculate the total votes by obtaining the len of the voters list   
        #total_votes=(len(voters))
    #print(total_votes)
    #to obtain the elements and the times they appear we must use import collections and the formular below (dont know why-ASK!). 
    # Also now we make a dictionary candidate_name_votes {keys(candidates):values(number of votes)} 
    candidate_name_votes = collections.Counter(candidate)
    #to obtain the names of the candidates
    #candidate_name = candidate_name_votes.keys()
    #to obtain the number of votes
    candidate_votes = candidate_name_votes.values()
    #we can also obtain the total number of votes by the sum of the values of the dictionary
    total_votes = (sum(candidate_votes))
    #we need to determine the values of the dictonary candidate_name_votes using items
    for key, value in candidate_name_votes.items():
        votes_num = (value)
        #print (votes_num)
    #we can also obtain the total number of votes by the sum of the values of the dictionary
    #total_votes = (sum(candidate_votes))
    #print(int(total_votes))
    #to convert the values of the dictionay to percentagem we must loop between each value, divide by the total_votes and multiply by 100.
    #this dictonary is now in percentagem, so I gave it a new name of per_candidates_votes
    for value in candidate_name_votes:
        candidate_name_votes[value] = (candidate_name_votes[value] / total_votes)*100
    #need dictionary with the percentages of the votes and corresponding key(candidates)
    per_candidates_votes = (candidate_name_votes)
    #value_max = (max(per_candidates_votes.values()))
    maximum = max(per_candidates_votes, key=per_candidates_votes.get)  # Just use 'min' instead of 'max' for minimum.
    #print(maximum, per_candidates_votes[maximum])
    #get the key of maximum votes
    winner = maximum
    #winner_vote_perc = per_candidates_votes[winner]
    output = ("")
    output += ("Election Results" + "\n"
    "----------------------------" + "\n" 
    "Total Votes: " + str (total_votes) + "\n"
    "----------------------------" + "\n")
    print("Election Results" + "\n"
    "----------------------------" + "\n" 
    "Total Votes: " + str (total_votes) + "\n"
    "----------------------------" + "\n")
    #print (winner)
    #print (winner_vote_perc)
    #print (value_max)
    #to print the key and values of the dictionary per_candidate_votes use the .items() and the for loop through the data
    for cand, per in per_candidates_votes.items():
        kand = (cand)
        perc = (per)
        #print (kand)
        #print (perc)
        sum_results =  (" " + (kand) + ": " + str(perc) + "%" + " (" + str (votes_num) + ")" )
        output += (sum_results + "\n")
        print (sum_results)

    print("----------------------------" + "\n" 
    "Winner: " + str(winner) + "\n"
   "----------------------------" + "\n")
    output += ("----------------------------" + "\n" 
    "Winner: " + str(winner) + "\n"
   "----------------------------" + "\n")
    if total_votes == 803000:
        f = open("HW3Pypooltest1.txt","w") #opens file with name of "test.txt"
        f.write(output)
        f.close()
    else:
        f = open("HW3Pypooltest2.txt","w") #opens file with name of "test.txt"
        f.write(output)
        f.close()
    #output the Data requested
    #text =  ("Election Results" + "\n"
    #"----------------------------" + "\n" 
    #"Total Votes: " + str (total_votes) + "\n"
    #"----------------------------" + "\n")
    #print (text) 
        #print(sum_results)------ ask why i cant get the loop if i dont indent
        #" " + (kand) + ": " + str(perc) + "%" + " (" + str (votes_num) + ")"
    #text2 = ("----------------------------" + "\n" 
    #"Winner: " + str(winner) + "\n"
   # "----------------------------" + "\n")
    #print (text2)