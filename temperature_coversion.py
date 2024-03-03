while True:
    user_choice = input("Do you want to convert from Fahrenheit (F) or Celsius (C)? ")

    if user_choice == "F":
        x = int(input("Please enter Fahrenheit temperature: "))
        fahrenheit_to_celsius = (x - 32) * 5/9
        print(f"{x} degrees Fahrenheit is equal to {fahrenheit_to_celsius} degrees Celsius.")

    elif user_choice == "C":
        c = int(input("Please enter Celsius temperature: "))
        celsius_to_fahrenheit = (c * 9/5) + 32
        print(f"{c} degrees Celsius is equal to {celsius_to_fahrenheit} degrees Fahrenheit.")

    else:
        print("Sorry, I didn't understand that. Please enter 'F' or 'C'.")