print("Enter a number less than 25")
n = int(input())
if n > 25:
    print("Error")
else:
    while n <= 25:
        print(f"Inside the loop, my variable is {n}")
        n += 1