def add_numbers():
    numbers=input("enter numbers separated by spaces: ").split()
    total=0
    for num in numbers:
        total+=int(num)
    return total
result=add_numbers()
print("the sum is",result)
