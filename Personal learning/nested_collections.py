#Initialize an empty tic-tac-toe board
#nested lists
tic_tac_toe_board = [["", "", ""], ["", "", ""], ["", "", ""]]
for row in tic_tac_toe_board:
    print(row)

#nested dictionary for student grades
student_grades = {
    "John": {
        "Math": {
    
        "Assignments": [90, 85, 77],
        "Exams": [88, 76]
        },
        "Science": {
        "Assignments": [92, 89],
        "Exams": [84, 77]
        },
        "English": {
        "Assignments": [85, 82, 94],
        "Exames": [90]
        }
    }
}
print(student_grades)
#To print John's Math exam grades
print(student_grades["John"] ["Math"] ["Exams"])