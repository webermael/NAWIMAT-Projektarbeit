class Config:
    def __init__(self): 
        # World
        self.row_length = 100
        self.column_length = 100

        self.tile_width = 5
        self.tile_height = 5

        self.danger_min_life = 15
        self.danger_max_life = 15

        self.population_size = 50

        self.organism_min_life = 60
        self.organism_max_life = 100
        self.organism_min_vit = 80
        self.organism_max_vit = 100