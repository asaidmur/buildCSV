#############################################################
#############################################################
#                                                           #
#  Super Fancy HaCkEr script that creates a csv file.       #
#                                                           #
#  To run script:                                           #
#  Open terminal, navigate to directory of script and type  #
#                                                           #
#  Python buildCsv.py                                       #
#                                                           #
#  Follow the prompts, enter number of rows,                #
#  enter a String for field 'parent account'                #
#  In the same directory you will find a 'test.csv' file #
#  containing the number of rows you specified.             #
#                                                           #
#  Highest I ran was 50 rows, but you could see how far it  #
#  can go. 100? 50,000? 9999999999? Sky is the limit        #
#                                                           #
#############################################################
#############################################################

import csv
import os

if os.path.exists('test.csv'):
    os.remove('test.csv')

with open('test.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['displayName', 'email', 'password', 'role','defaultLandingPage', 'parentAccount', 'accountType'])
    rowNum = int(raw_input("How many rows you want? "))
    parent_account = raw_input("parent account: ")

    for row in range(rowNum):
        filewriter.writerow(['TestUser'+str(row), 'TestUser'+str(row)+'@indicee.com', 'Welkom01', 'consumer', 'default', parent_account, 'user'])