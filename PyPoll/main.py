import os
import csv

# read file
election_data_csv = os.path.join('PyPoll/Resources/election_data.csv')

totalVotes = 0 # total rows (not including the header is the total of votes)

# empty dictionary to catch votes should be:
# votesPerCandidate = {
#   "candidate_one": votes as int
# }
votesPerCandidate = {}

# open csv file
with open(election_data_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        totalVotes += 1
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1   
        
        


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")

for candidate, votes in votesPerCandidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(votesPerCandidate, key=votesPerCandidate.get)

print(f"Winner: {winner}")

# now write this to an output file

output_file = os.path.join("PyPoll/Analysis/output.txt")
with open(output_file,"w") as new:
    new.write("Election Results")
    new.write('\n')
    new.write("-------------------------")
    new.write('\n')
    new.write("Total Votes: " + str(totalVotes))
    new.write('\n')
    new.write("-------------------------")
    new.write('\n')

    new.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    new.write('\n')
  
    new.write("-------------------------") 
    new.write('\n')
    new.write(f"Winner: {winner}")
    new.write('\n')
