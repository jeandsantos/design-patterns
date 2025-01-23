from abc import ABC


class Game(ABC):
    def __init__(self, number_of_players: int):
        self.number_of_players = number_of_players
        self.current_player: int = 0

    def run(self):
        """Template method for Game."""
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f"Game over. The winner is {self.winning_player}")

    def start(self): ...

    def take_turn(self): ...

    @property
    def have_winner(self): ...

    @property
    def winning_player(self): ...


class Chess(Game):
    def __init__(self):
        super().__init__(number_of_players=2)
        self.max_turns = 10
        self.turn = 1

    def start(self):
        print(f"Starting a game of chess with {self.number_of_players} players.")

    @property
    def have_winner(self):
        return self.turn == self.max_turns

    def take_turn(self):
        print(f"Turn {self.turn} taken by player {self.current_player}.")
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self):
        return self.current_player


if __name__ == "__main__":
    game = Chess()
    game.run()

    # Output:
    # Starting a game of chess with 2 players.
    # Turn 1 taken by player 0.
    # Turn 2 taken by player 1.
    # Turn 3 taken by player 0.
    # Turn 4 taken by player 1.
    # Turn 5 taken by player 0.
    # Turn 6 taken by player 1.
    # Turn 7 taken by player 0.
    # Turn 8 taken by player 1.
    # Turn 9 taken by player 0.
    # Game over. The winner is 1
