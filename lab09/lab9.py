import time

def rand_num(min_val, max_val):
    seed = int(time.time() * 1000)
    random_num = (seed % (max_val - min_val + 1)) + min_val
    return random_num