class Config:
    def __init__(self): 
        # World
        self.row_length = 128
        self.column_length = 128

        self.tile_width = 5

        self.generation_duration = 600

        self.tickspeed = 180

        self.danger_tiles = 100
        self.food_tiles = 1000

        self.danger_min_life = 15
        self.danger_max_life = 15
        self.danger_spread_chance = 100 # final chance will be 1 / spread_chance
        self.danger_damage = 20

        self.food_min_spread = 30
        self.food_max_spread = 50
        self.food_spread_chance = 2 # final chance wile be 1 / spread_chance
        self.food_bonus = 42

        self.mutation_rate = 0.01
        self.mutation_max_difference = 0.1

        self.population_size = 300 

        self.organism_eyes_size = 5

        self.nn_layer_sizes = (2 * (self.organism_eyes_size ** 2 + self.organism_eyes_size), self.organism_eyes_size * 5, self.organism_eyes_size * 2, 9)

        self.organism_start_life = 400
        self.organism_tick_damage = 1
        self.border_damage = 100
        self.move_bonus = 0.0000001
        self.survivor_bonus = 100
