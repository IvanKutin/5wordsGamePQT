words = []
with open('russian_nouns.txt', 'r', encoding='utf-8') as file:
    while True:
        s = file.readline()
        if len(s) == 6 and s != 'ящурка':
            words.append(s)
        if not s:
            break
with open('5letters.txt', 'w', encoding='utf-8') as file:
    for i in words:
        file.write(i)
