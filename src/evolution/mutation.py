import random
def mutation(config, value):
    if random.random() <= config.mutation_rate:
        return value * random.uniform(config.mutation_min_multiplier, config.mutation_max_multiplier)
    else:
        return value