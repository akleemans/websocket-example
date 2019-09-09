import random


class Board:
    """A board class"""
    board = []
    gems = 'wpryogb'
    dim = 8
    score = 0

    def __init__(self, test=False):
        if not test:
            self.generate_random()

    def __str__(self):
        return ''.join(self.board) + '|' + str(self.score)

    def move(self, start, target):
        # swap pieces
        temp = self.board[start]
        self.board[start] = self.board[target]
        self.board[target] = temp

    def generate_random(self):
        for i in range(64):
            self.board.append(random.choice(self.gems))
        self.remove_duplicates()

    def remove_duplicates(self, count_score=False):
        # check if already three in a row
        for i in range(64):
            # horizontal
            if i % self.dim <= 5:
                if self.board[i] == self.board[i + 1] == self.board[i + 2]:
                    # set new gem
                    if count_score: self.score += 10
                    print 'found match at', i
                    replacements = list(set(self.gems) - self.get_aligned_gems(i))
                    for j in range(3):
                        self.board[i + j] = random.choice(replacements)
            if i < self.dim * (self.dim - 2):
                if self.board[i] == self.board[i + self.dim] == self.board[i + self.dim * 2]:
                    if count_score: self.score += 10
                    # set new gem
                    print 'found match at', i
                    replacements = list(set(self.gems) - self.get_aligned_gems(i))
                    for j in range(3):
                        self.board[i + self.dim * j] = random.choice(replacements)

    def get_aligned_gems(self, pos):
        g = set()
        x, y = self.get_coords(pos)
        if x >= 1: g.add(self.board[self.get_pos(x - 1, y)])
        if x <= (self.dim - 2): g.add(self.board[self.get_pos(x + 1, y)])
        if y >= 1: g.add(self.board[self.get_pos(x, y - 1)])
        if y <= (self.dim - 2): g.add(self.board[self.get_pos(x, y + 1)])
        return g

    def get_coords(self, pos):
        x = pos % self.dim
        y = (pos - x) / self.dim
        return x, y

    def get_pos(self, x, y):
        return y * self.dim + x

    def set_from_string(self, s):
        self.board = list(s)
        return self.board
