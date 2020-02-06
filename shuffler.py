import random
import class_map
file_name = "students.txt"

def collect_students(file_name):
    r"""
    receive a .txt file with all the students names seperate with \n
    return an array with all the names
    """
    # reads the list of students from text file
    students_file = open(file_name, "r") 

    # create array with all the names
    students = []
    for x in students_file:
        x = x[0: -1].title()
        students.append(x)
    students.append([''])
    students.append(['Segev Kazav'])
    return students

def shuffle(students):
    """
    receive the students array
    returns new array randomly shuffled
    """
    temp = []
    temp.extend(students)
    random.shuffle(temp)
    return temp

if __name__ == "__main__":
    students = collect_students(file_name)
    shuffled_array = shuffle(students)
    class_map.create_map(shuffled_array)
    print(shuffled_array)