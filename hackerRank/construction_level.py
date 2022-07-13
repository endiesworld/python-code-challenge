#  Count the occuence of each block(Frewuency of all other blocks)
#  The block with the highest occurrence( mode block) becomes the reference block
#  Run through your blocks subtracting each block from your refefrence block, and store the modulus of the result in an array.
# The sum of the above array is the numbers of step you have to take.

from operator import mod


def foundation(ground):
    block_count = {}
    levels = 0
    for square in ground:
        if square in block_count:
            block_count[square] = block_count[square] + 1
        else:
            block_count[square] = 1
    highest_freq = max(block_count.values())

    for square in ground:
        levels += abs(square - highest_freq)

    return levels


print(foundation([1, 3, 2, 2]))
