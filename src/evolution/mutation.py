import random
def mutation(inputs, value):
    # has a chance to slightly change the input value
    if random.random() <= inputs["probability"]:
        return value + random.uniform(inputs["max_difference"], -inputs["max_difference"])
    else:
        return value