import random

name = input("whats your name?")
print("welcome", name)
print("game instruction")
print("you will try to find one of the city of turkey")
print("you have 5 mistakes. After finished your chance if you want you can try to find word ")
print("let the game begin")

words = ['adana', 'adıyaman', 'afyon', 'ağrı', 'aksaray', 'amasya', 'ankara', 'antalya'
          'ardahan', 'artvin' 'aydın', 'balıkesir',
         'bartın', 'batman', 'bayburt', 'bilecik', 'bitlis', 'bolu', 'burdur', 'bursa', 'çanakkale', 'çankırı', 'çorum',
         'denizli', 'diyarbakır', 'düzce', 'edirne', 'elaziğ', 'erzincan', 'erzurum', 'eskişehir', 'gaziantep',
         'giresun', 'gümüşhane', 'hakakri', 'hatay', 'ığdır', 'ısparta', 'istanbul', 'izmir', 'kahramanmaraş',
         'karabük', 'karaman', 'kars', 'kastamonu', 'kayseri', 'kırıkkale', 'kırklareli', 'kırşehir', 'kilis',
         'kocaeli', 'konya', 'kütahya', 'malatya', 'manisa', 'mardin', 'mersin', 'muğla', 'muş', 'nevşehir', 'niğde',
         'ordu', 'ordu', 'osmaniye', 'rize', 'sakarya', 'samsun', 'siirt', 'sinop', 'sivas', 'şanlıurfa', 'şırnak',
         'tekirdağ', 'tokat', 'trabzon', 'tunceli', 'uşak', 'van', 'yalova', 'yozgat', 'zonguldak']

word = random.choice(words)

guessnumber = 5

a=len(word)
z = list('_' * a)
print(' '.join(z), end='\n')

while guessnumber > 0:
    x = input("Guess a letter : ")

    if x not in word:
        guessnumber -= 1
        print("wrong guess!. you have {} guess left.".format(guessnumber))
        
    else :
        for i in range(len(word)):
         if x == word[i]:
          print("CORRECT")
          z[i] = x
        print(' '.join(z), end='\n')

answer = input("Do you want to guess a word? ['y' veya 'n'] : ")

if answer == "y":
    guess = input("What is your guess? : ")
    if guess == word:
        print("congratulations")

    else:
       print("YOU LOST.MAN HANGED")


        


