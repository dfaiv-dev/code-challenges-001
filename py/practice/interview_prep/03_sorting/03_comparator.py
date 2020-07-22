from functools import cmp_to_key

# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

class Player:
    def __init__(self, name, score):
        self.score = score
        self.name = name

    def __repr__(self):
        return {
            name: self.name,
            score: self.score
        }

    def comparator(a, b):
        # order by score (desc), name (asc)
        if a.score < b.score:
            return 1
        if a.score > b.score:
            return -1

        # scores equal, order by name
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1

        # everything equal
        return 0


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)