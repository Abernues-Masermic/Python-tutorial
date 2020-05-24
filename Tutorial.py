import pandas as pd
import random
from datetime import datetime, date, time
help(datetime.strptime)

date1 = datetime(2014, 5, 16, 14, 45, 5)
print(datetime.strptime('20140516134328', '%Y%m%d%H%M%S'))


'''
# read the data from the downloaded CSV file.
data = pd.read_csv('https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv')
# set a numeric id for use as an index for examples.
data['id'] = [random.randint(0, 1000) for x in range(data.shape[0])]

print(data.head(5))

print(data.iloc[0]) # first row of data frame (Aleshia Tomkiewicz) - Note a Series data type output.
print(data.iloc[1]) # second row of data frame (Evan Zigomalas)
print(data.iloc[-1]) # last row of data frame (Mi Richan)
# Columns:
print(data.iloc[:, 0]) # first column of data frame (first_name)
print(data.iloc[:, 1]) # second column of data frame (last_name)
print(data.iloc[:, -1]) # last column of data frame (id)

# Multiple row and column selections using iloc and DataFrame
print(data.iloc[0:5]) # first five rows of dataframe
print(data.iloc[:, 0:2]) # first two columns of data frame with all rows
print(data.iloc[[0, 3, 6, 24], [0, 5, 6]]) # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
print(data.iloc[0:5, 5:8]) # first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).

# Select rows with index values 'Andrade' and 'Veness', with all columns between 'city' and 'email'
data.set_index("last_name", inplace=True)
data.head()
print(data.loc[['Andrade', 'Veness'], 'city':'email'])

'''

#Python tips and tricks
class Enum:
    Tim, Bill, Joe = range(1,4)

print (Enum.Tim == 1)


x, y, z = [4, 5, 6]

print(y)


name = "Tim"
age = 15

print("Hello my name is", name, "and I am ", age, "years old")
print("Hello my name is " + name + " and I am " + str(age)+ " years old")

st = F"Hello my name is {name} {age + 10}"
print(st)


x = [2, 3, 4, 5]

for i, e in enumerate(x):
    print(i, e)


names = ["Tim", "Bill", "Joe"]
ages = [19, 64, 34, 76]
fav_color = ["blue", "red", "green"]

for tup in zip(names, ages, fav_color):
    print (tup)


import queue
x = ""
print(dir(x))
print(dir(queue.Queue))


x = [i for i in range(5) if i % 2 == 0]
print(x)

x = [[x, y] for x, y in zip(range(5), range(5, 10))]
print(x)


for _ in range(5):
    print("Hello")

DELIMETER = ","
words = ["hello", "my", "name", "is"]
print(DELIMETER.join(words))


st = "hello"
print(st[::-1])


import sys
x = 100
print(sys.getsizeof(x))  # num bytes


x = [1,2,3,4,4,5,5,6,6,1,1,1,1,1,2,2,2,2,3,4,5]
print(max(set(x), key=x.count))


x = [(1, 2, 10), (3, 4, 8), (1, 9, 4)]
print(max(x, key=lambda y: y[2]))


print("hello-" * 100 + "yu" * 80)


def func(*args, **kwargs):
    print(args, kwargs)

func(2, 3)
func(8, 7, 6, 5, 3)
func(2, 3, k=0, x=8, hey=10)



