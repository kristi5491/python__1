studets_file = 'students.csv'
def create_db():
    with open(studets_file, 'w', newline='') as file:
        headers = ['id', 'Name','LastName','Age','Specialty']
        file.write(','.join(headers) + '\n')

def add_students( id=0, name = '', lastname= '', age=0, specialty='' ):
    with open('students.csv', 'a', newline='') as file:
        file.write(f'{id},{name},{lastname},{age},{specialty}\n')


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
                        raise ValueError
                except ValueError:
                    print('---')


def rewrite_students():
    modified_lines = []
    modified_lines.append('id Name LastName Age Specialty\n')
    stud_id = int(input('Введіть id студента спеціальність ,якого ви  хочете поміняти: '))
    new_specialty = input('Введіть нову спеціальність: ')
    with open(studets_file, 'r',newline='' ) as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 5:
                id_str, name, lastname, age_str, specialty = parts
                id = int(id_str)
                if stud_id == id:
                    specialty = new_specialty
                modified_line = f'{id},{name},{lastname},{age_str},{specialty}\n'
                modified_lines.append(modified_line)
    with open(studets_file, 'w', newline='') as file:
        file.writelines(modified_lines)

def delete_student():
    modified_lines = []
    modified_lines.append('id Name LastName Age Specialty\n')
    stud_id = int(input('Введіть id студента  ,якого ви  хочете забрвти: '))
    with open (studets_file, 'r',newline='') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 5:
                id_str, name, lastname, age_str, specialty = parts
                id = int(id_str)
                if stud_id != id:
                    
                    modified_line = f'{id},{name},{lastname},{age_str},{specialty}\n'
                    modified_lines.append(modified_line)
    with open(studets_file, 'w', newline='') as file:
        file.writelines(modified_lines)



def sort_stud():
    students = []
   
    with open (studets_file, 'r',newline='') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 5:
                id_str, name, lastname, age_str, specialty = parts
                id = int(id_str)
                age = int(age_str)
                students.append((id, name, lastname, age, specialty))

    students.sort(key=lambda student: student[3])
    with open(studets_file, 'w', newline='') as file:
        file.write('id Name LastName Age Specialty\n')
        for student in students:
            id_str, name, lastname, age_str, specialty = student
            id = str(id_str)
            age = str(age_str)
            line = f'{id} {name} {lastname} {age} {specialty}\n'
            file.write(line)

def get_avarage():
    students = []
    specialty_data = dict()
    with open (studets_file, 'r',newline='') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 5:
                id_str, name, lastname, age_str, specialty = parts
                age = int(age_str)
                if specialty in specialty_data:
                    specialty_data[specialty]['total_age'] += age
                    specialty_data[specialty]['count'] += 1
                else:
                    specialty_data[specialty] = {'total_age':age , 'count': 1}
    print("Average Age of Students by Specialty:")
    for specialty, data in specialty_data.items():
        average_age = data['total_age'] / data['count']
        print(f"{specialty}: {int(average_age)} years")
                
        




create_db()

add_students( 1, 'alica', 'wonk', 21, 'Lawyer')
add_students( 2, 'Ola', 'Leins', 20, 'Doctor')
add_students( 3, 'lora', 'Jains', 35, 'Doctor')
add_students( 4, 'Andry' ,'Mcalin', 19, 'Lawyer')
add_students( 5, 'Ola' ,'Bublik', 28, 'Doctor')
# get_avarage()
read_db()
# print_age()
# rewrite_students()
# delete_student()
# sort_stud()
