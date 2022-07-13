#  Count the occurrence of each block(Frewuency of all other blocks)
#  The block with the highest occurrence( mode block) becomes the reference block
#  Run through your blocks subtracting each block from your refefrence block, and store the modulus of the result in an array.
# The sum of the above array is the numbers of step you have to take.

from operator import mod


def foundation(ground):

    block_count = {}  # Used to store blocks count
    levels = 0  # Used as the number os works to be done

    # Store the occurrence of block count
    for square in ground:
        # Check if block has been identified, if yes increase count
        if square in block_count:
            block_count[square] = block_count[square] + 1

        # if no, start block count
        else:
            block_count[square] = 1

    # Get the highest amount of block count
    highest_freq = max(block_count.values())

    # Substract each block from the maximum count, find the absolute value and add to works to be done
    for square in ground:
        levels += abs(square - highest_freq)

    return levels


print(foundation([1, 3, 2, 2]))
