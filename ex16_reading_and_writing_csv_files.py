# Reading and Writing CSV Files in Python

# The Python csv library will work for most cases. If your work requires lots 
# of data or numerical analysis, the pandas library has CSV parsing 
# capabilities as well, which should handle the rest.

# CSV
# A CSV file (Comma Separated Values file) is a type of plain text file that
# uses specific structuring to arrange tabular data. 
# Because it’s a plain text file, it can contain only actual text data—
# in other words, printable ASCII or Unicode characters.
# The separator character is called a delimiter.

# The Python’s Built-in CSV Library

# Reading CSV Files With csv

import csv

with open('sample.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='!')  #  delimiter - default is comma (',')
    # Each row returned by the reader is a list of String elements containing the data found by removing the delimiters
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

# Reading CSV Files Into a Dictionary With csv

# You can read CSV data directly into a dictionary (technically, an Ordered Dictionary)
# The first line of the CSV file is assumed to contain the keys to use to build the dictionary. 
# If you don’t have these in your CSV file, you should specify your own keys 
# by setting the fieldnames optional parameter to a list containing them.
import csv

with open('sample.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='!')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row["product_id"]} works in the {row["account_number"]} department, and was born in {row["name"]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

# Optional Python CSV reader Parameters
#   delimiter - specifies the character used to separate each field. The default is the comma (',').
#   quotechar - specifies the character used to surround fields that contain the delimiter character. The default is a double quote (' " ').
#   escapechar - specifies the character used to escape the delimiter character, in case quotes aren’t used. The default is no escape character.


# Writing CSV Files With csv
# You can also write to a CSV file using a writer object and the .write_row() method:
import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John, Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])   

# The optional parameter quotechar
# If quoting is set to csv.QUOTE_MINIMAL, then .writerow() will quote fields only if they contain the delimiter or the quotechar. This is the default case.
# If quoting is set to csv.QUOTE_ALL, then .writerow() will quote all fields.
# If quoting is set to csv.QUOTE_NONNUMERIC, then .writerow() will quote all fields containing text data and convert all numeric fields to the float data type.
# If quoting is set to csv.QUOTE_NONE, then .writerow() will escape delimiters instead of quoting them. In this case, you also must provide a value for the escapechar optional parameter.


# Writing CSV File From a Dictionary With csv
import csv

with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})