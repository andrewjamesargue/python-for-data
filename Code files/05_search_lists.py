# %%
my_letters = ["a","b","c","d","e"]

letter_to_find = input("What letter do you want to search for?")

if letter_to_find in my_letters:
    print(f"{letter_to_find} is in the list!")
else    
    print(f"{letter_to_find} is not in the list")

