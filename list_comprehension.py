# Creating a list of squares for numbers from 1 to 5:

square_num = [x**2 for x in range(1,6)]
print(square_num)

# Creating a list of even numbers from 1 to 10:
even_num = [x for x in range(1,11) if x%2==0]
print(even_num)

# Creating a list of uppercase letters from a string:
text = 'Hello World'
upper_string = [x for x in text if x.isupper()]
print(upper_string)

# Using a list comprehension with a condition to filter out negative numbers:
nums = [-3,-7,5,6,8,-1,0]
filted_num = [x for x in nums if x > 0]
print(filted_num)



