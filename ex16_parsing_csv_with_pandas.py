# Parsing CSV Files With the pandas Library

# using pandas library is highly recommended if you have a lot of data to analyze

# Anaconda
# conda install pandas

# Python
# pip install pandas

# Reading CSV Files With pandas
import pandas
df = pandas.read_csv('hrdata.csv')
print(df)
# pandas.read_csv() opens, analyzes, and reads the CSV file provided, 
# and stores the data in a DataFrame

# Here are a few points worth noting:
# * First, pandas recognized that the first line of the CSV contained
# column names, and used them automatically.
# * pandas is also using zero-based integer indices in the DataFrame. 
# That’s because we didn’t tell it what our index should be.
df = pandas.read_csv('hrdata.csv', index_col='Name')

# if you look at the data types of our columns, 
# you’ll see pandas has properly converted the Salary and 
# Sick Days remaining columns to numbers, but the Hire Date column is 
# still a String. This is easily confirmed in interactive mode
print(type(df['Hire Date'][0]))
# <class 'str'>

# You can force pandas to read data as a date with the parse_dates 
# optional parameter, which is defined as a list of column names to treat as dates:
df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)

print(type(df['Hire Date'][0]))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

# If your CSV files doesn’t have column names in the first line, 
# you can use the names optional parameter to provide a list of column names. 
# You can also use this if you want to override the column names provided in 
# the first line. In this case, you must also tell pandas.read_csv() 
# to ignore existing column names using the header=0 optional parameter:
df = pandas.read_csv('hrdata.csv', index_col='Employee', parse_dates=['Hired'], header=0, names=['Employee', 'Hired', 'Salary', 'Sick Days'])

# Writing CSV Files With pandas
import pandas
df = pandas.read_csv('hrdata.csv', index_col='Employee', parse_dates=['Hired'], header=0, names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('hrdata_modified.csv')