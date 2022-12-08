
# %%
my_letters = ["a","b","c","d","e"]
print(len(my_letters))


# %%
my_range = list(range(2, 11, 2))
print(my_range)

# %%
my_letters = ["a","b","c","d","e"]
for current_index in range(len(my_letters)):
    print(f"the current letter is {my_letters[current_index]}")

# %%
my_letters = ["a","b","c","d","e"]
my_letters.insert(0,"zzzz")
print(my_letters)

# %%
my_letters = ["a","b","c","d","e"]
my_letters.append("zzzz")
print(my_letters)

# %%
import random
my_letters = ["a","b","c","d","e"]
result = random.choice(my_letters)
print(result)

#%%
import random
my_letters = ["a","b","c","d","e"]
result = random.choices(my_letters, k=4)
print(result)
# %%
import random
my_letters = ["a","b","c","d","e"]
result = random.sample(my_letters, k=4)
print(result)

# %%

# %%
my_letters = ["a","b","c","d","e"]
letter_to_find = input("What letter do you want to search for?")
if letter_to_find in my_letters:
    print(f"{letter_to_find} is in the list!")
else:
    print(f"{letter_to_find} is not in the list")