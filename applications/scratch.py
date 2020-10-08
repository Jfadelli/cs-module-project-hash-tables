# importing "math" for mathematical operations  
import math  
  
# x = 2
# y = 2
# z = 8
  
# # returning the factorial 
# print ("The factorial of 5 is : ", math.factorial(x)) 
# print ("The power of 2*2 is : ", math.pow(x,y)) 
# print ("The factorial of 8 is : ", math.factorial(z)) 
x = 2
y = 10

def prob(x, y):
    v = math.pow(x, y)
    print('step 1: ', v)
    print(' ')
    v = math.factorial(v)
    print('step 2: ', v)
    print(' ')
    v //= (x + y)
    print('step 3: ', v)
    print(' ')
    v %= 982451653
    print('step 4: ', v)
    return v

prob(x,y)