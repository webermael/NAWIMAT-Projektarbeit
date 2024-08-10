class Config:
    def __init__(self): 
        # World
        self.row_length = 100
        self.column_length = 100

        self.tile_width = 5
        self.tile_height = 5

        self.danger_tiles = 20
        self.food_tiles = 100

        self.danger_min_life = 15
        self.danger_max_life = 15
        self.danger_spread_chance = 100 # final chance will be 1 / spread_chance

        self.food_min_spread = 60
        self.food_max_spread = 100
        self.food_spread_chance = 5 # final chance wile be 1 / spread_chance

        self.population_size = 100

        self.organism_min_life = 60
        self.organism_max_life = 100
        self.organism_min_vit = 80
        self.organism_max_vit = 100