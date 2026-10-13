
# first we will define a function that takes two numbers as input and returns their sum

def add_two_numbers(num_1, num_2):
    number_to_return = num_1 + num_2
    return number_to_return

# sconed we have to call the function to make it actually run

my_added_numbers = add_two_numbers(1, 1) # call means that we are using the function.

print(my_added_numbers) # will print 2


#############exercise: #######################
# functions 
# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."
# Global variables
count = 999
summary = "unset"
result = "unset"

def count_above(nums, limit): # this is a function called count_above that takes two arguments, nums and limit
    count = 0                 # this a local variable called count that is different from the global variable called count only works in the function
    for num in nums:          # the for loop will go through each number in the list nums and check if it is greater than the limit
        if num > limit:       # this will check if the number is greater than the limit
            count += 1        # this will add 1 to the count variable each time a number is greater than the limit
    return count              # this will return the value of count to the function call

print(count)
print(count_above(nums, limit)) 
print(count) # count is still 999 because the function has its own local variable called count

#Counting through the list (limit = 4):
#3 → no
#-1 → no
#7 → yes (count = 1)
#2 → no
#9 → yes (count = 2)
#0 → no
#4 → no (4 is not greater than 4)

# the function explaination :
# def count_above(nums, limit):
#   count = 0            # start a counter
#   for num in nums:      # look at each number
#       if num > limit:    # check the condition
#        count += 1      # update the counter
#   return count           # give back the result


####### second exercise: #######################


def summarize_text(s):
    summary = {"digits": 0, "letters": 0, "other": 0}
    for ch in s:
        if ch.isdigit():
            summary["digits"] += 1
        elif ch.isalpha():
            summary["letters"] += 1
        else:
            summary["other"] += 1
    return summary

print(summary)
print(summarize_text(text))
print(summary)


######################

def ca_area(length, width): #(length, width) are parameters
    area = length * width
    print(area)

ca_area(2, 2) # this is an argument that call for the function to work 




################## Aggregate with a mode ############

nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
result = "unset"

def aggregate(seq, mode, threshold):
    if mode == "sum":
        result = 0
    elif mode == "count":
        result = 0
    elif mode == "max":
        result = None

    for n in seq:
        if n < 0:
            continue
        if n >= threshold:
            if mode == "sum":
                result += n
            elif mode == "count":
                result += 1
            else:
                if result is None or n > result:
                    result = n
    return result
print("now!")
print(result)
print(aggregate(nums, "sum", limit))
print(aggregate(nums, "count", limit))
print(aggregate(nums, "max", limit))
print(result)



### Errors and try/except ####


values = ['10', '5', 'hello', "life", '8', 'three', '2']

for v in values:
    try:
        number = int(v)
        print(number)
    except ValueError:
        print("Skipping invalid value:", v)

