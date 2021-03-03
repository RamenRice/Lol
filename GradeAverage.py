def average():
    x = sum(grade_list)
    y = x / how_many_grades
    print(y)
grade_list = []
conti = 'yes' and 'y'
while conti == 'y' or conti == 'yes':
    how_many_grades = int(input('How many gardes are being input? (Min of 5) : '))
    if how_many_grades >= 5:
        for i in range(how_many_grades):
            grades = int(input('Input grades : '))
            grade_list.append(grades)
        average()
        grade_list.clear()
        conti = input('Would you like to continue? : ').lower()
    else:
        print('Come back when you wish to put in grades')
        break
