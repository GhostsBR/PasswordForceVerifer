import string
score = 0
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [")", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def countcharacters(password):
    global score
    add = len(password) * 4
    score += add
    return add

def countuppercaseletters(password):
    global score
    upper = 0
    for i in list(password):
        if i in string.ascii_uppercase:
            upper += 1
    if upper > 0:
        add = ((len(password) - upper) * 2)
    else:
        add = 0
    score += add
    return add


def countlowercaseletters(password):
    global score
    lower = 0
    for i in list(password):
        if i in string.ascii_lowercase:
            lower += 1
    if lower > 0:
        add = ((len(password) - lower) * 2)
    else:
        add = 0
    score += add
    return add


def countnumbers(password):
    global score
    numbers = 0
    hasLetter = False
    for i in list(password):
        if not i in string.digits:
            hasLetter = True
        if i in string.digits:
            numbers += 1
    if hasLetter:
        add = numbers * 4
    else:
        add = 0
    score += add
    return add



def countsymbols(password):
    global score
    password = password.replace(" ", "")
    password = password.replace("_", "")
    symbols = 0
    for i in list(password):
        if not i in string.ascii_letters and not i in string.digits and not i == " ":
            symbols += 1
    add = symbols * 6
    score += add
    return add


def countmiddlenumberssymbols(password):
    global score
    password = password.replace(" ", "")
    password = password.replace("_", "")
    numbers = 0
    symbols = 0
    for i in range(0, len(password)):
        if 0 < i < (len(password) - 1):
            if password[i] in string.digits:
                numbers += 1
            if not password[i] in string.ascii_letters and not password[i] in string.digits and not password[i] == " ":
                symbols += 1
    add = (numbers + symbols) * 2
    score += add
    return add


def countrequirements(password):
    global score
    completed = 0
    hasMinimum = False
    hasLower = False
    hasUpper = False
    hasNumber = False
    hasSymbol = False
    if (len(password)) >= 8:
        completed += 1
        hasMinimum = True
    for i in list(password):
        if i in string.ascii_lowercase:
            hasLower = True
        if i in string.ascii_uppercase:
            hasUpper = True
        if i in string.digits:
            hasNumber = True
        if not i in string.ascii_letters and not i in string.digits and not i == " " and not i == "_":
            hasSymbol = True
    if hasMinimum:
        if hasLower:
            completed += 1
        if hasUpper:
            completed += 1
        if hasNumber:
            completed += 1
        if hasSymbol:
            completed += 1
    if completed > 3:
        add = completed * 2
        score += add
    else:
        add = 0
    return add


def verifylettersonly(password):
    global score
    onlyLetters = True
    password = password.replace(" ", "x")
    hasOther = False
    for i in list(password):
        if i in string.ascii_letters or i in string.digits:
            hasOther = True
            break
    if hasOther:
        password = password.replace("_", "x")
    for i in list(password):
        if i in string.digits:
            onlyLetters = False
        if not i in string.ascii_letters and not i in string.digits:
            onlyLetters = False
    if onlyLetters:
        rem = len(password)
    else:
        rem = 0
    score -= rem
    return rem


def verifynumbersonly(password):
    global score
    onlyNumbers = True
    for i in list(password):
        if i in string.ascii_letters:
            onlyNumbers = False
        if not i in string.digits and not i in string.ascii_letters and not i == " ":
            onlyNumbers = False
    if onlyNumbers:
        rem = len(password)
    else:
        rem = 0
    score -= rem
    return rem


def countconsecutiveupperletters(password):
    global score
    consecutiveUpper = 0
    password = password.replace(" ", "")
    for i in range(0, len(password)):
        if i == 0:
            continue
        if password[i] in string.ascii_lowercase or password[i] in string.digits:
            continue
        if password[i] in string.ascii_uppercase and password[i-1] in string.ascii_uppercase and not password[i] == "_":
            consecutiveUpper += 1
    rem = consecutiveUpper * 2
    score -= rem
    return rem


def countconsecutivelowerletters(password):
    global score
    consecutiveLower = 0
    password = password.replace(" ", "")
    for i in range(0, len(password)):
        if i == 0:
            continue
        if password[i] in string.ascii_uppercase or password[i] in string.digits:
            continue

        if password[i] in string.ascii_lowercase and password[i-1] in string.ascii_lowercase and not password[i] == "_":
            consecutiveLower += 1
    rem = consecutiveLower * 2
    score -= rem
    return rem


def countconsecutivenumbers(password):
    global score
    consecutiveNumbers = 0
    for i in range(0, len(password)):
        if i == 0:
            continue
        if password[i] in string.ascii_letters:
            continue

        if password[i] in string.digits and password[i-1] in string.digits:
            consecutiveNumbers += 1
    rem = consecutiveNumbers * 2
    score -= rem
    return rem


def countsequentialletters(password):
    global score
    password = password.lower()
    sequential = 0
    oldSequentials = set()
    for i in range(len(password)):
        if password[i].isnumeric():
            continue
        if not password[i].isalpha() and not password[i].isnumeric() and not password[i] == " ":
            continue
        try:
            index = letters.index(password[i])
        except:
            continue
        if not (i+2) >= len(password):
            try:
                letters[index+2]
            except:
                continue
            if password[i+1] == letters[index+1]:
                if password[i+2] == letters[index+2]:
                    sequence = str(password[i]+password[i+1]+password[i+2])
                    if sequence in oldSequentials:
                        continue
                    sequential += 1
                    oldSequentials.add(sequence)
    password = password[::-1]
    for i in range(len(password)):
        if password[i].isnumeric():
            continue
        if not password[i].isalpha() and not password[i].isnumeric() and not password[i] == " ":
            continue
        try:
            index = letters.index(password[i])
        except:
            continue
        if not (i+2) >= len(password):
            try:
                letters[index+2]
            except:
                continue
            if password[i+1] == letters[index+1]:
                if password[i+2] == letters[index+2]:
                    sequence = str(password[i]+password[i+1]+password[i+2])
                    if sequence in oldSequentials:
                        continue
                    sequential += 1
                    oldSequentials.add(sequence)

    rem = sequential * 3
    score -= rem
    return rem


def countsequentialnumbers(password):
    global score
    sequential = 0
    oldSequentials = set()
    for i in range(len(password)):
        if password[i] in string.ascii_letters:
            continue
        if not password[i].isalpha() and not password[i].isnumeric() and not password[i] == " ":
            continue
        try:
            index = numbers.index(password[i])
        except:
            continue
        if not (i+2) >= len(password):
            try:
                numbers[index+2]
            except:
                continue
            if password[i+1] == numbers[index+1]:
                if password[i+2] == numbers[index+2]:
                    sequence = str(password[i]+password[i+1]+password[i+2])
                    if sequence in oldSequentials:
                        continue
                    sequential += 1
                    oldSequentials.add(sequence)
    password = password[::-1]
    for i in range(len(password)):
        if password[i] in string.ascii_letters:
            continue
        if not password[i].isalpha() and not password[i].isnumeric() and not password[i] == " ":
            continue
        try:
            index = numbers.index(password[i])
        except:
            continue
        if not (i+2) >= len(password):
            try:
                numbers[index+2]
            except:
                continue
            if password[i+1] == numbers[index+1]:
                if password[i+2] == numbers[index+2]:
                    sequence = str(password[i]+password[i+1]+password[i+2])
                    if sequence in oldSequentials:
                        continue
                    sequential += 1
                    oldSequentials.add(sequence)
    rem = sequential * 3
    score -= rem
    return rem

def countsequentialsymbols(password):
    global score
    sequential = 0
    oldSequentials = set()
    for i in range(len(password)):
        if password[i] in symbols:
            try:
                index = symbols.index(password[i])
            except:
                continue
            if not (i+2) >= len(password):
                if password[i+1] == symbols[index+1] and password[i+2] == symbols[index+2]:
                    sequence = str(password[i] + password[i + 1] + password[i + 2])
                    if sequence in oldSequentials:
                        continue
                    sequential += 1
                    oldSequentials.add(sequence)
    password = password[::-1]
    for i in range(len(password)):
        if password[i] in symbols:
            try:
                index = symbols.index(password[i])
            except:
                continue
            if not (i+2) >= len(password):
                if password[i+1] == symbols[index+1] and password[i+2] == symbols[index+2]:
                    sequence = str(password[i] + password[i + 1] + password[i + 2])
                    if sequence in oldSequentials:
                        continue
                    sequential += 1
                    oldSequentials.add(sequence)
    rem = sequential * 3
    score -= rem
    return rem


def start(password):
    print("\nPONTOS:")
    print(f"Quantidade de Caracteres: {bcolors.OKGREEN}+{countcharacters(password)} pontos{bcolors.ENDC}")
    print(f"Quantidade de Letras Maisculas: {bcolors.OKGREEN}+{countuppercaseletters(password)} pontos{bcolors.ENDC}")
    print(f"Quantidade de Letras Minusculas: {bcolors.OKGREEN}+{countlowercaseletters(password)} pontos{bcolors.ENDC}")
    print(f"Quantidade de Numeros: {bcolors.OKGREEN}+{countnumbers(password)} pontos{bcolors.ENDC}")
    print(f"Quantidade de Simbolos: {bcolors.OKGREEN}+{countsymbols(password)} pontos{bcolors.ENDC}")
    print(f"Quantidade de Simbolos/Numeros no Meio: {bcolors.OKGREEN}+{countmiddlenumberssymbols(password)} pontos{bcolors.ENDC}")
    print(f"Quantidade de Requerimentos Concluidos: {bcolors.OKGREEN}+{countrequirements(password)} pontos{bcolors.ENDC}")
    print(f"Apenas Letras: {bcolors.WARNING}-{verifylettersonly(password)} pontos{bcolors.ENDC}")
    print(f"Apenas Numeros: {bcolors.WARNING}-{verifynumbersonly(password)} pontos{bcolors.ENDC}")
    print(f"Quantida de Letras Maiusculas Consecutivas: {bcolors.WARNING}-{countconsecutiveupperletters(password)} pontos{bcolors.ENDC}")
    print(f"Quantida de Letras Minusculas Consecutivas: {bcolors.WARNING}-{countconsecutivelowerletters(password)} pontos{bcolors.ENDC}")
    print(f"Quantida de Numeros Consecutivos: {bcolors.WARNING}-{countconsecutivenumbers(password)} pontos{bcolors.ENDC}")
    print(f"Sequencia de Letras: {bcolors.WARNING}-{countsequentialletters(password)} pontos{bcolors.ENDC}")
    print(f"Sequencia de Numeros: {bcolors.WARNING}-{countsequentialnumbers(password)} pontos{bcolors.ENDC}")
    print(f"Sequencia de Simbolos: {bcolors.WARNING}-{countsequentialsymbols(password)} pontos{bcolors.ENDC}")
    print("\n")

def starttest(password):
    global score
    score = 0
    countcharacters(password)
    countuppercaseletters(password)
    countlowercaseletters(password)
    countnumbers(password)
    countsymbols(password)
    countmiddlenumberssymbols(password)
    countrequirements(password)
    verifylettersonly(password)
    verifynumbersonly(password)
    countconsecutiveupperletters(password)
    countconsecutivelowerletters(password)
    countconsecutivenumbers(password)
    countsequentialletters(password)
    countsequentialnumbers(password)
    #countsequentialsymbols(password)

    if score > 100:
        percent = 100
    elif score < 0:
        percent = 0
    else:
        percent = score

    return percent

def menu():
    global score
    score = 0
    print("=" * 60)
    print("\t\t\t\tVERIFICADOR DE SENHA")
    print("=" * 60)
    password = input("Digite a senha: ")
    start(password)

    if score > 100:
        percent = 100
    elif score < 0:
        percent = 0
    else:
        percent = score

    print(f"{bcolors.BOLD}Sua senha possui: {score} pontos, o que configura uma senha {percent}% segura.{bcolors.ENDC}")


testes = []

testes.append(("Teste1", 36))
testes.append(("Aa$%9w012", 100))
testes.append(("AWEpoiu", 25))
testes.append(("1234567890", 7))
testes.append(("imaginesó", 30))
testes.append(("á$%012ó~w", 100))
testes.append(("awd01002", 58))
testes.append(("8909801123á", 87))
testes.append(("abcabc123123", 68))
testes.append(("abácadabr4", 52))
testes.append(("_teste sobre isso__", 41))
testes.append(("!d$%*5 w", 88))
testes.append(("MEUNOME", 9))
testes.append(("meunome", 9))
testes.append(("AbCnomeABcMNo", 49))
testes.append(("<>@!_ *(#", 88))
testes.append(("_awDad_ ", 42))

def test():
    for i in testes:
        nota = starttest(i[0])
        if nota == i[1]:
            print(f"O teste {i[0]} foi correto!")
        else:
            print(f"O teste {i[0]} foi diferente! Esperado: {i[1]}, recebido: {nota}")
test()
#menu()


