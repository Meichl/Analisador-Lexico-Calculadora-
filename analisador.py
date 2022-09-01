num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def someTokens(lista):
    tokens = []
    for exp in str(lista):
        if exp == "(":
            tokens.append("PARENTESES")
        elif exp == ")":
            tokens.append("PARENTESES")
        elif exp == "+":
            tokens.append("OPE MAIS")
        elif exp == "-":
            tokens.append("OPE MENOS")
        elif exp == "/":
            tokens.append("OPE DIVISÃO")
        elif exp == "*":
            tokens.append("OPE MULTI")
        elif exp == "=":
            tokens.append("IGUALDADE")
        elif exp in num:
            tokens.append("NÚMEROS")
        elif exp == " ":
            continue
        else:
            print('A expressão é invalida')
    return tokens


#expressão = "10"
expressão = "10 + 6 * 6"
#expressão = "6 / 5 * 6"
#expressão = "5 + 5 = 10"
#expressão = "nomes derivados"
print(someTokens(expressão))
