from googletrans import Translator

with open("text4.txt", 'w', encoding='utf-8') as f:
    with open('text3.txt', 'r', encoding='utf-8') as w:
        text = w.read()
        f.write(Translator().translate(text, dest='ru').text)