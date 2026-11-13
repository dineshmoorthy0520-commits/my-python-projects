students={
    1:"dhanush",
    2:"dinesh moorthy",
    3:"arun",
    4:"gokul",
    5:"yogesh",
    6:"tharun"
    }
name=input("Enter your name:")
if name in students.values():
    print("student verified")
else:
    print("student not verified")
roll_no=int(input("Enter your roll.no:"))
if roll_no in students.keys():
    print(name,roll_no)
e_marks=int(input("Enter english marks:"))
t_marks=int(input("Enter tamil marks:"))
m_marks=int(input("Enter maths marks:"))
s_marks=int(input("Enter science marks:"))    
so_marks=int(input("Enter social marks:"))
total_marks=e_marks+t_marks+m_marks+s_marks+so_marks
print(total_marks)
if total_marks<=300:
    print("pass")
else:
    print("fail")

             
    
