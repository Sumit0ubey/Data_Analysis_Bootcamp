def BMIcalculator(name: str, weight: float, height: float)->None:

    print(f"Hello, {name}!")
    print(f"Your weight is {weight} kg and your height is {height} m.")

    height = height / 100
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print(f"Your BMI is {bmi:.2f}, you are underweight.")
    elif 18.5 <= bmi < 25:
        print(f"Your BMI is {bmi:.2f}, you are normal weight.")
    elif 25 <= bmi < 30:
        print(f"Your BMI is {bmi:.2f}, you are overweight.")
    else:
        print(f"Your BMI is {bmi:.2f}, you are obese.")

while True:
    name = input("Enter your name: ")
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))
    BMIcalculator(name, weight, height)
    cont = input("To stop enter no/No: ")
    if cont.lower() == "no":
        break

