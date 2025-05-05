# 1st solution 
# first_name = input("Hey, what's your first name? : ").strip()
# last_name = input("And your last name? : ").strip()
# print("Well, pleased to meet you,", first_name, last_name + ".")

# 2nd solution
def name():
    first_name = input("Hey, what's your first name? : ").strip()
    last_name = input("And your last name? : ").strip()
    print(f"Well, pleased to meet you, {first_name} {last_name}.")
name()
