#!/usr/bin/env python3

# Variable
nums = [12,-1,-4,0,7,7,-9,3]
num=0

# Sum of numbers > 5
for number in nums:
    if number > 5:
        num=num+number
print(f"The sum of numbers > 5 = {num}")

# Function bucket(n)

def bucket(n):
    if n <= -5:
        return("LOW")
    elif n < 5 and n > -5:
        return("MID")
    else: return("HIGH")

print(f"Using n = -9 in bucket(n) returns {bucket(-9)}")
print(f"Using n = 7 in bucket(n) returns {bucket(7)}")

# Loop over nums and call bucket(n)
count_low=0
count_mid=0
count_high=0
odd_high=[]

for number in nums:
    if bucket(number) == "LOW":
        count_low += 1
    elif bucket(number) == "MID":
        count_mid += 1
    else: 
        count_high += 1
        if number % 2 == 1:
            odd_high.append(number)

print(f"Count for low = {count_low}, count for mid = {count_mid}, count for high = {count_high} and odd_high = {odd_high}")
