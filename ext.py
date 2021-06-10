"""
EXTRA FUNCTIONS
"""


def add(num1 = None, num2 = None):
    if num1 == None:
        raise Exception("You can't use a empty number")
        return
    elif num2 == None:
        raise Exception("You can't use a empty number")
        return
    elif num1 == str:
        raise Exception("You must use a integer")
        return
    elif num2 == str:
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
    elif num1 == str:
        raise Exception("You must use a integer")
        return
    elif num2 == str:
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
    elif num1 == str:
        raise Exception("You must use a integer")
        return
    elif num2 == str:
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
    elif num1 == str:
        raise Exception("You must use a integer")
        return
    elif num2 == str:
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