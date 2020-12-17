import math
k="y"
while k == "y":
    x = str(input("Want area or volume(a/v):\n"))
    if x=="a":
        y = str(input("Enter the name of the shape:\n"))
        if y == "square" or y == "Square":
            z = int(input("Enter the length of side:\n"))
            print("The area is: ",4*z)
        elif y == "rectangle" or y == "Rectangle":
            z = int(input("Enter the length:\n"))
            w = int(input("Enter the breadth:\n"))
            print("The area is :",2*(z+w))
        elif y == "triangle" or y == "Triangle":
            z = int(input("Enter the height:\n"))
            w = int(input("Enter the length of base:\n"))
            print("The area is: ",((z*w)/2))
        elif y == "rhombus" or y == "Rhombus":
            z = int(input("Enter the length of the first diagonal:\n"))
            w = int(input("Enter the length of the second diagonal:\n"))
            print("The area is: ",((z*w)/2))
        elif y == "parallelogram" or y == "Parallelogram":
            z = int(input("Enter the height:\n"))
            w = int(input("Enter the length of the base:\n"))
        elif y == "Circle" or y == "circle":
            z = int(input("Enter the radius:\n"))
            print("The area is :",math.pi*((z)**2))
        else:
            print("Area for complex shapes is not in the code.")
    elif x=="v":
        y = str(input("Enter the name of the shape:\n"))
        if y == "cube" or y == "Cube":
            z = int(input("Enter the length of side:\n"))
            print("The volume is: ",z**3)
        elif y == "Cuboid" or y == "cuboid":
            z = int(input("Enter the length:\n"))
            w = int(input("Enter the breadth:\n"))
            t = int(input("Enter the height:\n"))
            print("The volume is :",z*w*t)
        elif y == "cone" or y == "Cone":
            z = int(input("Enter the height:\n"))
            w = int(input("Enter the radius:\n"))
            print("The volume is: ",(math.pi*z*(w**2))/3)
        elif y == "cylinder" or y == "Cylinder":
            z = int(input("Enter the height:\n"))
            w = int(input("Enter the radius:\n"))
            print("The volume is: ",(math.pi*z*(w**2)))
        elif y == "sphere" or y == "Sphere":
            z = int(input("Enter the radius:\n"))
            print("The volume is: ",(math.pi*(z**3)))
        else:
            print("Area for complex shapes is not in the code.")
    else:
        print("Enter a valid input\n")
    k = str(input("Want to continue?(y/n):\n"))
else:
    print("Thankyou for using the area/volume calculator!!")