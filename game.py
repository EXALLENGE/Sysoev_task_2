d = dict({1: 'hello', 2: 'world', 3: 'style'})
n = int(input('Выберете слово (1-3): '))
s = list(d[n]) #создает список букв
n = len(s) #количесво букв
word = ['*']*n
kol = 0 #ищет буквы (если 0 - игрок ввел букву, отсутствующую в слове)
mis = 1 #количесво ошибок
while mis <= 5 and s != word:
    l = input('Guess a letter: ') #вводимая игроком буква
    for p in range(n):
        if s[p] == l:
            word[p] = l
            kol += 1
    if kol > 0:
        print('Hit!')
    else:
        print('Missed, mistake', mis, 'out of 5.')
        mis += 1
    print('The word:', ''.join(word)) #выводит слово
    kol = 0
if mis == 6:
    print('You lost!')
elif s == word:
    print('You won!')