""" 
Author name : Rohan Chandra

Python Script to ask the user for the name of a file, read the contents of the file and calculate how many emails are sent each day 
of the week, Sunday through Saturday.The results are then plotted and displayed as a bar chart.

"""

from collections import defaultdict, OrderedDict
import sys
import os
import matplotlib.pyplot as plt

days = { 'Sun': 0, 'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6}

def getDay(item):
    """function to be used as a key for sort"""
    return days[item[0]]

fname = input('Enter a filename: ')                      #get a filename from the user 

try:
    
    fhand = open(fname)                                                             

except FileNotFoundError :
    
    print('File cannot be opened :', fname)              #handle invalid filenames
        
else :
    
    if os.stat(fname).st_size == 0:                      #check if the file size is 0 
        
        print ("Empty File!")
        
        sys.exit(0)                                      #handle empty files and exit                     
    
    dd = defaultdict(int)                                #initialize a defaultdict with int as factory                       
    
    for line in fhand :
        
        words = line.split()                             #split each line in the file into words 
        
        if len(words) != 0 and words[0] == 'From' :   
        
            if '@' in words[1] and '.' in words[1] :
               #add each day to the dictionary along with no of emails sent(update at each iteration)
               dd[words[2]] += 1                         
               
    if len(dd) > 0 :
        #create an OrderedDict sorted according to the order of days in the week
        a = OrderedDict(sorted(dd.items(), key=getDay))  
        keys, values = zip(*a.items())                   #convert the OrderedDict into 2 lists; 1 for keys and 1 for values 
        y_positions = range(len(keys))                   #generate y positions   
        
        #create bar plot
        plt.bar(y_positions, values)                     
        plt.xticks(y_positions, keys)
        plt.title("Total Number of e-mails sent for each day of the week")
        plt.ylabel("No of e-mails sent")
        plt.show()
        
        
        
   
        