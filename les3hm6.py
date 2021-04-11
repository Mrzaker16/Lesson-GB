def int_func(word):
    latinabc = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latinabc) else False


string = input("Enter string").split()
for i in string:
    res = int_func(i)
    if res:
        print(int_func(i), ' ')
