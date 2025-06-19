# 🐍 Snake Game in Python (OOP Version)

This is a complete implementation of the **classic Snake Game** using Python's `turtle` graphics module.
The game uses **Object-Oriented Programming (OOP)** principles for better modularity and readability.
It includes smooth snake movement, food collision logic, boundary detection, self-collision logic, and a score tracker.

## 🎮 Gameplay Overview

- The snake moves continuously across the screen.
- The player controls the snake using arrow keys (Up, Down, Left, Right).
- The snake grows longer each time it eats food.
- The game ends when:
  - The snake hits the wall.
  - The snake collides with itself.
- The score is displayed on the screen and increases with each food eaten.

## 🛠️ Technologies Used

- Python 3.x
- `turtle` module
- `time` module (for animation delay)

## 🧱 Project Structure

snake_game/
│
├── main.py # Main game loop
├── snake.py # Snake class: handles body segments and movement
├── food.py # Food class: generates food at random positions
├── scoreboard.py # Score class: handles score updates and game over message
└── README.md # Project documentation
