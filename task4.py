events =  [(1991, "ukraine become independent" ),
            (2019, "First sign of life on Mars from the 'Curiosity' Rover'"),
            (2023, "release of iPhone 15" ), (2004, "Олімпійські ігри в Афінах")]


time_dict = {year: event for year,  event in events}

set_years = set([1991, 2023, 2019, 2004])

years_to_visit = [1991, 2023, 2010]


print('список подій:')
for year, event in events:
    print(f"в  {year} році відбулвсь подія: {event} ")


print("Словник часу: ")
for year, event in time_dict.items():
    print(f"У {year}, році відбулась подія: {time_dict[year]}")


print("що ви хочете зробити:\n 1)Відправитись в якийст рік\n 2) глянути словник часу\n 3)спиок подій  ")
choice = input("введіть відповідь:")
match choice:
    case '1':
            for year in years_to_visit:
                try:
                    if year in set_years:
                        print(f"У {year}, році відбулась подія: {time_dict[year]}")
                    else:
                       raise ValueError
                except ValueError:
                    print(f'ви не можете відпраитись в {year}  рік')
    case '2':
            print("Словник часу: ")
            for year, event in time_dict.items():
                print(f"У {year}, році відбулась подія: {time_dict[year]}")
            print('також ти можеш:\n 1)видалити подію\n 2)добавити подію')
            choice2 = input('')
            match choice2:
                case '1':
                    num = input('введіть рік: ')
                    try:
                        set_years.remove(int(num))
                        print(f'ви видвлили 2 {num}')
                    except KeyError:
                         print('ви ввели число якого немає в словнику')
                case '2':
                    num = input('ввкдіть рік: ')
                    try:
                        set_years.add(int(num))
                        print(f'ви добавили {num}')
                    except KeyError:
                         print('ви ввели число якого немає в словнику')
                      

    case '3':
            print('список подій:')
            for year, event in events:
                print(f"в  {year} році відбулвсь подія: {event} ")


        
     


