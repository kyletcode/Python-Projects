from math import pi

#My solution
def cal_circle(x): 
    area = pi * (pow(x, 2))
    return area

userinput = float(input("Enter a random radius: "))
cal_circle(userinput)
print("Radius chosen: " + str(userinput) +  "\nCalulated area is: " + str(cal_circle(userinput)))


