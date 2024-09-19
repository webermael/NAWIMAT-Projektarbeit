interface_values = {
    "world": 
    {
        "size": 
        {
            "column_length": ["Height", 10, 500, 10], 
            "row_length": ["Width", 10, 500, 10],
            "tile_width": ["Tile size (pixels)", 1, 20, 1]
        }, 
        "danger": 
        {
            "count": ["Amount", 0, 2000, 100],
            "min_life": ["Minimal burning time", 0, 100, 5],
            "max_life": ["Maximal burning time", 0, 200, 5],
            "spread_chance": ["Chance to spread (per tick)", 0, 1, 0.01],
            "damage": ["Damage", 0, 500, 10]
        }, 
        "food":
        {
            "count": ["Amount", 0, 2000, 100],
            "min_spread": ["Minimal time to spread", 0, 100, 5],
            "max_spread": ["Maximal time to spread", 0, 200, 5],
            "lifetime_bonus": ["Nutrition value", 0, 500, 10]
        }
    }, 
    "population":
    {
        "organisms":
        {
            "start_life": ["Time to live", 0, 400, 10],
            "eyes_size": ["Range of vision (in tiles)", 0, 5, 1],
        }, 
        "mutations":
        {
            "probability": ["Probability", 0, 1, 0.01],
            "max_difference": ["Maximal mutation influence", 0, 2, 0.01]
        }, 
        "interactions":
        {
            "border_damage": ["Border damage", 0, 1000, 10],
            "move_bonus": ["Points for moving", 0, 10, 0.1],
            "survivor_bonus": ["Points for surviving", 0, 1000, 100],
        }, 
        "population_size": ["Population Size", 0, 1000, 100]
    },
    "general": 
    {
    "generation_duration": ["Generation duration", 0, 2000, 100],
    "tickspeed": ["Tickspeedcap (0: uncapped)", 0, 180, 30]
    },
}
