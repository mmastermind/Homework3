import os
import csv
import numpy    
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
            #INSERT COUNTER OF VOTES HERE? WITH SAME LIST APPENDED FOR POSITIONS? CHECK
    return [conteo,data_mtx,cands]

def candidates(d):
    cands=[]
    for i in d:
        a = d[1][i].count("Khan")
    #cands.append(i[2]) = [i[2] for i in d if i[2] not in cands]
    return [a]

# Read in the CSV file
with open(working_file, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #skips header
    headers = next(csvreader)   
    #calls operations function in "d" variable
    print ('------ELECTION RESULTS-------')
    d = votesT(csvreader) #check why it returns the count of the total rows x three columns, if I'm comparing / summing only [2] of each row in def votesT
    print (f'Total votes are {d[0]}')
    print (d[2])
    #Unzip the data_mtx on three separate lists (columns) to count each candidate's votes
    x,y,z = zip(*d[1])
    #---------------alt code
    w=[]
    p = (len(d[2]))
    print (p)
    for i in range(p):
        w.append(z.count(d[2][i])/d[0]*100)
        print(f'Votes % for {d[2][i]} is {w[i]}%')


    #---------------working code
    f = (z.count(d[2][0])/d[0])*100
    g = (z.count(d[2][1])/d[0])*100
    h = (z.count(d[2][2])/d[0])*100
    K = (z.count(d[2][3])/d[0])*100
    print (f'Votes % for {d[2][0]} is {f} %')
    print (f'Votes % for {d[2][1]} is {g} %')
    print (f'Votes % for {d[2][2]} is {h} %')
    print (f'Votes % for {d[2][3]} is {K} %')
    #a=d[1].count("Khan")
    #print(a)
    #for j in d[2]:
    #    cands_perc[j].count = [i for i in d[1] if d[2][j]==d[1][2]
    #print (cands_perc[0])
    
    
