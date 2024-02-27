import math

def circle_stats(radious) :
    area = format(math.pi * radious ** 2,'.2f')
    circumference =  format(2 * math.pi * radious,'.2f')

    return area , circumference

a,c = circle_stats(2)

print("Area",a , "Circumference",c)