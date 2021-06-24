from tkinter import *
def start():
    print('This is the canculator.')
    enter=input("Do you want to calculate?(y/n)").lower()
    if enter in ['n', 'not', 'no']:
        exit()
    else:
        return enter


enter=start()

while(enter not in ['y', 'yes', 'no', 'n', 'not']):
    print('\nPlease Reply only with y or n only.\n===================================\n\n')
    enter=start()


exit_v='n'

print("\nAvailable operations:", "Operation done between n1 and n2:".rjust(35),
      "\n-> Additions", "n1 + n2".rjust(22),
      "\n-> Subtraction", "n1 - n2".rjust(20),
      "\n-> Multiplication", "n1 x n2".rjust(17),
      "\n-> Division", "n1 / n2".rjust(23),
      "\n-> Exponent", "n1 ^ n2".rjust(23) )

def calculator(res):
    result=res
    a=None
    b=None
    while a in [None]:
        a= input("Enter the first number(n1):  ").lower()
        if a==None:
            print('Error: Empty field.\n')
            continue
        if a not in ['ans', 'e', 'pi'] :
            a=int(a)
        elif a=='ans':
            a=result
        elif a=='e':
            a=2.718
        elif a=='pi':
            a=3.14159

    while b in [None]:
        b= input("Enter the second number(n2): ").lower()
        if b==None:
            print('Error: Empty field.\n')
            continue
        if b not in ['ans', 'e', 'pi'] :
            b=int(b)
        elif b=='ans':
            b=result
        elif b=='e':
            b=2.718
        elif b=='pi':
            b=3.14159
    
    op=input("Enter the operation: ").lower()
    op_check=0
    error=0
    
    while(op_check==0):
        if(op in {"add", "addition", "+"}):
            op='+'
            op_check=1
            break
        elif(op in {"subtract", "subtraction", "-"}):
            op='-'
            op_check=1
            break
        elif(op in  {"multiply", "multiplication", "x", "*"}):
            op='*'
            op_check=1
            break
        elif(op in {"divide", "division", "/"}):
            op='/'
            op_check=1
            break
        elif(op in {"exponent", "exp", "^", "**", "raise to power"}):
            op='**'
            op_check=1
            break
        else:
            print("Error: Operation not available.\n")
            op=input("Enter the operation: ").lower()
            
    if(op=='+'):
        result=a+b
    elif(op=='-'):
        result=a-b
    elif(op=='*'):
        result=a*b
    elif(op=='/'):
        result=a/b
    elif(op=='**'):
        result=a**b

    print("Result =", result)
    
    exit_v = input("Do you want to exit the calculator?(y/n)").lower()
    
    if(exit_v in ['y', 'yes']):
        exit()
    elif(exit_v in ['no', 'n', 'not']):
        print('\nStarting next calculation.\n===================================\n\n')
        calculator(result)
    else:
        while(exit_v not in ['y', 'yes', 'no', 'n', 'not']):
            print('\nPlease Reply only with y or n only.\n===================================\n')
            exit_v = input("Do you want to exit the calculator?(y/n)").lower()
    return

calculator(None)

b1=Button()