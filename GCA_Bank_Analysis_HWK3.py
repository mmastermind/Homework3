import os
import csv 
# Path to collect data from the Resources folder
working_file = os.path.join("Resources","budget_data.csv")
# Define the function and have it accept the 'wrestlerData' as its sole parameter
def ops(csvreader):
    data_mtx=[]
    adicion=0
    conteo = 0
    avgnum=0
    delta_lst=[]
    check = 0
    check2=0
    counter = 0
    #read through the matrix
    for row in csvreader:
        #adds every read row to the list
        data_mtx.append(row)
        #print(data_mtx)
        #sums all the p/l
        adicion = adicion + int(row[1])
        #checks total number of months/rows with counter if row has any value
        if (int(row[1]) != 0):
            conteo = conteo + 1
        #looks for numerator to compute average delta changes
        if counter==0:
            avgnum=int(row[1])
        else:
            delta = int(row[1])-avgnum
            delta_lst.append(delta)
            avgnum = int(row[1])
        #looks for minumum P/L
        if (int(row[1]) > check):
            check = check
            counter = counter +1
        else:
            check = int(row[1])
            counter = counter + 1
        #looks for max P/L
        if (int(row[1]) < check2):
            check2 = check2
            counter2 = counter2 +1
        else:
            check2 = int(row[1])
            counter2 = counter + 1
    #returns function variables to the program
    return [adicion,conteo,check,check2,avgnum,data_mtx,delta_lst]
# Read in the CSV file
with open(working_file, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #skips header
    headers = next(csvreader)   
    #calls operations function in "d" variable
    d = ops(csvreader)
    #Get the average of each month deltas
    average = sum(d[6])/(d[1]-1)
    #Finds row that matches check values in order to save the position/month in order to print it in the summary
    positionmax = [i for i in d[5] if int(i[1]) == int(d[3])]
    positionmin = [j for j in d[5] if int(j[1]) == int(d[2])]
    print("-------FINANCIAL ANALYSIS-------")
    print(f'Total months for the analysis are {d[1]}')
    print(f'Net Total P/L for all the months is $ {d[0]}')
    
    print (f'Average of the changes in P/L over the entire period was: $ {average}')
    print (f'Worst month result was in {positionmin[0][0]}: $ {d[2]}')
    print (f'Best month result was in {positionmax[0][0]}: $ {d[3]}')
