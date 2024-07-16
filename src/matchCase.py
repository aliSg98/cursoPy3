def runMatch():
    num = int(input("Enter a number: "))
    
    # match case
    match num:
        case num if num > 0:
            print("Positive")
        case num if num < 0:
            print("Negative")
        case _:
            print("Zero")
            
runMatch()