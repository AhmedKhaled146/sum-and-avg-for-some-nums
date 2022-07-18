num_of_numbers = int(input("How many numbers you want to sum: "))

def sum():
    global sum 
    sum = 0  
    for x in range(num_of_numbers):  
        sum += int(input(f"Enter Value {x + 1}: "))  

    return sum  

def avg():
    return sum/num_of_numbers

print("the summation  is", sum())
print("the average  is", avg())
