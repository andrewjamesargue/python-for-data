
# %%
test_file = open("../sample_data/test.txt", 'w')
test_file.close()

# %%
import os
os.remove('../sample_data/test.txt')

# %%
my_cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
outfile = open('../sample_data/test.txt', 'w')
for city in my_cities:
    outfile.write(city+"\n")
outfile.close()

# %%
infile = open('../sample_data/test.txt', 'r')
my_cities2 = infile.readlines()
infile.close()
print(my_cities2)

# %%
infile = open('../sample_data/test.txt', 'r')
my_cities2 = infile.readlines()
infile.close()
for city in my_cities2:
    print(city.rstrip('\n'))

# %%
import csv
import os
my_header = ["id","name","age","grade"]
with open('../sample_data/test.csv', 'w', newline='') as test_file: # add newline='' or else it adds a blank row
    writer = csv.writer(test_file)
    writer.writerow(my_header)
test_file.close()    

# %%
import csv
my_data = ["0001","John Doe","22","A"]
with open('../sample_data/test.csv', 'a', newline='') as test_file:
    writer = csv.writer(test_file)
    writer.writerow(my_data)
test_file.close()    

# %%
import csv
my_students = [["0002","Karl Marx","24","A+"], ["0003","Adam Smith","21","A-"]]
with open('../sample_data/test.csv', 'a', newline='') as test_file:
    writer = csv.writer(test_file)
    for current_row in my_students:
        writer.writerow(current_row)
test_file.close() 
