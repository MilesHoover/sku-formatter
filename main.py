import re

# open the file for reading
# iterate through file to find skus
# skus are determined by an unbroken string of numbers separated by a space or a common or both like: "12345678, 123456789 987654321"
# I will use regex to parse out skus
# if a line has no numbers, go to the next line to keep checking until end of file
# format them and add them to a list_one
# strip any commas, padded zeros (like 0012345678), unnecessary spaces
list_one = []

with open("input.txt", "r") as file:
    for line in file:
        x = re.findall(r"\d*", line) # "\d" means decimal digits and "*" means 0 or more times
        for sku in x:
            print(re.findall(r"\A0*", sku)) # "\A" means matching any 0s                    #check re.sub and ^ tomorrow to kick out leading zeros before adding them to the list_one
            list_one.append(sku)

print("\nlist_one:")    
print(list_one)

# dedupe the list into a set
# iterate through the list adding a new sku to a set, for every sku in the original list, check it against what's been added to the new, deduped set. If it already exits, its a dupe and doesn't need to be added. 

# put the deduped set into a list_two with the single quotes added to each entry

# feed list_two to .join() to add ending commas except the last entry

# open the file for writing

# write to the file with formatted skus in a column with added formatting
# each sku should be on its own line surround by 's and a common at the end
# the last entry should not have a comma
# like:
# '12345678', 
# '123456789', 
# '987654321'

# close file