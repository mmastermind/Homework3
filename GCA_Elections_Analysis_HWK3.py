import os
import csv
# Path to collect data from the Resources folder
working_file = os.path.join("Resources","Resources_election_data.csv")
# Define the function and have it accept the 'wrestlerData' as its sole parameter
def votesT(csvreader):
    data_mtx=[]
    conteo = 0
    cands=[]
    #read through the matrix
    for row in csvreader:
        #adds every read row to the list
        data_mtx.append(row)
        #print(data_mtx)
        #sums all the votes
        if ((row[2]) != " "):
            conteo = conteo + 1
        if row[2] not in cands:
            cands.append(row[2])
    return [conteo,data_mtx,cands]
# Read in the CSV file
with open(working_file, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #skips header
    headers = next(csvreader)   
    #calls operations function in "d" variable
    print ('------ELECTION RESULTS-------')
    d = votesT(csvreader)
    print (f'Total votes are {d[0]}')
    print ('-----------------------------')
    #Unzip the data_mtx on three separate lists (columns) to count each candidate's votes
    x,y,z = zip(*d[1])
    w=[]
    #winner=0
    p = (len(d[2])
    for i in range(p):
        w.append(z.count(d[2][i])/d[0]*100)
        print(f'Votes % for {d[2][i]} is {w[i]}%')  
   #     if w[i]<Winner: 
    #        winner = winner 
     #   else:
      #      winner = w[i]
       #     position = i   
    print ('-----------------------------')
    print (f'Election Winner: {d[position]} with {winner} % votes')
    print ('-----------------------------')