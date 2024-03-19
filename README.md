    # YOUR PROJECT TITLE
    #### Video Demo:  <URL HERE>
    #### Description:
    TODO




# bruhN Game

A simple game written in Python using the Pygame library. The game features a player character that can jump, avoid obstacles, and accumulate a score.

## How to Play

- Press the **Spacebar** to make the player character jump.
- Avoid obstacles to keep the game going.
- Your score is displayed on the screen.

## Game Elements

### Player Character

- The player character can jump using the spacebar.
- The character's animation changes when jumping.

#### Important Functions

1. **player_input()**: Handles player input, specifically the spacebar for jumping.
2. **the_gravity()**: Manages the gravity effect on the player's vertical movement.
3. **animate_state()**: Updates the player character's animation based on its state.
4. **update()**: Integrates player input, gravity, and animation updates.
5. **player_animate()**: Controls the animation of the player character based on its position.

   **Brief Explanation**: This function manages the animation of the player character. If the character is in the air, it displays the jump animation; otherwise, it cycles through walking animations.

6. **collision_sprite()**: Checks for collisions between the player character and obstacles.

   **Brief Explanation**: This function uses Pygame's sprite collision detection to identify if the player character collides with any obstacles. If a collision occurs, the obstacle group is cleared, and the game ends.

### Obstacles

- Two types of obstacles: **Snail** and **Fly**.
- Obstacles move from right to left on the screen.
- The player must avoid colliding with obstacles.


### Scoring

- The game keeps track of the player's score based on the time survived.

#### Important Functions

1. **show_score()**: Calculates and displays the player's score on the screen.
2. **obs_mov()**: Controls the movement and rendering of obstacles.

   **Brief Explanation**: This function updates the position of each obstacle, renders them on the screen, and removes obstacles that have gone off-screen. It is responsible for the continuous movement of obstacles during gameplay.

3. **animation_state()**: Manages the dynamic animation of obstacles, smoothly transitioning between frames to bring Snail and Fly obstacles to life.

4. **update()**: Controls the horizontal movement of obstacles, creating the effect of obstacles advancing towards the player. It also handles the removal of off-screen obstacles to optimize resource usage.

5. **destroy()**: Removes obstacles that have moved off-screen, freeing up resources and maintaining game performance. The function utilizes the kill method to eliminate the obstacle sprite effectively.


## Installation

1. Install Python: [https://www.python.org/downloads/] or (https://www.python.org/downloads/)
2. Install Pygame: Run `pip install pygame` in your terminal.

## How to Run

1. Download the game code.
2. Open a terminal in the game directory.
3. Run the game using the command: `python game.py`

## Controls

- **Spacebar**: Jump

## Credits

- Game assets freepiks and MayTree (YouTube) obtained.

Enjoy playing the bruhN game! Feel free to customize and enhance it.
