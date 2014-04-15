def square (number):
    """Return the square of a number by multiplying the number by itself.
    """
    sqr_num = number * number
    return sqr_num

def returnDifference(num1,num2):
    """Return the difference between two numbers.
    """    
    return num1 - num2
    
def cubeFun(num1):
    '''a function that returns the cube of the function'''
    cube_num = num1 * num1 * num1
    return cube_num

def multiplyThree(num1,num2):
    '''a function that multiplies 2 numbers together and returns the result.'''
    response = num1 * num2
    return response

def convToCelc(temp1):
    '''Convert input to Degree Celcius'''
    toCelc = (temp1 - 32) * 5/9
    return toCelc

def convToFehr(temp1):
    '''Convert input to Degree Celcius'''
    toFehr = temp1 * 9 / 5 + 32
    return toFehr

input_num = 5
output_num = square(input_num)

print output_num
print returnDifference(8,3)
print cubeFun(3)
print multiplyThree(3,3)
print convToCelc(97)
print convToFehr(36)