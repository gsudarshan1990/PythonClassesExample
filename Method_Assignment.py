
"""
Your job is to add three methods to the existing program:

1. A method print_students_data that prints the name of each one of the students in the dictionary, their age, and the classes they are taking, one student per line.

A sample output would be:

"Student: Gino who is 15 years old and is taking ['Piano', 'Guitar']"
"Student: Talina who is 28 years old and is taking ['Cello']"
"Student: Eric who is 12 years old and is taking ['Singing']"
2. A method print_student that prints the string shown above with the name, age, and classes of a student. It should take the name of the student as an argument and print only the data of that particular student. (Tip: you might consider using this method in the print_students_data  method to avoid repetition).

3. A method add_student  that adds a student to the existing students dictionary. The key used to add the student to the dictionary should be the name of the student and the value should be a list with the age, phone number, and classes that the student is taking. The method should take the name of the student as a parameter and a list with the data associated with that name as another parameter.

------------------------------

After adding these methods, you should create an instance of MusicSchool with 8 working hours, and 15000 as the initial revenue. Then, call each method through that instance like this:

<instance>.print_students_data()
<instance>.print_student("Gino")
<instance>.add_student("Jack", [60, "562-234-234", ["Piano"]])
Note: remember that students is a class attribute. You will need to use a particular syntax to access it in your methods.

------------------------------

Challenge: Right now, the existing program does not store the data in a file, so new student records are lost when the program ends. Could you make this program save the students' information to a .txt file using methods? This is not required to submit the assignment, but it's an interesting program that you might enjoy working on.

------------------------------
"""


class MusicSchool:
    students = {"Gino": [15, "653-235-345", ["Piano", "Guitar"]],
                "Talina": [28, "555-765-452", ["Cello"]],
                "Eric": [12, "583-356-223", ["Singing"]]}

    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue

    def print_students_data(self):
        for key,value in self.students.items():
            print('Student: {} who is {} years old and is taking {}'.format(key,value[0],value[2]))

    def print_student(self,student_name):
        if student_name in self.students:
            list1=self.students[student_name]
            print('Student: {} who is {} years old and is taking {}'.format(student_name,list1[0],list1[2]))

    def add_student(self,student_name,list1):
        self.students[student_name]=list1


m1=MusicSchool(8,15000)
m1.print_students_data()
print("================")
m1.print_student("Talina")
m1.add_student("Jack", [60, "562-234-234", ["Piano"]])
print("=============")
m1.print_students_data()