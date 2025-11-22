barrier = "="*20

name = input("Input Your Name ")
city = input("Input Your City ")
role = input("Input Your Role ")
hobby = input("Input Your Hobby ")
pet = input("Input Your Pet ")
length = str(len(name))

print(f"{barrier}\nUSER PROFILE SUMMARY\n{barrier}")
print(f"Name: {name}")
print(f"City: {city}")
print(f"Role: {role}")
print(f"Hobby: {hobby}")
print(f"Pet: {pet}\n")
print(f"Fun Fact: Your Name has {length} characters.\n")
print(f"Generated Nickname:\n{city} {pet}\n")
print(barrier)
print("Thanks for using this tool!")