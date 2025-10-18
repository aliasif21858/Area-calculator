print("==================")
print("Area Calculator 📐")
print("==================")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

choice = int(input("Which shape: "))

if choice == 1:
    Base = float(input("Enter base: "))
    Height = float(input("Enter height: "))
    Area = 0.5 * Base * Height
    print("Area of the Triangle: ",Area)
elif choice == 2:
    Length = float(input("Enter Length: "))
    Width = float(input("Enter Width: "))
    Area = Length * Width
    print("Area of Rectangle: ",Area)
elif choice == 3:
    Side = float(input("Enter Side: "))
    Area = Side**2
    print("Area of Square: ",Area)
elif choice == 4:
    Radius = float(input("Enter Radius:"))
    Area = 3.14 * Radius**2
    print("Area of Circle: ",Area)
elif choice == 5:
    print("Quit")