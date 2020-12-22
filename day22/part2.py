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

game_count = 0
def play_game(players):
    Play = collections.namedtuple('Play', ['player', 'card'])

    global game_count
    game_count += 1
    game = game_count
    sys.stderr.write('=== Game {} ===\n\n'.format(game))

    previous_states = []

    round = 0
    while True:
        round += 1
        sys.stderr.write('-- Round {} (Game {}) --\n'.format(round, game))
        for player in players:
            player.Dump(sys.stderr)

        this_state = tuple([player.deck[:] for player in players])
        #for previous_state in previous_states:
        #    if this_state == previous_state:
        if this_state in previous_states:
            sys.stderr.write('Infinite Recursive Combat!!!\n')
            sys.stderr.write('The winner of game {} is {}!\n'.format(game, players[0].name))
            return players[0].name
        previous_states.append(this_state)

        plays = []
        for player in players:
            top_card = player.Draw()
            sys.stderr.write('{} plays: {}\n'.format(player.name, top_card))
            plays.append(Play(player, top_card))

        if all(len(play.player.deck) >= play.card for play in plays):
            sys.stderr.write('Playing a sub-game to determine the winner...\n\n')
            new_players = [Player(play.player.name, play.player.deck[:play.card]) for play in plays]
            winner_name = play_game(new_players)
            sys.stderr.write('\n...anyway, back to game {}.\n'.format(game))
            plays = sorted(plays, key=lambda play: play.player.name == winner_name, reverse=True)
        else:
            plays = sorted(plays, key=lambda play: play.card, reverse=True)

        winner = plays[0].player
        sys.stderr.write('{} wins round {} of game {}!\n'.format(winner.name, round, game))
        for play in plays:
            winner.Add(play.card)

        out_of_cards = sum(player.IsDeckEmpty() for player in players)
        if out_of_cards == len(players) - 1:
            sys.stderr.write('The winner of game {} is {}!\n'.format(game, winner.name.lower()))
            return winner.name
        sys.stderr.write('\n');

def main():
    players = read_players()
    winner_name = play_game(players)

    sys.stderr.write('\n\n== Post-game results ==\n')
    for player in players:
        player.Dump(sys.stderr)
        if player.name == winner_name:
            final_deck = player.deck

    score = sum(i * card for i, card in enumerate(reversed(final_deck), start=1))
    print(score)

if __name__ == "__main__":
    main()
