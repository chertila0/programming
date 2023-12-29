import time

def rand_num(minn, maxx):
    seed = int(time.time() * 1000)
    random_ch = (seed % (maxx - minn + 1)) + minn
    return random_ch

