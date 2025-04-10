def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def find_average(numbers):
    if len(numbers) == 0:
        return "List is empty"
    total_sum = calculate_sum(numbers)
    average = total_sum / len(numbers)
    return average

# Test data
numbers = [10]

# Function calls
total = calculate_sum(numbers)
average = find_average(numbers)

print("Total:", total)
print("Average:", average)

#with debugging in line 4 the output is:
#number = 10, numbers = [10,20,30,40,50], total = 0

#with debugging in line 11 the output is:
#total sum= 150, numbers = [10,20,30,40,50]

#watch total_sum/len(numbers) = 30.0

#added condition to breakpoint: len(numbers) == 1

