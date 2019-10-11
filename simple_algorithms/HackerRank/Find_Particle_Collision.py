#
# Given an array of integers representing speeds of imaginary particles,  
# find the particles which will 'collide' with position n as given.
# Collision will not affect the current speed or direction of the moving particle.
#
# Examples are given below
#

def collision(speed, pos):
    # Here we assume there are no negative numbers
    # start from pos, iterate backwards
    counter = speed[pos]

    collisions = 0

    for i in range(pos - 1, -1, -1):
        counter += 1
        # also add if any number if greater than, since will overtake eventually
        if speed[i] >= counter or speed[i] > speed[pos]:
            collisions += 1
        
    
    # start from pos, iterate forwards to determine if it will overtake any
    counter = speed[pos]

    for i in range(pos + 1, len(speed), 1):
        counter -= 1
        # also have to add if smaller since will overtake eventually
        if speed[i] <= counter or speed[i] < speed[pos]:
            collisions += 1

    return collisions

print(collision([10, 8, 3, 6, 2, 2, 4, 8, 1, 6], 7))  # should return 3