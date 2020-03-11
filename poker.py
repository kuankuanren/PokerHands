class pokerHand(object):
    CARD="2345678TJQKA"
    result=["win","Tie","Lose"]
    def __init__(self,hand):
        self.values=''.join(sorted(hand[::3],key=self.CARD.index))
        self.suits = set(hand[1::3])
        self.is_flush = 0
        self.is_straight = 0
        self.score = 0
    def IsFlush(self):
        if len(self.suits)==1:
            self.is_flush = 1
            return 1
    def IsStraight(self):
        if self.values in self.CARD:
            self.is_straight = 1
            return 1
    def computeScore(self):
        self.IsFlush()
        self.IsStraight()
        self.score = (2 * sum(self.values.count(card) for card in self.values)  # 不同卡牌计数
                      + 13 * self.is_straight + 14 * self.is_flush,  # 顺子*13，同花*15
                      [self.CARD.index(card) for card in self.values[::-1]])
        return self.score

    def compare_with(self,other):
        if(self.computeScore() == other.computeScore()):
            return "Tie"
            print("Tie")
        elif(self.computeScore() >other.computeScore()):
            return "black wins"
            print("black wins")
        else:
            return "white wins"
            print("white wins")






