# !/usr/bin/python3
import sys
import csv
import re
import os

"""
Function that gets the filename used for writing it to the new .csv file. 
"""
def get_filename(filename):
    name = re.findall(r'.+/(.+)', filename)
    return name[0]

"""
Function that finds any cases of \ and replaces them with \" to keep
information accurate from original csv file.
"""
def escape_quotes(entry):
    new_entry = re.sub(r'\\', r'\"', entry)
    return new_entry.strip()

"""
Remove any instance of double quote at the end of a entry.
Additionally, replace any pairs of "" with a single quote.
This case happens due to how regex is written to handle escape characters.
"""
def remove_dq(entry):
    if entry.endswith('"'):
        entry = entry.rstrip(entry[-1])

    # any double quotes present, replace with single quote
    entry = entry.replace(r'""', r'"') 
    return entry.strip()

"""
Function that parses each .csv file.
Print's each new row of data to stdout.
"""
def parse(file):
    file_name = get_filename(file) # get filename.csv

    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',') # dictionary of csv

        # loop over all rows of csv
        for row in reader:
            curr_email = row['email_hash'] # get email 
            curr_cat = row['category'] # get category
            # handle cases with category
            curr_cat = escape_quotes(curr_cat) # case: there is a /" in our category
            # curr_cat = remove_dq(curr_cat) # case: "" from regex and " at end of string
            
            # build row of data
            data = '"' + curr_email + '","' + curr_cat + '","' + file_name + '"'
            print(data) # print data to stdout


"""
Checks whether an argument passed is a .csv file. 
Returns True if file is a .csv; false otherwise.
"""
def is_csv_file(filename):
    return len(filename) > 4 and filename[-4::] == '.csv'

"""
Driver of csv-combiner.py. 
"""
def main(argv):
    # check the len of argv; should have at least one 
    if len(argv) < 2:
        sys.exit('ERROR: Must pass in at least one .csv file')
    
    # print header of new .csv file
    print('\"email_hash\",\"category\",\"filename\"') 
    
    for file in argv[1:]:
        if(os.path.exists(file)): # check if file exists
            if (is_csv_file(file)): # check if file is valid .csv 
                parse(file) 
            else:
                error = 'ERROR: Non .csv file passed as argument. File passed: {}'.format(file)
                sys.exit(error)
        else:
            error = 'ERROR: File {} does not exist'.format(file)
            sys.exit(error)
    
# call main 
if __name__ == "__main__":
    main(sys.argv)