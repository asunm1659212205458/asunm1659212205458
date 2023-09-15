

# Define the Player class

class Player:

    def play(self):

        print("The player is playing cricket.")

# Define the Batsman class, derived from Player

class Batsman(Player):

    def play(self):

        print("The batsman is batting.")

# Define the Bowler class, derived from Player

class Bowler(Player):

    def play(self):

        print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes

batsman = Batsman()

bowler = Bowler()

# Call the play() method for each object

batsman.play()

bowler.play()
[tool.poetry.dependencies]
python = ">=3.10.0,<3.11"

[tool.pyright]
# https://github.com/microsoft/pyright/blob/main/docs/configuration.md
useLibraryCodeForTypes = true
exclude = [".cache"]

[tool.ruff]
# https://beta.ruff.rs/docs/configuration/
select = ['E', 'W', 'F', 'I', 'B', 'C4', 'ARG', 'SIM']
ignore = ['W291', 'W292', 'W293']

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"