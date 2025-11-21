from src.game import Game

def main():
    # Initialize the game
    game = Game(data_path='data')
    game.load_data()

    # Create a simple party for the player and the opponent
    game.player_party = [game.data_loader.creatures['lion']]
    opponent_party = [game.data_loader.creatures['snake']]

    # Start the battle
    game.start_battle(opponent_party)

if __name__ == "__main__":
    main()
