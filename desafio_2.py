def solve(equation: str):

    if "+" not in equation and "-" not in equation:
        return str(conta_resolv)
    equation2 = equation

    conta_resolv = []
    result = 0
    dicionario = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
   } 

    equation = equation.replace(" ", "")
    for char in range(len(equation)):
        if equation[char] == "+":
            conta_resolv.append(dicionario[equation[char-1]] + dicionario[equation[char+1]]) 
            equation2 = equation.replace(equation[:char+1], str(conta_resolv[0]))
        elif equation[char] == "-":
            conta_resolv.append(dicionario[equation[char-1]] - dicionario[equation[char+1]])
            equation2 = equation.replace(equation[:char+1], str(conta_resolv[0]))
        solve(equation2)


    for num in conta_resolv:
        result += num

    return result


var = "2 - 3 + 2"
print(solve(var))
    


