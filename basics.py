# single-line comment

# single line
string = "hello world!!"
print(string)

# multi line string
multi_line_string = '''hello
    world
          !'''
print(multi_line_string)

# substrings
substring = string[0:5]
print(substring)

# integer
integer_number = 1
print(integer_number)

# float
float_number = 0.2
print(float_number)

# to string
number_to_string = str(integer_number)
print(number_to_string)

# to number
string_to_int_number = int("42")
string_to_float_number = float("42")
print(string_to_float_number)

# conditional
age = 18

if age >= 18:
    print("adult")
elif age >=12:
    print("teenager")
elif age >=3:
    print("child")
else:
    print("baby")

# ternary
old_enough = True if age >= 21 else False
print(old_enough)

# loops
while age < 23:
    print(age)
    age = age+1

# lists
sample_list =[1,2,42.0,"string",True]

# append element to the list
sample_list.append(False)

# print list
print(sample_list)

# print element of the list
print(sample_list[4])

# remove item
del sample_list[4]
print(sample_list)

# iterate over list
for item in sample_list:
    print(item)

# dictionaries
sample_dictionary = {}

sample_dictionary['type'] = 'Car'
sample_dictionary['brand'] = 'Tesla'
sample_dictionary['capacity'] = 4


print(sample_dictionary['type'])

del sample_dictionary['capacity']

print(sample_dictionary)

for k,v in sample_dictionary.items():
    print(k, '-', v)


#import classes
from sample_class import Sample

sample = Sample(1,2)
sample.print_attr_1()
sample.print_attr_2()
