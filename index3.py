num1 = float(input("Введіть перше число: "))

num2 = float(input("Введіть друге число: "))

signs = input('action(+, -, *, /, =, тип): ')

if signs == "+":
    print(f"num1 + num2 = {num1 + num2}")
elif signs == "-":
    print(f"num1 - num2 = {num1 - num2}")
elif signs == "/":
    print(f"num1 / num2 = {num1 / num2}")
elif signs == "*":
    print(f"num1 * num2 = {num1 * num2}")
elif signs == "=":
    print(f"num1 = num2 = {num1 == num2}")
elif signs == "тип":
    print(num1, type(num1), num2, type(num2))
else: print("Введений неправильний знак")
