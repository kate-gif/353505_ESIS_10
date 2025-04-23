def task3():
    text = input("write a text")
    simbol_g = "g"
    simbol_o = "o"
    i = 0
    while text[i] != simbol_g:
        i += 1
    j = i
    while text[j] != simbol_o:
        j += 1
    print(text[i:j+1])
    return text[i:j+1]

def decoration(func):
    def wrapper():
        original = func()
        modified = original.upper()
        return modified
    return wrapper
#* args!!!!