#function definition
def sample_function():
    return 'Hello world!'

def sample_function_with_arguments(number_1 , number_2):
    return number_1 + number_2

def sample_function_with_multiple_return(number_1 , number_2):
    return number_1+number_2,number_1-number_2

print('Simple function:',str(sample_function()))
print('Function with arguments:',str(sample_function_with_arguments(4,10)))
print('Function with multiple return:',str(sample_function_with_multiple_return(5,2)))

