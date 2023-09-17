

# --------------------- Problem 1

def countFuncEValue():
    inputValue = "geeksforgeeks"         # this the input of user 
    countValue = inputValue.count("e")   # here we compare the inputValue to the e and store in single variable  
    print("\nThe number of occurrences of e in geeksforgeeks in ",countValue)                    # print the result 

countFuncEValue()                        # call the function

def countFunc3Value():
    inputValue = "abccdefgaa."
    countValue = inputValue.count("a")   # we need to count a for taking the result or output 3
    print("\nThe number of occurrences of e in abccdefgaa in ",countValue)                 
    
countFunc3Value()

# ---------------- Problem 2


def is_palindrome(str):                 # define the function with the parameter
  str = str.lower()                     # here we convert the string in lower case
  reversed_str = str[::-1]              # here we reversed the string and store in variable
  return str == reversed_str            # now we need t0 compare the lower case value to reversedString Value and the result into boolean 

str1 = "anna"                           # create the variable for store the input value
str2 = "India"                          # ""   

print("\nanna => ",is_palindrome(str1))              # call the is_palindrome function with inputValue variable parameter and print the return value 
print("\nIndia => ",is_palindrome(str2))              # ""


# ----------------------- Problem 3

def find_max_min(arr):                  # create the function with arr
  max = arr[0]                          # assign the Arr[0] value to the max variable
  min = arr[0]                          # assign the Arr[0] value to the min variable
  for i in range(len(arr)):             # [ range(len(arr) ] mean the length of array 
    if arr[i] > max:                    # check arr[i] is grater then arr[0], if yes then store the arr[i] in max
      max = arr[i]
    if arr[i] < min:                    # check arr[i] is smaller then arr[0], if yes then store the arr[i] in min 
      min = arr[i]
  return max, min                       # return the max and min value 


def situation(arr):                     # here we make the function to call the another function and print the return value 
    max, min = find_max_min(arr)
    print("\n{} => Maximum is: {}".format(arr ,max))
    print("\n{} => Minimum is: {}".format(arr ,min))

situation([1, 2, 3, 4, 5])              # call the function with array parameter
situation([5, 3, 7, 4, 2])


# ------------------- Problem 4 

def swapStrings():
    a = "Hello"
    b = "World"
    print("\nthe before swapping Strings value a:{} and b:{}".format(a,b))          # print the before value with his variable name
    a,b=b,a         # here we swap the value with using any third variable
    print("\nafter swapping Strings value a:{} and b:{}".format(a,b))               # print the after value with his variable name
    
swapStrings()              # call the function

# ------------------- Problem 5

def swapnumbers():
    a = "10"
    b = "50"
    print("\nthe before swapping numbers value a:{} and b:{}".format(a,b))          # print the before value with his variable name
    a,b=b,a         # here we swap the value with using any third variable
    print("\nafter swapping numbers value a:{} and b:{}".format(a,b))               # print the after value with his variable name
    
swapnumbers()              # call the function
