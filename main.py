class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0

players = [Player(x.split('; ')[0], int(x.split('; ')[1]), int(x.split('; ')[2])) for x in lst_in]
players_filtered = list(filter(lambda x: x, players))