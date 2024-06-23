#建立猜測清單
guess_list = []
guess = input('Guess the lowercase alphabet:')
guess_list.append(guess)
import random

a_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num =random.randint(0,27)
alpha = a_list[num]
#猜不到字母
while guess!=alpha:
    if guess<alpha:
        print('The alphabet you are looking for is alphabetically lower.')
        guess=input('Guess the lowercase alphabet:')
        guess_list.append(guess)
    if guess>alpha:
        print('The alphabet you are looking for is alphabetically higher.')
        guess=input('Guess the lowercase alphabet:')
        guess_list.append(guess)

#猜到字母
if guess==alpha:
    print('Congratulations!You guessed the the alphabet \"', alpha , '\" in ',len(guess_list),'tries.')
    print('Guess Histogram:')
    print('a-d:')
    print('e-h:')
    print('i-l:')
    print('m-p:')
    print('q-t:')
    print('u-x:')
    print('y-z:')