import csv

headers = ['Name ' 'LastName ' 'Age ' 'Specialty']
# students = [['Ola', 'Leins', 20, 'civil servant'],
#             ['Jhon', 'Mcarti', 22, 'Artist'],
#             ['lora', 'Jains', 21, 'Doctor'],
#              ['Andry' 'Mcalin', 19, 'Lawyer'] ]

studets_file = 'students.csv'

with open(studets_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
def add_students( fname = '', lastname= '', age=0, specialty='' ):
    with open(studets_file, 'a') as file:
        writer = csv.writer(file)
        students_d = [fname, lastname, age, specialty]
        writer.writerow(students_d)
def read_db():
    with open(studets_file, 'r' ) as file:
        inf = csv.reader(file)
        for row in inf:
            print(row)

def print_age(fname = '', lastname= '', age=0, specialty=''):
    with open(studets_file, 'r') as file:
        inf = csv.reader
        for row in inf:
            age = int(age)
            fname,age = row
            if age > 20:
                print(f'{fname}, {lastname}, {age}, {specialty}')
            else:
                print('---')
        












add_students('alica', 'wonk', 19, 'lawyer')
add_students('Ola', 'Leins', 20, 'civil servant')
add_students('lora', 'Jains', 21, 'Doctor')
add_students('Andry' 'Mcalin', 19, 'Lawyer')

print_age()
