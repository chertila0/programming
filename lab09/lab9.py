import time

def rand_num(min_val, max_val):
    seed = int(time.time() * 1000)
    random_num = (seed % (max_val - min_val + 1)) + min_val
    return random_num

mins = 20
maxs = 70 
print(rand_num(mins, maxs))