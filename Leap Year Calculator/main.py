year = int(input("Enter number of year: "))

# if year % 4 == 1:
#     print(f"Year {year} is a Leap year.")
# elif year % 100 == 0:
#     print(f"Year {year} is not a Leap year.")
# elif year % 400 == 0:
#     print(f"Year {year} is not a Leap year.")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap year.")
        else:
            print(f"{year} is not a Leap year.")
    else:
        print(f"{year} is a Leap year.")
else:
    print(f"{year} is not a Leap year.")