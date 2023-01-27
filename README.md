# Battleship

## About the project and it's functions:

- This is a basic battleship game, with a regular 10x10 board and 13 ships. If you don't know how the game works, you can find a description here: [Battleship](https://en.wikipedia.org/wiki/Battleship_(game))
- First, the game will ask who the two players are.
- Second, you will see your board, where you can place your ships. Instructions and options are shown on the screen, by bigger ships you have to enter a beginning and end coordinate, logically, by one-length ships you only have to enter one coordinate.
- Entering a coordinate is validated:
  - You have to reenter the coordinate if you give invalid input. 
  - This also valid for shooting phase, where despite giving invalid input, you won't lose your turn. 
  - The size of the ships must be correct too. For example, by placing four-length ships you have to give 2 coordinates that are in a correct distance in order to place it on the board. If you fail to do so, you will get an error message and have to reenter the coordinates.
- Screen cleaner and sleep function:
  - Note: screen cleaner only works if you open the file in CLI, PyCharm doesn't want to accept this feature :( 
  - If you open the project in Pycharm, I recommend you to delete the screen cleaner function, because the PyCharm adds a weird rectangle in the first row, thereby indicating the screen cleaners presence. This causes the board to shift. 
  - The game is optimised for two players that are across each other. There is a timer built in for the current player to see and read messages, after that the screen is cleared, where there is an additional 5 seconds to give the laptop to the other player. This way, you won't see each other's board.
- The rest of the game works as a usual Battleship game. After both players place their ships on their board, the first player begins the shooting phase.
- Shooting phase:
  - Here you enter a coordinate to shoot. There are two possibilities:
    - 1.: You miss your shot -> There will be a message saying there is no ship on that position, and by your next shooting there will be an "M" letter showing that you have already guessed this coordinate, and you missed your shot.
    - 2.: You hit a ship -> There will be a message saying you hit a ship, and by your next shooting there will be an "H" letter showing that you have already guessed this coordinate and hit a ship.
      - If you sunk a ship, there will be a message saying that you sunk ***this many*** one/two/three/four -length ships. This message will stay on your screen, and will get updated how many ships you sunk so far, so you will know where you stand in the game. 
- Winning the game:
  - As you may know, the game ends if you sunk all your opponents the ships 