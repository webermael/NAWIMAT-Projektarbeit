interface_values = {
    "world": 
    {
        "size": 
        {
            "column_length": ["Column Length", 0, 128, 1], 
            "row_length": ["Row Lenght", 0, 128, 1],
            "tile_width": ["Tile Width", 0, 5, 1]
        }, 
        "danger": 
        {
            "count": ["Quantity", 0, 100, 1],
            "min_life": ["Minimal Duration", 0, 15, 1],
            "max_life": ["Maximal Duration", 0, 27, 1],
            "spread_chance": ["Chance to spread", 0, 100, 1],
            "damage": ["Damage", 0, 20, 1]
        }, 
        "food":
        {
            "count": ["Quantity", 0, 500, 1],
            "min_spread": ["Minimal spread", 0, 30, 1],
            "max_spread": ["Maximal spread", 0, 50, 1],
            "spread_chance": ["Chance to spread", 0, 2, 1],
            "lifetime_bonus": ["Nutrition value", 0, 50, 1]
        }
    }, 
    "population":
    {
        "organisms":
        {
            "start_life": ["TIME TO LIVE", 0, 200, 1],
            "eyes_size": ["Field of view", 0, 3, 1],
        }, 
        "mutations":
        {
            "probability": ["Probability", 0, 0.05, 0.01],
            "max_difference": ["Maximal Mutation", 0, 0.25, 0.01]
        }, 
        "interactions":
        {
            "border_damage": ["Border Damage", 0, 100, 1],
            "move_bonus": ["Points for moving", 0, 0.01, 0.01],
            "survivor_bonus": ["Points for surviving", 0, 500, 1],
        }, 
        "population_size": ["Population Size", 0, 300, 1]
    }, 
    "generation_counter": ["Generations", 0, 0, 1],
    "generation_duration": ["Generation duration", 0, 350, 1],
    "tickspeed": ["Tickspeed", 0, 180, 1]
}
