my_f = open("text.txt", "w")
text = input("Enter text \n")
while text:
    my_f.writelines(text)
    text = input('Enter text \n')
    if not text:
        break
my_f.close()
