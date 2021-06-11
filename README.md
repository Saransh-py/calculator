# calculator

```py
main.py

import ext as e

while True:
    num1inp = int(input("enter first number : "))
    num2inp = int(input("enter second number : "))
    opinp = input("enter operation : ")

    if opinp == "+":
        e.add(num1inp, num2inp)
    if opinp == "-":
        e.sub(num1inp, num2inp)
    if opinp == "//":
        e.divrounded(num1inp, num2inp)
    if opinp == "/":
        e.div(num1inp, num2inp)
    if opinp == "*":
        e.mul(num1inp, num2inp)
    print("Operation done")
```

```py
ext.py

def add(num1 = None, num2 = None):
    if num1 == None:
        raise Exception("You can't use a empty number")
        return
    elif num2 == None:
        raise Exception("You can't use a empty number")
        return
    elif num1 == str(num1)
        raise Exception("You must use a integer")
        return
    elif num2 == str(num2):
        raise Exception("You must use a integer")
        return

        
    print(num1 + num2)


def sub(num1 = None, num2 = None):
    if num1 == None:
        raise Exception("You can't use a empty number")
        return
    elif num2 == None:
        raise Exception("You can't use a empty number")
        return
    elif num1 == str(num1):
        raise Exception("You must use a integer")
        return
    elif num2 == str(num2):
        raise Exception("You must use a integer")
        return

        
    print(num1 - num2)
    
def mul(num1 = None, num2 = None):
    if num1 == None:
        raise Exception("You can't use a empty number")
        return
    elif num2 == None:
        raise Exception("You can't use a empty number")
        return
    elif num1 == str(num1):
        raise Exception("You must use a integer")
        return
    elif num2 == str(num2):
        raise Exception("You must use a integer")
        return

    print(num1 * num2)
    
def divrounded(num1 = None, num2 = None):
    if num1 == None:
        raise Exception("You can't use a empty number")
        return
    elif num2 == None:
        raise Exception("You can't use a empty number")
        return
    elif num1 == str(num1):
        raise Exception("You must use a integer")
        return
    elif num2 == str(num2):
        raise Exception("You must use a integer")
        return
        
    print(num1 // num2)
    
def div(num1 = None, num2 = None):
    if num1 == None:
        raise Exception("You can't use a empty number")
        return
    elif num2 == None:
        raise Exception("You can't use a empty number")
        return
    elif num1 == str(num1):
        raise Exception("You must use a integer")
        return
    elif num2 == str(num2):
        raise Exception("You must use a integer")
        return

        
    print(num1 // num2)
```
