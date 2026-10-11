#!usr/bin/python3


"""
def add_together(n1, n2, n3):
	x = n1 + n2 + n3
	print(x)
"""

# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

# Define a function named count_above that takes two arguments: seq and lim.
# Inside the function, create a local variable named count that starts at 0.'
# Loop through seq. For each number that is strictly greater than lim, increase count by 1.
# Return count from the function.

# Outside the function:
	#  Print the global count.
	#  Call count_above(nums, limit) and print the returned number.
	#  Print the global count again.

def count_above(seq, lim):
	count = 0
	for n in nums:
		if n > limit:
			count += 1
	return count


print(count)
print(count_above(nums, limit))
print(count)

"""
Why is the global count still 999, even though the function set a variable called count to 0 and then increased it?
bc function sets variable locally, global variables are not affected
"""
"""
 Define a function named summarize_text that takes one argument: s.
 Inside the function, create a local variable named summary that holds a dictionary with exactly these keys: "digits", "letters" and "other". Each key should start at 0.
 Loop through each character in s and use an if/elif/else chain:
	If the character is a digit, increase "digits" by 1.
	Else, if the character is a letter, increase "letters" by 1.
	Else, increase "other" by 1.
	 Hint: Strings have the methods isdigit() and isalpha().
 Return the summary dictionary.
 Outside the function:

    Print the global summary.
    Call summarize_text(text) and print the returned dictionary.
Print the global summary again.
"""

#s = "99 luftballons"
def summarize_text(s):
	#dig_val = 0
	#let_val = 0
	#oth_val = 0
	#summary = {"digits":dig_val, "letters":let_val, "other":oth_val}	 
	summary = {"digits":0, "letters":0, "other":0}
 # Iterate over characters in s 
	for char in s:
		if s.isdigit() == True:
			#"digits":+1
			#summary[(:+1),,]
			#summary(1, +1)
			#dig_val = +1
			summary["digits"] += 1
		elif s.isalpha() == True:
			summary["letters"] += 1
		elif s.isalpha() != True and s.isdigit() != True: summary["others"] += 1
		#else: oth_val = +1
	#summary = {"digits":dig_val, "letters":let_val, "other":oth_val}
	return(summary)

print(summary)						# Unset
print(summarize_text(text))			# 0:0:1 baaah

# outputs <function summarize_text at 0x7056a969f1c0>. See ya later
# Now outputs incorrect dict 

## What counts as "other" in text? 
#		Characters that aren't numbers or letters ,.!" etc"
# Check that the numbers add up to the length of the string using len(text).
# 		They do not

#__________________________________________________________________________________________
"""
 Define a function named aggregate that takes three arguments: seq, mode and threshold.
 Inside the function, create a local variable named result. Its starting value depends on mode:
	    If mode is "sum", start at 0.
    If mode is "count", start at 0.
    If mode is "max", start at None. This means “no qualifying value found yet”.

 Loop through each number n in seq:

    If n is negative, skip it.
    If n is at least threshold:
        If mode is "sum", add n to result.
		#        Else, if mode is "count", increase result by 1.
        Else, treat the mode as "max". If result is None or n is greater than result, set result to n.
	Hint: continue skips the rest of the current iteration and moves on to the next number.
 Return result from the function.
     Outside the function:
        Print the global result.
        Call the function three times and print each returned value:
            aggregate(nums, "sum", limit)
            aggregate(nums, "count", limit)
            aggregate(nums, "max", limit)
        Print the global result again.
"""


# def aggregate(seq, mode, threshold)


# What does aggregate(nums, "max", 100) return, and why?



