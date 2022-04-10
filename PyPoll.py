# Import needed modules
import csv
import os

# The data we need to retrieve
file_to_load = os.path.join('Resources', 'election_results.csv')
#Create a filename variable to save the file to a path
file_to_save = os.path.join('analysis', 'election_analysis.txt')
# 1. The total number of votes cast
#Initialize a total vote counter
total_votes = 0
# Candidate list
candidate_options = []
# Candidate votes dictionary
candidate_votes = {}
# Winning candidate variable
winning_candidate = ''
winning_count = 0
winning_percentage = 0
#Open the election results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        candidate_name = row[2]
        # 2. A complete list of candidates who received votes
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Track candidate vote count
            candidate_votes[candidate_name] = 0
        # Add count of candidate vote
        candidate_votes[candidate_name] += 1
    # 3. The percentage of votes each candidate won
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Get vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #print candidate names and percentage
        print(f'{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n')
    # 5. The winner of the election based on popular vote
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name   
    winning_candidate_summary = (
        f'------------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage: .1f}%\n'
        f'CONGRATULATIONS!\n'
        f'------------------------------\n'
    )
    print(winning_candidate_summary)
    
    #print(f'The winning candidate is: {winning_candidate} with {winning_count:,} votes and {winning_percentage: .1f}%\n CONGRATULATIONS!')
 


# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


#Close the file
