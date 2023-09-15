import time
import random

def delay_print(s):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(random.random() * 0.06)
    print()


character_name = input("Вітаю! Введіть ім'я вашого персонажа.")
delay_print("Вітаю, " + character_name +
            "! Тобі належить вибрати свій шлях у невеликій грі!. Від твоїх дій повність залежить розвиток сюжету.Отож почнемо")



delay_print("Вітаю!" + character_name + "Ви живете в селі та  у вас зовсім немає грошей, а підзаробити хочеться. ")
delay_print("Ви пішли в гори на пошук скарбів та хтось вцепився вам в ногу\nВи опустили голову та побачили що це маленька  мавпа")
delay_print('Ви не дуже любите тварин проте вирішили взято його з собою ')
delay_print('Пройшло вже дві години як ви йдете з тваринкою та натикаєтесь на стовп а на ньому дві позначки на право та на ліво.\nКуди вирішите піти:')
print("Варіанти відповідей:\n1) 'Вирішити за допомою лічилки'\n2) 'Куди мавпа побіжить туди і підем'")

inp_answer = input("\nВведіть відповідь: ")

question_index = 0

answers_array = []


def answer_1(answ):
    match answ:
        case '1': 
            delay_print('Лічилочка вказала піти на право')
        case '2':
            delay_print('Тваринка довго не думала і побігла на ліво ')
        case _:
            print(' Напиши цифру 1 чи 2')
            answ  = input("Введіть відповідь: ")
            answer_1(answ)
    return answ 

answer = answer_1(inp_answer)

answers_array.append(answer)

previous_answer = answers_array[question_index]

question_index += 1

match previous_answer:
    case '1':
        delay_print('Ви йшли по дорозі і побаачили пусту галявину та дерево посередині')
        delay_print('Постукавши по ньому воно почало говорити ')
        delay_print("Дерво: 'Я розумне дерево, і знаю все. Та вам потрібно відповісти на моє питання, щоб я вам це розказав'")
        delay_print(' Ви швидко погоджуєтесь та просите питання')
        delay_print("Так ось питання\nДерево: 'ПІД ЧАС ШТОРМУ В ТИХОМУ ОКЕАНІ 10 СІЧНЯ 1992 РОКУ У МОРІ ПОТРАПИЛО ПОРЯДКУ 30 ТИСЯЧ ЇХ. ЛЮДИ ДО СІХ ПІР знаходять їх у різних куточках світу в морських водах.Питання: 'що до сих пір вони знаходять?'")
        print('1)Бутилки\n2)Резинові качечки\n3)Ракушки')
        inp_answer = input("Введіть відповідь: ")
    case '2':
        delay_print("Тварина кудась швидко бігла та ви ледве встигали за нею ")
        delay_print('По дорозі ви підхопили ключ!!')
        delay_print('Нарешті ви наздогнаи мавпу та побачили що вона дивиться на печеру')
        print('Тепер перед вами вибір\n1.Зайти туди\n2)Пошукати можливо щось є біля печери')
        inp_answer = input("Введіть відповідь: ")

def answer_2(answ):
    match previous_answer:
        case '1':
            match answ:
                case '1':
                    delay_print('Подумайте краще')
                    answ  = input("Введіть відповідь: ")
                    answer_2(answ)
                case '2':
                    delay_print('ЦЕ правильна відьповідь.Ви виграли та можете спитати що завгодно!!')
                    delay_print(character_name + 'Запитує де лижить золото\n Дерево показує місце на карті та ми швидко біжимо туди')
                    delay_print('Ви знайшли мільйон доларів та пройшли гру!!! ')
                case '3':
                    delay_print('Подумуайте ще (кря кря)')
                    answ = input("Введіть відповідь: ")
                    answer_2(answ)
                case _:
                    print(' Напиши цифру 1 чи 2')
                    answ = input("Введіть відповідь: ")
                    answer_2(answ)
                
        case '2':
            match answ:
                case '1':
                    delay_print('Ви довго йшли та наткнулись на двері\n Згадавши, що ви знайшли ключ по дорозі, ви відкриваєте ним двері\n На щастя, ключ підійшов, та ви відкриваєте двері.')
                    delay_print('Кімната була наповнена золотом, і ви були раді, що взяли тварину, яка допоможе вам це все донести.')
                    delay_print('Вітаю з проходженням!!')
                case '2':
                    delay_print('Ви довго блукали по горах та вже стемніло\n ')
                    delay_print('Раптом ви чуєте, що хтось підкрадається, і це був ведмідь.\n Ви довго боретесь   але всеодно програєте в поєдинку ')
                    delay_print('На жаль, ви помираєте та Медвідь вас зїдає')
                case _:
                    print(' Напиши цифру 1 чи 2')
                    answ = input("Введіть відповідь: ")
                    answer_2(answ)

answer = answer_2(inp_answer)

answers_array.append(answer)

previous_answer = answers_array[question_index]

print('Як вам гра\n1)Норм \n2)пайдьот\n3)Класна')
feedback = input("Введіть відповідь: ")
