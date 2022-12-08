# %%
import random
import csv

passenger_ages = []

with open("../sample_data/titanic.csv") as data_file:
    reader_object = csv.reader(data_file)
    for observation in reader_object:
        passenger_ages.append(observation[5])
data_file.close()
# print(passenger_ages[0:60])

# %%
passenger_ages = passenger_ages[1:]
# print(passenger_ages[0:60])

# %%
passenger_ages2 = []

for i in range(len(passenger_ages)):
    if passenger_ages[i] != "":
        passenger_ages2.append(int(float(passenger_ages[i]))) # Convert string to float then to integer or else can't plot it
# print(passenger_ages2[:60])

# %%
import matplotlib.pyplot as plt

plt.figure()
plt.hist(passenger_ages2)
plt.show()

# %%
print(passenger_ages2)

# %%

plt.figure()
plt.hist(passenger_ages2, edgecolor="black", bins=40)
plt.yticks(range(0,60,5)) # Do this instead of writing out a list of values
plt.show()

# %%
import random
import csv

passenger_details = []

with open("../sample_data/titanic.csv") as data_file:
    reader_object = csv.reader(data_file)
    for observation in reader_object:
        passenger_details.append([observation[4], observation[5]])
data_file.close()

print(passenger_details[:10])

# %%
passengers_clean = []

for record in passenger_details:
    if record[1] != "":
        passengers_clean.append(record)

male_ages = []
female_ages = []

for record in passengers_clean: # skip the first line with column headers
       
    if record[0] == 'male':
        male_ages.append(int(float(record[1]))) #convert string to float then integer for plotting\
    elif record[0] == 'female':
         female_ages.append(int(float(record[1])))
    else:
        pass

# %%
import matplotlib.pyplot as plt
plt.figure()

plt.hist(male_ages,
         alpha=0.5, # the transaparency parameter
         label="Men", 
         edgecolor="black", 
         bins=40)
plt.hist(female_ages,
         alpha=0.5,
         label="Women",
         edgecolor="black", 
         bins=40)
plt.legend(loc='upper right')
plt.title('Overlapping with both alpha=0.5')
plt.show()
plt.hist(passenger_ages2, edgecolor="black", bins=20)
plt.yticks(range(0,60,5)) # Do this instead of writing out a list of values
plt.show()
