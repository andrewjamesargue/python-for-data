
# %%
my_letters = ["a","b","c","d","e"]

# %%
for current_letter in my_letters:
    print(f"the current letter is {current_letter}")

# %%
for current_letter in range(len(my_letters)):
    print(f"the current letter is {my_letters[current_letter]}")

# %%
my_list = ["one","two","three",True, [1,2,3,4,5]]
print(my_list[0])

# %%
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

list_of_lists = [list1,list2]

print(list_of_lists)


# %%
my_dict = {"bob": 1, 
            "alice": 2, 
            "jerry": 3, 
            "max": False, 
            "fiona": [1,2,3,4,5]}
print(my_dict)