import csv
import os
#Assign a variable to load file from a path
file_to_load=os.path.join("OneDrive/Documents/Data Analytics/Election_Analysis/election_results.csv")
# Assign a variable to save the file to a path
file_to_save=os.path.join("OneDrive/Documents/Data Analytics/analysis.txt")
# Initialize a total vote counter
total_vote=0
# Candidate options and candidate votes
candidate_options=[]
candidate_votes={}
# Track the winning candidate, vote count, and percentage
winning_candidate= ""
winning_count= 0
winning_percentage =0
# Open the election results and read the file:
with open(file_to_load) as election_data:
    file_reader= csv.reader(election_data)
    # Read the head row
    headers= next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_vote +=1
        # Get the candidate name from each row
        candidate_name= row[2]
        # If candidate does not match any existing candidate add it to the canidate list
        if candidate_name not in candidate_options:
            # Add the canidate name ot the candidate list
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name]=0
    # Add a vote to that candidate's count
    candidate_votes[candidate_name]+=1

# Save the results to our text file:
with open(file_to_save,"w") as txt_file:
    #After opening the file print the final vote count to the terminal
    election_results= (
        f"\nElection Results\n"
        f"-------------------\n"
        f"Total Votes: {total_vote:,}\n"
        f"--------------------\n")
    print(election_results, end="")
    #After printing the final vote cound to the terminal save to the text file
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
    # Retrieve vote count and percentage
        votes= candidate_votes[candidate_name]
        vote_percentage= float(votes) / float(total_vote)*100
        candidate_results=(
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Print each candidate, their voter count, and percentage
    print(candidate_results)
    # Save the candidate results tou out text file
    txt_file.write(election_results)
    # Determine winning vote count, winning percentage, and candidate
    if (votes> winning_count) and (vote_percentage > winning_percentage):
        winning_count= votes
        winning_percentage = vote_percentage
        winning_candidate= candidate_name
    # Print the winning candidates' results to the terminal
    winning_candidate_summary= (
        f"------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)
