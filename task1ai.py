import random

class VacuumCleanerAgent:
    def __init__(self, grid_size):
        # initializes the grid and sets up the agent’s starting position and possible directions
        self.grid_size = grid_size
        self.grid = [['Dirty' if random.random() > 0.3 else 'Clean' for _ in range(grid_size)] for _ in range(grid_size)]
        self.x, self.y = 0, 0
        self.directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def print_grid(self):
        # prints the current state of the grid with borders for better visualization
        print('+' + '-' * (self.grid_size * 7 - 1) + '+')
        for row in self.grid:
            print('|' + '|'.join(f' {cell:6} ' for cell in row) + '|')
            print('+' + '-' * (self.grid_size * 7 - 1) + '+')

    def move(self, direction):
        # updates the agent’s position based on the given direction if it's within the grid boundaries
        dx, dy = self.directions[direction]
        new_x, new_y = self.x + dx, self.y + dy
        if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size:
            self.x, self.y = new_x, new_y

    def suck(self):
        # cleans the current room if it is dirty
        if self.grid[self.x][self.y] == 'Dirty':
            self.grid[self.x][self.y] = 'Clean'

    def is_clean(self):
        # checks if all rooms in the grid are clean
        return all(room == 'Clean' for row in self.grid for room in row)

    def take_action(self, action):
        # performs the specified action, either moving the agent or cleaning the room
        if action == 'Suck':
            self.suck()
        elif action in self.directions:
            self.move(action)

    def run(self):
        # runs the main loop of the agent’s actions until all rooms are clean, including printing the grid and agent’s position
        actions = ['Suck', 'U', 'D', 'L', 'R']
        steps = 0  # counter to limit how often the grid is printed
        while not self.is_clean():
            print(f'Agent at ({self.x}, {self.y})')
            self.print_grid()
            action = random.choice(actions)
            print(f'Action: {action}')
            self.take_action(action)
            steps += 1
        print('All rooms are clean!')
        self.print_grid()

# initialize and run the vacuum cleaner agent with a 3x3 grid
vacuum_cleaner = VacuumCleanerAgent(grid_size=3)
vacuum_cleaner.run()
