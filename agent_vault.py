print ("====AGENTVALUT====")
name = input("Enter your name:")
age = int(input("Enter your age:"))
city = input ("Enter your city:")
experience = int(input ("Enter your experience:"))
skill = input ("Enter your main skill:")

# age verification
if age>=18:
    print("Misson approved")
else:
    print("Traning requireds")

# experience classification
if experience>=2:
    print("Experienced")
elif experience == 1:
    print("Intermidiate")
else:
    print("Beginner")

# skill verification
if skill == "python":
    print("you can hired for python developer")
elif skill == "cybersecurity":
    print("you can hired for cybersecurity")
else:
    print("YOU CAN'T BE HIRED FOR ANY OF THE ABOVE ROLES")

# display profile
print("====BASIC PROFILE====")
print("NAME:",name)
print("AGE:",age)
print("CITY:",city)
print("EXPERIENCE:",experience)
print("SKILLS:",skill)

