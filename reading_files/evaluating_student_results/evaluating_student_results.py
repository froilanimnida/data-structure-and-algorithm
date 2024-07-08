"""
4.3.10   LAB   Evaluating students' results
Prof. Jekyll conducts classes with students and regularly makes notes in a text file.
Each line of the file contains three elements: the student's first name, the student's
last name, and the number of points the student received during certain classes.

The elements are separated with white spaces. Each student may appear more than once
inside Prof. Jekyll's file.

The file may look as follows:

John     Smith    5
Anna     Boleyn   4.5
John     Smith    2
Anna     Boleyn   11
Andrew   Cox      1.5
sample_file.txt
Your task is to write a program which:

asks the user for Prof. Jekyll's file name;
reads the file contents and counts the sum of the received points for each student;
prints a simple (but sorted) report, just like this one:
Andrew   Cox      1.5
Anna     Boleyn   15.5
John     Smith    7.0
Output

Note:

your program must be fully protected against all possible failures: the file's non-existence,
the file's emptiness, or any input data failures; encountering any data error should cause
immediate program termination, and the error should be presented to the user;
implement and use your own exceptions hierarchy – we've presented it in the editor; the
second exception should be raised when a wrong line is detected, and the third when the
source file exists but is empty.
Tip: Use a dictionary to store the students' data.
"""


class StudentsDataException(Exception):
    def __init__(self, message) -> None:
        Exception.__init__(self, message)


class BadLine(StudentsDataException):
    def __init__(self, message) -> None:
        StudentsDataException.__init__(self, message)


class FileEmpty(StudentsDataException):
    def __init__(self, message) -> None:
        StudentsDataException.__init__(self, message)


def grade_file_function(filename):
    try:
        grade_file = open(file=f'{filename}.txt', mode='r+')
        read_file = grade_file.readline()
        
        if len(read_file) == 0:
            raise FileEmpty(message="Empty File")
        for line in read_file:
            if line.isspace():
                raise BadLine(message="Bad Line Detected")
            else:
                grade_file.seek(0)
                break
    except IOError as io_error:
        print(f'IOError occurred: {io_error}')
    except FileEmpty as file_empty:
        print(file_empty)
    except BadLine as bad_line:
        print(bad_line)
    else:
        with grade_file:
            lines = grade_file.readlines()
            new_copy = {}
            for line in lines:
                x = line.split()
                current_name = f"{x[0]} {x[1]}"
                current_score = float(x[2])
                if current_name in new_copy:
                    existing_score = float(new_copy.get(current_name))
                    new_copy.update({current_name: existing_score + current_score})
                    continue
                
                new_copy[current_name] = current_score
                
            sorted_result = dict(sorted(new_copy.items(), key=lambda i: i[1], reverse=True))
            grade_file.seek(0)
            grade_file.truncate()
            for y, z in sorted_result.items():
                name_split = y.split()
                grade_file.write(f"{name_split[0]}\t\t{name_split[1]}\t\t{z}\n")
                print(y, z)


x = input("Please type in the filename: ")
grade_file_function(filename=x)
