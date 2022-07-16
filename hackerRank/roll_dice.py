
calls = 0


def dice_rolls(dice):
    rolled_dice = []
    return _dice_rolls(dice, rolled_dice)


def _dice_rolls(dice, rolled_dice):
    if dice == 0:
        return (print(rolled_dice))
    # my_number = dice

    for data in range(1, 7):
        rolled_dice.append(data)
        _dice_rolls(dice-1, rolled_dice)
        rolled_dice.pop()


class Rolling_Dice:
    calls = 0

    def __init__(self) -> None:
        pass

    def dice_rolls_sum(self, dice, sum_):
        rolled_dice = []
        return self._dice_rolls_sum(dice, sum_, rolled_dice)

    def _dice_rolls_sum(self, dice, sum_, rolled_dice):
        self.calls += 1
        if sum(rolled_dice) == sum_:
            print(rolled_dice)
        if dice == 0:
            return None

        for data in range(1, 7):
            if (sum(rolled_dice) + data) <= sum_:
                rolled_dice.append(data)
                self._dice_rolls_sum(dice-1, sum_, rolled_dice)
                rolled_dice.pop()


class Rolling_Dice_2:
    calls = 0

    def __init__(self) -> None:
        pass

    def dice_rolls_sum(self, dice, sum_):
        rolled_dice = []
        return self._dice_rolls_sum(dice, sum_, rolled_dice)

    def _dice_rolls_sum(self, dice, sum_, rolled_dice):
        self.calls += 1
        if sum(rolled_dice) == sum_:
            print(rolled_dice)
        if dice == 0:
            return None

        for data in range(1, 7):
            rolled_dice.append(data)
            self._dice_rolls_sum(dice-1, sum_, rolled_dice)
            rolled_dice.pop()

# print(dice_rolls(3, 5))


dice = Rolling_Dice()
print(dice.dice_rolls_sum(3, 5))
print(f'{dice.calls} numbers of calls')
dice_2 = Rolling_Dice_2()
print(dice_2.dice_rolls_sum(3, 5))
print(f'{dice_2.calls} numbers of calls')
