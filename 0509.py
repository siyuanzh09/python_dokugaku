def f1(x):
    """
    Return 2*x.
    :param x: int
    :return: int of 2*x.
    """
    return 2*x

def f2(x):
    """
    Print x and Return none.
    :param x: string
    :return: not defined.
    """
    print(x)

def f3(x,y=2,z=3):
    """
    Return z-y-x.
    :param x: int. required
    :param y: int. optional
    :param z: int. optional
    :return: int result of (z-y-x).
    """
    print(z-y-x)
    

def f4_1(a):
    """
    Return a/2.
    :param a: int.
    :return: int result of a/2.
    """
    return a/2

def f4_2(b):
    """
    Return b*4.
    :param b: int.
    :return: int result of b*4.
    """
    return b*4

"""
a=f4_1(10)
b=f4_2(a)
print (a)
print (b)
"""
x=input("num")
def f5(x):
    """
    Return float num of x and catch value error.
    :param x: int.
    :return: float. of x.
    """
    try:
        return float(x)
    except ValueError:
        print ("ERROR")

a=f5(x)
if a != 1 :
 print(a)
        

"""
print (f1(2))
f2(3)
f3(1)


age = input("enter your age:") 
int_age= int (age)

if int_age<21:
    print ("young")
else:
    print("old")
"""