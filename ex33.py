def counter(count,step):
    i = 0
    numbers =[]
    for i in range(0,count,step):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Number now:",numbers)
        print(f"At the bottom i is {i}")

    print("The numbers:")

    for num in numbers:
        print(num)
