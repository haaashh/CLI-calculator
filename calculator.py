
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return "Can't divide by zero."
    return a/b
print("CALCULATOR\n")

while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\nChoose from 1-5: ")
    ch=(input())
    if ch=='5':
         print("Exited")
         break

    if ch not in ['1','2','3','4']:
         print("Invalid choice. Choose from the given options.")
         continue
    try:
         x = float(input("Enter first number: "))
         y = float(input("Enter second number: "))
    except ValueError:
         print("Invalid. Enter numbers.")
         continue

    if ch=='1':
            result = add(x,y)
    elif ch=='2':
            result = sub(x,y)
    elif ch=='3':
            result = mul(x,y)
    elif ch=='4':
            result = div(x,y)
    print(f"Result: {result}\n")


    
   