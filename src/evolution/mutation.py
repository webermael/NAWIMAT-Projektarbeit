import random
def mutation(inputs, value):
    if random.random() <= inputs["chance"]:
        return value + random.uniform(inputs["max_difference"], -inputs["max_difference"])
    else:
        return value