import random
barrels = 90  #бочонков
rows = 3      #строк в карточке
cols = 5      #цифр в строке
posits = 9    #всего позиций
gamers = [['Вундеркинд', False], ['Железяка', True], ['Железяка 2', True]]

class Card:
    def __init__(self, gamer):
        self.positions = []     
        self.numbers = random.sample(range(1, barrels+1), rows * cols)
        for i in range(rows):
            pos = random.sample(range(posits),cols)
            bpos = [1 if position in pos else 0 for position in range(posits)]
            self.positions.append(bpos)
        self.used = []
        self.gamer = gamer

    def show(self):
        print('Карточка: ', self.gamer[0])
        print('#'*(posits*3-1))
        for i in range(0, rows):
            string = ''
            itr = iter(sorted(self.numbers[i*cols : (i+1)*cols]))

            for j in range(0, posits):
                if self.positions[i][j]:
                    next_num = next(itr)
                    string += '$$ ' if next_num in self.used else '{0:2d}'.format(next_num)+' '
                else:
                    string += '   '
            print(string)
        print('#' * (posits*3-1))

    def decision(self, bar_num, rest_num):
        if self.gamer[1]:

            ans = bar_num in self.numbers
        else:
            print('Вынули бочонок: ', bar_num, ' (В мешке:', rest_num,')')
            ans =  input('Зачеркнуть цифру? (у/n) ') in 'ДдYy'
        return ans

    def cover(self, bar_num, decis):
        ans = (True, '')
        if bar_num in self.numbers:
            if decis:
                self.used.append(bar_num)
                if len(self.used) == rows * cols:
                    ans = (False, self.gamer[0]+' Ура! Все номера закрыты!')
            else:
                ans = (False, self.gamer[0]+' :(((! Пропущен номер на карточке!')
        else:
            if decis:
                ans = (False,  self.gamer[0]+' Ж(((! Нет такого номера :(((!')
        return ans

class Bag:
    def __init__(self):
        self.cur_pos = -1
        self.bag = random.sample(range(1, barrels + 1), barrels)

    def next_barrel(self):
        self.cur_pos += 1
        if self.cur_pos >= barrels:
            raise Exception('Бочонки RUN OUT')
        return self.bag[self.cur_pos], barrels-self.cur_pos-1

def new_game():
    games = []
    for gamer in gamers:
        games.append(Card(gamer))
    print('New game>><<>>>')
    loop = True
    bag = Bag()
    msg = ''
    while loop:
        barrel, rest_num = bag.next_barrel()
        for game in games:
            game.show()
            des = game.decision(barrel, rest_num)
            answer = game.cover(barrel, des)
            loop = answer[0]
            msg = answer[1]
            if not loop:
                break
        if rest_num == 0:
            loop = False
            msg = 'GAME OVER!'
    print(msg)
new_game()


