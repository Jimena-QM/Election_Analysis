# Election_Analysis

## Project Overview
Tom a Colorado Board of Elections employee hired me to complete the election audit for the US Congression precinct in Colorado. Our client is requesting a summary with following:

1. Total number of votes cast
2. List of all the candidates that participated in the election and received votes
3. Total number of votes per candidate
4. Percentage of votes per candidate
5. Winner of the election based on popular vote

## Resources
- Source file from client: election_results.csv
- Software: Python v3.7.6, Visual Studio Code v1.66.1

## Election Audit Results
The final results are:
- The total votes cast in the election were 369,711
- The candidates were:
  - Charles Casper Stockham
  - Diane DeGette
  - Raymon Anthony Doane
- The results for each candidate are:
  - Charles Casper Stockham received 23.0% of the votes and 85,213 votes
  - Diane DeGette received 73.8% of the votes and 272,892 votes
  - Raymon Anthony Doane received 3.1% of the votes and 11,606 votes
- The winner of the election was:
  - Candidate Diane DeGette, who received 73.8% of the votes and 272,892 votes

  ![Alt text](https://github.com/Jimena-QM/Election_Analysis/blob/main/Resources/Election_results_terminal.PNG "Terminal Election Results")

## Election Audit Summary
This script can be used to audit any election results. It's important that the file to be audited with the election results has at least the same three column structure: Ballot ID, County and Candidate and is in csv.

![Alt text](https://github.com/Jimena-QM/Election_Analysis/blob/main/Resources/election_results_structure.PNG "Structure")

The changes that have to be done within the code are: 
![Alt text](https://github.com/Jimena-QM/Election_Analysis/blob/main/Resources/Lines%20of%20Code%20to%20Change.PNG "Lines to Change")
-file_to_load with the Relative Path of the file (.csv) that contains the information to be audited
-A txt blank file should be created prior to modifying file_to_save with the Relative Path of the file where the results will be saved.
If more information regarding voters is present, such as sex, zip codes, age the script can be updated to reflect a deeper analysis. 
