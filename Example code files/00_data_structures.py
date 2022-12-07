
# %%
my_letters = ["a","b","c","d","e"]

# %%
for current_letter in my_letters:
    print(f"the current letter is {current_letter}")

# %%
for current_letter in range(len(my_letters)):
    print(f"the current letter is {my_letters[current_letter]}")

# %%
# test_file = open("test.txt", 'w')

# %%
my_list = ["one","two","three",True, [1,2,3,4,5]]
print(my_list[0])

# my_tuple = (1, "two", 3, False, [1,2,3,4,5])
print(my_tuple[1])

# my_set = {"one", 2, "3", True, "five"}
print(my_set)

my_dict = {"bob": 1, 
            "alice": 2, 
            "jerry": 3, 
            "max": False, 
            "fiona": [1,2,3,4,5]}
print(my_dict)

my_range = list(range(2, 11, 2))
print(my_range)

my_letters = ["a","b","c","d","e"]
print(len(my_letters))




