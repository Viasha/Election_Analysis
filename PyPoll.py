#The data we need to retrieve
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each canidate won
#The winner of the election based on popular vote


#Import the datetime classs from the datetime module
import datetime as dt
#use the nonw() attribute on the datetime class to get the present time.
now= dt.datetime.now()
#Print the present time.
print("The time right now is", now)

import csv
import os
#Assign a variabl for the file to load and the path
file_to_load=os.path.join("OneDrive/Documents/Data Analytics/Resources/election_results.csv")

file_to_save=os.path.join("OneDrive/Documents/Data Analytics/analysis.xlsx")
#Open the electoin results and read the file

total_vote=0
candidate_options=[]
candidate_votes={}
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)
    headers= next(file_reader)
    print(headers)
    for row in file_reader:
        total_vote +=1
        candidate_name= row[2]     
    if candidate_name not in candidate_options:
        candidate_options.append(candidate_name)
        candidate_votes[candidate_name]=0
    candidate_votes[candidate_name]+=1
    print(candidate_votes)

for candidate_name in candidate_votes:
    votes= candidate_votes[candidate_name]
    vote_percentage= float(votes) / float(total_vote)*100
    
winning_candidate= ""
winning_count= 0
winning_percentage =0
if (votes> winning_count) and (vote_percentage > winning_percentage):
    winning_count= votes
    winning_percentage = vote_percentage
    winning_candidate= candidate_name
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary= (
    f"------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1}%\n"
    f"------------------\n")
print(winning_candidate_summary)






