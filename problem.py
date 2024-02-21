#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def multiply_or_sum(number1,number2):
    product = number1*number2

    if product <= 1000:
        return product
    else :
        return number1+number2
    
result = multiply_or_sum(20,30)
print(f"the result is{result}")


result = multiply_or_sum(40,10)
print(f"the result is{result}")