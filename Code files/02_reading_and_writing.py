
# %%
test_file = open("../sample_data/test.txt", 'w')
test_file.close()

# %%
import os
os.remove('../sample_data/test.txt')

# %%
import csv

# %%
my_letters = ["a","b","c","d","e"]
with open('../sample_data/test.csv', 'w') as test_file:
    writer = csv.writer(test_file)
    writer.writerow(my_letters)

test_file.close()    

# %%
