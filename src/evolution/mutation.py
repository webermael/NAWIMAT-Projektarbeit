import random
def mutation(config, value):
    if random.random() <= config.mutation_rate:
        return value + random.uniform(config.mutation_max_difference, -config.mutation_max_difference)
    else:
        return value