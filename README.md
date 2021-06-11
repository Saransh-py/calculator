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
