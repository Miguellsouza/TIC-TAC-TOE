# TicTacBot 🎮

A console-based Tic-Tac-Toe game written in Python, where you play against a bot that picks its moves at random.

## About This Project

This game was proposed by **Cisco** as a hands-on project in one of its Python fundamentals courses (original assignment title: *Jogo da Velha*). I built this version while taking the course, which I completed and earned a certificate for.

## Features

- 3x3 board stored as a list of lists (`board[row][column]`)
- Squares numbered 1–9, row by row
- Player vs. computer (random moves, no AI)
- Win detection for rows, columns and both diagonals
- Game ends automatically when the board is full

## Requirements

- Python 3.6+ (uses f-strings)
- No external packages (only the standard library: `random`, `time`)

## How to Run

```bash
python Tic-tac-toe.py
```

## Game Rules

These rules describe how the game currently behaves:

1. **Board:** a 3x3 grid with squares numbered 1 to 9, row by row. A free square shows its number; an occupied square shows `X` or `O`.
2. **Symbols:** the player uses `X` and the computer uses `O`.
3. **Turn order:** in every round the computer moves first, then the player.
4. **Computer moves:** the computer picks a random number from 1 to 9. It does not check whether the square is free.
5. **Player moves:** the player types the number of the square they want.
6. **Occupied or invalid squares:** if the chosen square is already occupied, or the number is outside 1–9, **the turn is lost**. The board stays unchanged and the game moves on to the next round. This applies to both the computer and the player.
7. **Non-numeric input:** typing something that is not a number (like a letter) crashes the program.
8. **Winning:** a player wins by filling an entire row, column or diagonal with the same symbol. The check happens at the end of each round, after both moves.
9. **Draw:** if all 9 squares are filled, the game ends. No draw message is shown.

## How to Play

1. The bot places an `O` on a random square and the board is displayed.
2. Type the number of the square where you want to place your `X` and press Enter.
3. The updated board is shown, and the program checks for a winner.
4. Rounds repeat until someone completes a row, column or diagonal, or the board is full.

### Example board

```
[    1     ][    2     ][    3     ]
[    4     ][    O     ][    6     ]
[    7     ][    8     ][    9     ]
Choose a number:
```

## Project Structure

```
.
├── Tic-tac-toe.py   # Game source code
└── README.md
```

## How It Works

| Part | Description |
| --- | --- |
| `matriz` | 3x3 list holding either a free square number (int) or a symbol (`'X'`/`'O'`) |
| `auto()` | Returns a random number from 1 to 9 for the bot's move |
| Main loop | Bot moves → board is printed → player moves → board is printed → end-of-game checks |
| Win check | Compares the three cells of each row, column and diagonal |

## Known Limitations

This is a simple educational version. Some things you may want to improve:

- **No input validation:** typing a non-numeric value crashes the program, and choosing an occupied or out-of-range square wastes your turn.
- **Bot may skip its turn:** it picks any number from 1 to 9, even if that square is already taken.
- **No draw message:** when the board fills up, the game just ends.
- **Winner is not announced:** the message says where the line was formed, not whether `X` or `O` won.
- **Win check runs after both moves:** the bot's move and the player's move happen before the winner is checked.
- The loading animation at the top of the file is commented out.

## Ideas for Improvement

- Validate user input with `try/except` and a range check
- Make the bot choose only from free squares
- Add a draw message and announce the winner (`You won!` / `Computer won!`)
- Check for a winner after every single move
- Move the win-checking logic into a function
- Let the player choose who goes first

## License

This project is for educational purposes. Feel free to use and modify it.
