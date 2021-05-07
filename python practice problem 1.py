base_year = 2021

year_age = int(input("Enter your birth year or your age:\n"))

if len(str(year_age))>3:
    birth_year = year_age
    user_age = base_year-birth_year
else:
    user_age = year_age
    birth_year = base_year-year_age

if birth_year>base_year:
    print("You are not born yet")
elif birth_year<1900:
    print("You seems to be the oldest person alive")

print(f"You will complete your 100 years in the year of {birth_year+100}")

user_year = int(input("Enter a year and we will predict your age in that year:\n"))
print(f"You age will be {user_year-birth_year}")