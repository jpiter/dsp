#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

import csv

def read_data(csv_file_path):
    f = open(csv_file_path)
    csv_f = csv.reader(f)
    data_parsed = list(csv_f)
    
    keys = data_parsed[0] #row with headers
    stats = list(map(list, zip(*data_parsed[1:]))) #games' statistics, transpose of the original data record, as a list of lists
    d = dict(zip(keys,stats)) # dictionary of lists, where keys are original headers)
    f.close()
    
    return d
    
def get_min_score_difference(football_data):
    
    goals_for = football_data['Goals'] # goals scored for the team, string entries
    goals_against = football_data['Goals Allowed'] # goals scored against the team, string entries
    
    goals_for = [int(i) for i in goals_for] # change string records to integer values
    goals_against = [int(i) for i in goals_against] # change string records to integer values
    
    diff = [goals_for[i]-goals_against[i] for i in range(len(goals_for))] # compute the difference of scores
    min_diff = min(diff) #find the smallest difference
    min_index = diff.index(min_diff) #find the index that corresponds to the smallest difference
    team = football_data['Team'][min_index] #find corresponding team name
    
    return(min_diff, team)
    
# Run the functions. I use path to my football.csv. I am not sure how to set this up correctly
# without asking the user to provide the path name
file_path = input('Enter the full path to football.csv: ')
data = read_data(file_path)
result = get_min_score_difference(football_data)
print(result[1]," team has the smallest difference of", result[0]," goals scored for and against the team.")



 
