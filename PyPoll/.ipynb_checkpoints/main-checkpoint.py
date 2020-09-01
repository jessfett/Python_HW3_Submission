#import dependences
import os
import csv

# csv file path
election_path = os.path.join("Resources", "election_data.csv")

#open file
with open(election_path) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    print(csvreader)
   
    csv_header = next(csvreader)


    
#Create a list for unique candidates
    candidate_name_unique = []

#find candidate count
    for row in csvreader:
        candidate_name_unique.append(row[2])

    candidate_count = [[row,candidate_name_unique.count(row)] for row in set(candidate_name_unique)]
    

    
#create lists for unique names and votes
    votes = []
    name = []
    
#add unique names and votes to lists
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

    winner = max(votes)
    
#determine the winner name
    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]       
            
            
#Find candidate percentages by dividing candidate totals by total votes
votes = len(candidate_name_unique)

total_correy = candidate_name_unique.count("Correy")
percentage_correy = int(total_correy) / int(votes)

total_otooley = candidate_name_unique.count("O'Tooley")
percentage_tooley = total_otooley / votes

total_li = candidate_name_unique.count("Li")
percent_li = total_li / votes

total_khan = candidate_name_unique.count("Khan")
percentage_khan = total_khan / votes

        
#create variables with clean outputs with commas and rounding
comma_total_khan='{:,}'.format(total_khan)
comma_total_correy='{:,}'.format(total_correy)
comma_total_li='{:,}'.format(total_li)
comma_total_otooley='{:,}'.format(total_otooley)
comma_total_votes='{:,}'.format(votes)
    
#print Election Summary and format to Percentage with 2 decimals                                           
print("Election Results")
print(f"-------------------------")
print(f"Total Votes: {comma_total_votes}")
print(f"-------------------------")
print(f"Khan: {percentage_khan:.2%} ({comma_total_khan})")
print(f"Correy: {percentage_correy:.2%} ({comma_total_correy})")
print(f"Li: {percent_li:.2%} ({comma_total_li})")
print(f"OTooley: {percentage_tooley:.2%} ({comma_total_otooley})")
print(f"-------------------------")
print(f"Winner: {winner_name}")
print(f"-------------------------")


#output summary
output_summary=("Election Results\n"
f"-------------------------\n"
f"Total Votes: {votes}\n"
f"-------------------------\n"
f"Khan: {percentage_khan:.2%} ({comma_total_khan})\n"
f"Correy: {percentage_correy:.2%} ({comma_total_correy})\n"
f"Li: {percent_li:.2%} ({comma_total_li})\n"
f"OTooley: {percentage_tooley:.2%} ({comma_total_otooley})\n"
f"-------------------------\n"
f"Winner: {winner_name}\n"
f"-------------------------\n")

#Write to Text File
output_file="election_data_output.txt"

with open(output_file, "w") as txt_file:
    txt_file.write(output_summary)





with open("PyPoll.txt", "w") as text_file:
    print(f"Election Results", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Total Votes: {votes}", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Khan: {percentage_khan:.3%} ({total_khan})", file=text_file)
    print(f"Correy: {percentage_correy:.3%} ({total_correy})", file=text_file)
    print(f"Li: {percent_li:.3%} ({total_li})", file=text_file)
    print(f"OTooley: {percentage_tooley:.3%} ({total_otooley})", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Winner: {winner_name}", file=text_file)
    print(f"-------------------------", file=text_file)