import collections
import fileinput
import sys

class Player:
    def __init__(self, name, numbers):
        self.name = name
        self.deck = numbers

    def Dump(self, f):
        f.write("{}'s deck:".format(self.name))
        if self.deck:
            f.write(' {}'.format(self.deck[0]))
            for n in self.deck[1:]:
                f.write(', {}'.format(n))
        f.write('\n')

    def Draw(self):
        top_card = self.deck[0]
        del self.deck[0]
        return top_card

    def Add(self, card):
        self.deck.append(card)

    def IsDeckEmpty(self):
        return len(self.deck) == 0

def read_players():
    def read_player(input):
        name = None
        numbers = []
        for line in input:
            if line.isspace():
                yield name, numbers
                name = None
                numbers = []
            else:
                index = line.find(r':')
                if index >= 0:
                    name = line[:index].strip()
                else:
                    numbers.append(int(line))
        if name:
            yield name, numbers

    return [Player(name, numbers) for name, numbers in read_player(fileinput.input())]

def play_game(players):
    Play = collections.namedtuple('Play', ['player', 'card'])

    round = 0
    while True:
        round += 1
        sys.stderr.write('-- Round {} --\n'.format(round))
        plays = []
        for player in players:
            player.Dump(sys.stderr)
        for player in players:
            top_card = player.Draw()
            sys.stderr.write('{} plays: {}\n'.format(player.name, top_card))
            plays.append(Play(player, top_card))

        plays = sorted(plays, key=lambda play: play.card, reverse=True)
        winner = plays[0].player
        sys.stderr.write('{} wins the round!\n'.format(winner.name))
        for play in plays:
            winner.Add(play.card)
        out_of_cards = sum(player.IsDeckEmpty() for player in players)
        if out_of_cards == len(players) - 1:
            return winner.deck
        sys.stderr.write('\n');

def main():
    players = read_players()
    final_deck = play_game(players)

    sys.stderr.write('\n\n== Post-game results ==\n')
    for player in players:
        player.Dump(sys.stderr)

    score = sum(i * card for i, card in enumerate(reversed(final_deck), start=1))
    print(score)

if __name__ == "__main__":
    main()
