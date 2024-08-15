class Config:
    def __init__(self): 
        # World
        self.row_length = 100
        self.column_length = 100

        self.tile_width = 5
        self.tile_height = 5

        self.generation_duration = 300

        self.tickspeed = 60

        self.danger_tiles = 0 #20
        self.food_tiles = 900

        self.danger_min_life = 15
        self.danger_max_life = 15
        self.danger_spread_chance = 100 # final chance will be 1 / spread_chance
        self.danger_damage = 5 

        self.food_min_spread = 60
        self.food_max_spread = 100
        self.food_spread_chance = 5 # final chance wile be 1 / spread_chance
        self.food_bonus = 42

        self.population_size = 300 

        self.organism_eyes_size = 2

        self.nn_layer_sizes = ((self.organism_eyes_size * 2 + 1) ** 2, 5, 9)

        self.organism_start_life = 150
        self.organism_tick_damage = 1
        self.border_damage = 100
        self.move_bonus = 1
