#Excel data to code using only dictionary

# Function to create a student dictionary
def create_student(stdid, stdname, standard, age, hindi, english, maths, science, computer):
    total = hindi + english + maths + science + computer
    student = {
        'stdid': stdid,
        'stdname': stdname,
        'standard': standard,
        'age': age,
        'hindi': hindi,
        'english': english,
        'maths': maths,
        'science': science,
        'computer': computer,
        'total': total
    }
    return student
# Function to print the student dictionary in tabular format
def print_students_table(students):
    # Print the table header
    print(f"{'StdID':<10}{'Name':<20}{'Standard':<10}{'Age':<5}{'Hindi':<10}{'English':<10}{'Maths':<10}{'Science':<10}{'Computer':<10}{'Total':<10}")
    print('-' * 95)
    
    # Print each student's details
    for student in students:
        print(f"{student['stdid']:<10}{student['stdname']:<20}{student['standard']:<10}{student['age']:<10}{student['hindi']:<10}{student['english']:<10}{student['maths']:<10}{student['science']:<10}{student['computer']:<10}{student['total']:<10}")

# Example usage
student1 = create_student('STD01','rani','10th',15,85,88,92,90,95)
student2 = create_student('STD02','aditi','10th',16,78,82,88,84,80)
student3 = create_student('STD03','Aman','10th',15,90,92,94,93,96)
student4 = create_student('STD04','anjali','10th',15,97,90,90,91,90)
student5 = create_student('STD05','puja','10th',15,76,81,39,87,90)
student6 = create_student('STD06','sakshi','10th',16,64,72,58,94,70)
student7 = create_student('STD07','yash','10th',15,92,95,91,92,59)
student8 = create_student('STD08','vishwa','10th',15,78,69,70,88,76)
student9 = create_student('STD09','sunny','10th',15,88,81,50,70,51)
student10 = create_student('STD10','Ashiya','10th',15,88  ,81,50,70,51)

# List of students
students = [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10]

# Print the students table
print_students_table(students)