#!usr/bin/python3
# Copied the thing I did I did yesterday bc I am hungry and can't focus
print("hello!")
print("I like french fries, do you?")

answer = input() #declare variable answer, prompt user to answer

# Output string depends on user input yes/no/other
if answer == "yes":
   print("Bonjour! I too, am a human")  
elif answer == "no":
   print("Sacre bleu! We must start your human training at once!")
else: 
   print("This is nonsense, I give up.")
