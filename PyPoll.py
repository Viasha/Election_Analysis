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
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)
    headers= next(file_reader)
    print(headers)






