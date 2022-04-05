import random
import sys

a = 'グー'
b = 'チョキ'
c = 'パー'

cardist = [a, b, c]

my_card = int(input('次に従って出したい番号を入力してください\n1) グー\n2) チョキ\n3)パー\n'))

if my_card == 1:
    my_card = a
elif my_card == 2:
    my_card = b
elif my_card == 3:
    my_card = c
else:
    print('正しい番号を入力してください')
    try:
        raise ValueError
    except ValueError:
        print('プログラムを終了します。')
        sys.exit()


enemy_card = random.choice(cardist)

print('あなた：' + my_card)
print('相手：' + enemy_card)
print('---------------')

if my_card == enemy_card:
    print('引き分け！')
elif my_card == a and enemy_card == b:
    print('勝利！')
elif my_card == b and enemy_card == c:
    print('勝利！')
elif my_card == c and enemy_card == a:
    print('勝利！')
else:
    print('負け')