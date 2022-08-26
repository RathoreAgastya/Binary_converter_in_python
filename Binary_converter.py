
from rich.console import Console
console = Console()

def binary_converter() :
    binary = []
    check = True
    while check :
        number = console.input("Which number should be converted into binary: ")
        if number.isdigit() :
            number = int(number)
            orig_num = number
            check = False
        else :
            console.print(f"{number} is not an integer")
    
    convert_lp = True
    while convert_lp :

        if (number % 2) == 1 :
            binary.append(1)
            number = number // 2
            if number == 0 :
                binary.reverse()
                console.print(f"{orig_num} in binary is {binary} :smile:.")
                convert_lp = False
            else :
                pass
        else :
            pass

        if (number % 2) == 0 :
            binary.append(0)
            number = number // 2
            if number == 0 :
                binary.reverse()
                convert_lp = False
            else :
                pass
        else :
            pass
