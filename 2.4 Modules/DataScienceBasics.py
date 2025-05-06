import json

#Start by creating a function named calculate_mean in your module 
#that takes a list of numbers as an argument and returns the mean of those numbers.

def calculate_mean(nums):
    return sum(nums) / len(nums)

#Add a function named calculate_median to your module. 
#This function should take a list of numbers and return the median value.

def calculate_median(nums):
    return sorted(nums)[len(nums)//2]

#Write a function named load_data that takes a filename (a string) as its argument. 
#This function should read a file containing JSON data, parse it, and return the data as a list of dictionaries. 
#Assume each line in the file is a separate JSON encoded dictionary.

def load_data(filename):
    with open(filename, 'r') as file:
        data = [json.loads(line) for line in file]
    return data

#Create a function named filter_data that takes two arguments: 
#the dataset (a list of dictionaries) and a lambda function. 
#The function should return a new list containing all the items for which the lamba function returns True.

def filter_data(dataset, fun):
    return [item for item in dataset if fun(item)]

#Add a function called get_unique_values that takes the dataset and a key (string) as arguments. 
#This function should return a set of unique values for the specified key in the dataset.

def get_unique_values(dataset, key):
    return set(item[key] for item in dataset)

#Implement a function named transform_data that takes the dataset, a key, and a transform function. 
#The function should apply the transform function to each value of the specified key in the dataset and return the modified dataset.

def transform_data(dataset, key, fun):
    for item in dataset:
        item[key] = fun(item[key])
    return dataset

#Create a function named describe_data that takes the dataset and a key, 
#then calculates and prints the mean, and median for the numerical data associated with the key.

def describe_data(dataset, key):
    nums = [item[key] for item in dataset if isinstance(item[key], (int, float))]
    values = [item[key] for item in dataset]
    return calculate_mean(values), calculate_median(values)

#Write a function named aggregate_data that takes the dataset and a keys. 
#This function should return a dictionary with the unique values of the first key 
#as the keys and the sum of the corresponding values the same key.

def aggregate_data(dataset, key_to_group):
    data = {}
    for item in dataset:
        if item[key_to_group] in data:
            data[item[key_to_group]] += 1
        else:
            data[item[key_to_group]] = 1
    return data