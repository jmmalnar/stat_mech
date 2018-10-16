import random

# Estimate the value of PI using a Markov chain Monte Carlo simulation

# Start in the upper corner at (1, 1)
x, y = 1.0, 1.0

# delta is the maximum displacement
delta = 0.1
n_trials = 4000
n_hits = 0

for i in range(n_trials):
    # Starting at the initial position, displace in x and y by a random number within -delta and delta
    del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)

    # if the new location is inside the "box", then save it as the new location,
    # else try again from the previous location
    if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
        x, y = x + del_x, y + del_y

    # If the new location is within a radius of 1, mark it as a hit
    if x**2 + y**2 < 1.0:
        n_hits += 1

print(4.0 * n_hits / float(n_trials))