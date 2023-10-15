studets_file = 'students.csv'

with open(studets_file, 'w', newline='') as file:
    headers = ['Name ' 'LastName ' 'Age ' 'Specialty']
    file.write(','.join(headers) + '\n')

def add_students( name = '', lastname= '', age=0, specialty='' ):
    with open('students.csv', 'a', newline='') as file:
        file.write(f'{name},{lastname},{age},{specialty}\n')


def read_db():
    with open(studets_file, 'r' ) as file:
        inf =  file.read()
        print(inf)

def print_age(name = '', lastname= '', age=0, specialty=''):
    with open(studets_file, 'r') as file:
        lines = file.readlines()
        for line in lines :
            if age > 20:
                print(f'{name}, {lastname}, {age}, {specialty}')
            else:
                print('---')
        




add_students('alica', 'wonk', 19, 'lawyer')
add_students('Ola', 'Leins', 20, 'civil servant')
add_students('lora', 'Jains', 21, 'Doctor')
add_students('Andry' 'Mcalin', 19, 'Lawyer')
read_db()
print_age()
