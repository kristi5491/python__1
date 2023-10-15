studets_file = 'students.csv'

with open(studets_file, 'w', newline='') as file:
    headers = ['id ' 'Name ' 'LastName ' 'Age ' 'Specialty']
    file.write(','.join(headers) + '\n')

def add_students( id=0, name = '', lastname= '', age=0, specialty='' ):
    with open('students.csv', 'a', newline='') as file:
        file.write(f'{id}, {name},{lastname},{age},{specialty}\n')


def read_db():
    with open(studets_file, 'r' ) as file:
        inf =  file.read()
        print(inf)

def print_age(id = 0, name = '', lastname= '', age=0, specialty=''):
    with open(studets_file, 'r', newline='') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 5:
                id_str, name, lastname, age_str, specialty = parts
                try:
                    id = int(id_str)
                    age = int(age_str)
                    if age >= 20:
                        print(f'{id} {name}, {lastname}, {age}, {specialty}')
                    else:
                        print('---')
                except ValueError:
                    print('---')

def rewrite_students(id=0, name = '', lastname= '', age=0, specialty=''):
    with open(studets_file, 'w',newline='' ) as file:
        id_choose = input('Введіть номер який хочете поміняти: ')
        for line in file:
            parts = line.strip().split(',')




add_students( 1, 'alica', 'wonk', 19, 'lawyer')
add_students( 2, 'Ola', 'Leins', 20, 'civil servant')
add_students( 3, 'lora', 'Jains', 21, 'Doctor')
add_students( 4, 'Andry' 'Mcalin', 19, 'Lawyer')
read_db()
print_age()
