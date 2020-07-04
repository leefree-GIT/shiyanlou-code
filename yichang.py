def get_number():
    "Returns a float number"
    number = float(input("Enter a float number:"))
    return number

while True:
    try:
        print(get_number())
    except ValueError:
        print("you entered a wrong value.")

