{
    "world": 
    {
        "size": 
        {
            "column_length": ["Column Length", 128], 
            "row_length": ["Row Lenght", 128],
            "tile_width": ["Tile Width", 5]
        }, 
        "danger": 
        {
            "count": ["Quantity", 100],
            "min_life": ["Minimal Duration", 15],
            "max_life": ["Maximal Duration", 27],
            "spread_chance": ["Chance to spread", 100],
            "damage": ["Damage", 20]
        }, 
        "food":
        {
            "count": ["Quantity", 500],
            "min_spread": ["Minimal spread", 30],
            "max_spread": ["Maximal spread", 50],
            "spread_chance": ["Chance to spread", 2],
            "lifetime_bonus": ["Nutrition value", 50]
        }
    }, 
    "population":
    {
        "organisms":
        {
            "start_life": ["TIME TO LIVE", 200],
            "eyes_size": ["Field of view", 3],
        }, 
        "mutations":
        {
            "probability": ["Probability", 0.05],
            "max_difference": ["Maximal Mutation", 0.25]
        }, 
        "interactions":
        {
            "border_damage": ["Border Damage", 100],
            "move_bonus": ["Points for moving", 0.01],
            "survivor_bonus": ["Points for surviving", 500],
        }, 
        "population_size": ["Population Size", 300]
    }, 
    "generation_counter": ["Generations", 0],
    "generation_duration": ["Generation duration", 350],
    "tickspeed": ["tickspeed", 180]
}
