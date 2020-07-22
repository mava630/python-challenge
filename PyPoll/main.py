import csv, os

file = os.path.join('Resources','election_data.csv')
output_file = os.path.join('Analysis','Analysis.txt')

with open(file) as readfile:
    csvfile = csv.DictReader(readfile)

    total = 0
    candidate_list = []
    candidates = {}
    votes = 0

    for row in csvfile:
        total += 1
        # total = total + 1

        candidate = row['Candidate']

        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidates[candidate] = 0

        candidates[candidate] += 1

    output = ('\n\nElection Results' +
            '\n-------------------------' +
            f'\nTotal Votes: {total}' +
            '\n-------------------------')
for candidate in candidate_list:
        output += f'\n{candidate}: {candidates[candidate]/total*100:.3f}% ({candidates[candidate]})'

        if votes < candidates[candidate]:
         votes = candidates[candidate]
         winner = candidate

output += (f'\n-------------------------\nWinner: {winner}\n-------------------------')
print(output)

with open(output_file,'w') as output_txt:
    output_txt.write(output)