class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.events = Event()

    def fire(self, args):
        self.events(args)


class GoalScoreInformation:
    def __init__(self, scorer, goals_scored):
        self.scorer = scorer
        self.goals_scored = goals_scored


class Player:
    def __init__(self, name: str, game: Game):
        self.name = name
        self.game = game
        self.goals_scored: int = 0

    def score(self):
        self.goals_scored += 1
        args = GoalScoreInformation(self.name, self.goals_scored)
        self.game.fire(args)


class Coach:
    def __init__(self, game: Game):
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):
        if isinstance(args, GoalScoreInformation) and args.goals_scored < 3:
            print(f"Coach says: Well done {args.scorer}")


def main():
    game = Game()
    messi = Player("Messi", game)
    ronaldo = Player("Ronaldo", game)

    coach = Coach(game)  # noqa: F841

    messi.score()
    ronaldo.score()
    ronaldo.score()
    ronaldo.score()


if __name__ == "__main__":
    main()
    # output:
    # Coach says: Well done Messi
    # Coach says: Well done Ronaldo
    # Coach says: Well done Ronaldo
