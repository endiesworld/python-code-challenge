# #  Count the occurrence of each block(Frewuency of all other blocks)
# #  The block with the highest occurrence( mode block) becomes the reference block
# #  Run through your blocks subtracting each block from your refefrence block, and store the modulus of the result in an array.
# # The sum of the above array is the numbers of step you have to take.

# from operator import mod


# def foundation(ground):

#     block_count = {}  # Used to store blocks count
#     levels = 0  # Used as the number os works to be done

#     # Store the occurrence of block count
#     for square in ground:
#         # Check if block has been identified, if yes increase count
#         if square in block_count:
#             block_count[square] = block_count[square] + 1

#         # if no, start block count
#         else:
#             block_count[square] = 1

#     # Get the highest amount of block count
#     highest_freq = max(block_count.values())

#     # keys = block_count.keys()

#     for key, value in block_count.items():
#         if value == highest_freq:
#             ref = int(key)
#     # Substract each block from the maximum count, find the absolute value and add to works to be done

#     for square in ground:
#         levels += abs(square - ref)

#     return levels


# print(foundation([1, 3, 2, 2]))
def get_result(rocket_pos, rocket_speed):
    # Write your code here...
    max_speed = max(rocket_speed)
    position = rocket_pos
    steps = 15 // max_speed
    new_speed = rocket_speed
    for i in range(1, steps):
        for index, data in enumerate(position):
            position[index] = data + new_speed[index]

    block_count = {}  # Used to store blocks count

    # Store the occurrence of block count
    for square in position:
        # Check if block has been identified, if yes increase count
        if square in block_count:
            block_count[square] = block_count[square] + 1

        # if no, start block count
        else:
            block_count[square] = 1
    return len(block_count.keys())


rocket_pos = [3, 11]


rocket_speed = [5, 1]

# rocket_pos = [2, 3]
# rocket_speed = [1, 2]
print(get_result(rocket_pos, rocket_speed))


"""
Elon Musk presented a new space project - he launched a large number of rockets into the sky. There is an array rocket_pos, where rocket_pos[i] - the height of  i-th rocket and  rocket_speed array, where rocket_speed[i] - the speed of i-th rocket (the value of movement per time unit).

When the rockets reach the same height at some step, they unite into one rocket and their speed adds up.

Determine how many rockets will remain in the end.

Input:

rocket_pos - the initial position of each rocket (Integer[]), 0<length(rocket_pos)<=10, 0<=rocket_pos[i]<=1000
rocket_speed - the speed of each rocket (Integer[]), 0<length(rocket_speed)<=10, 0<=rocket_speed[i]<=15
Output:

Integer - the number of rockets that will remain in the end
Example 1:
"""
