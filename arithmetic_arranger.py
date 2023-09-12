def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    firstline=""
    secondline=""
    thirdline=""
    fourthline=""

    for i in problems:
        no1 , operator , no2 = i.split()
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not no1.isdigit() or not no2.isdigit():
            return "Error: Numbers must only contain digits."
        
        maxlen=max(len(no1),len(no2))
        firstline+=no1.rjust(maxlen+2)+"    "
        secondline+=(operator+no2.rjust(maxlen+1))+"    "
        thirdline+="-"*(maxlen+2)+"    "
        if operator=="+":
            result=int(no1)+int(no2)
        else:
            result=int(no1)-int(no2)
        fourthline+=str(result).rjust(maxlen+2)+"    "
    toprint= firstline.rstrip() + '\n'+ secondline.rstrip() +'\n'+ thirdline.rstrip() +'\n'
    if show_answers:
        toprint+=fourthline
    
    return toprint
    
l=["32 + 698", "978 + 2", "45 + 43", "123 + 49", "999 + 90"]
print(arithmetic_arranger(l, True))

    
