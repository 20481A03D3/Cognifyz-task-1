def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def temperature_converter():
    print("Temperature Converter")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        f_temp = float(input("Enter temperature in Fahrenheit: "))
        c_temp = fahrenheit_to_celsius(f_temp)
        print(f"{f_temp} Fahrenheit is equal to {c_temp:.2f} Celsius.")
    elif choice == 2:
        c_temp = float(input("Enter temperature in Celsius: "))
        f_temp = celsius_to_fahrenheit(c_temp)
        print(f"{c_temp} Celsius is equal to {f_temp:.2f} Fahrenheit.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the temperature converter
temperature_converter()
