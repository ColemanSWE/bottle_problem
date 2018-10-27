from fractions import gcd

"""
You have two unmarked bottles that can hold 3 liters and 5 liters respectively, and a bathtub with unlimited water.
You are allowed to either fill a bottle, empty a bottle or pour one bottle into the other until either the source bottle
is empty or the target bottle is full.

- how can 1 liter be measured?
- how can 4 liters be measured?

Implement a solution that would solve this problem and find the minimum amount of steps required to measure the desired amount of water (1 and 4 liters).
Note that the program should find the shortest solution given only the information above, i.e. the volume of the unmarked bottles and the desired target amount.

Provide the source code (including unit tests) and if necessary, a description of how to execute the code.
"""

#########################################################################################################################################################

"""
So after attempting OOP solutions involving instances of a bottle class with attributes for volume and storing their
contained liquid, I realized I was just trying to be too fancy and that simple algorithmic principles could be applied.
And I've usually found that creating your idea the simplest way you know how and then refining for speed/efficiency after
is usually more effective. (Motto I try to keep in mind: KISS! = "Keep it simple, stupid!")

-----------------------------------------------------------------------------------------------------------------

This problem can be simplified mathematically as such:

for bottle1 > bottle2 > 0
where bottle1 and bottle2 are relatively prime (gcd(bottle1, bottle2) % target == 0)
and target < bottle1:

bottle1(x) + bottle2(y) = target

And this is for positive x or y representing filling the bottle and negative x or y
representing emptying the bottles.

--------------------------------------------------------------------------------------------------------------------

And I've found there are 2 ways to solve this problem:

Solution 1 (Always transfer from bottle1 to bottle2):
-Fill bottle1 and empty it into bottle2.
-When bottle1 becomes empty fill it.
-When bottle2 becomes full empty it.
-Repeat steps 1,2,3 until either bottle1 or bottle2 contains the target amount.



Solution 2 (Always transfer from bottle2 to bottle1):
-Fill bottle2 and empty it into bottle1.
-When bottle2 becomes empty fill it.
-When bottle1 becomes full empty it.
-Repeat steps 1,2,3 until either bottle1 or bottle2 contains the target amount.

-------------------------------------------------------------------------------------------------------------------

Now all that's left is to code both solutions, comparing the amount of steps taken for each given the bottle sizes and target,
and return the solution that solves it quickest as well the amount of steps needed.

Edit: Added exceptions (useful for keeping our parameters where we want them).
"""

class InvalidTargetError(Exception):
    pass

class InvalidGcdRatioError(Exception):
    pass

# Implementing Solution 1 using a while loop that terminates when one of the bottles reaches the target and
# logic simulating transfer of liters of liquid between bottles. Solution 2 is implemented in the comparison just
# flipping the variables
def big_to_small(target, bottle1_vol, bottle2_vol):
    step = 1
    bottle1 = bottle1_vol
    bottle2 = 0

    if target % gcd(bottle1_vol, bottle2_vol) != 0:
        raise InvalidGcdRatioError

    if target > bottle1_vol and target > bottle2_vol:
        raise InvalidTargetError

    while bottle1 != target and bottle2 != target:

        # Max amount that can be poured
        pour = min(bottle1, bottle2_vol - bottle2)

        # Simulating the pouring of the amount in the last step
        bottle2 += pour
        if bottle1 - pour < 0:
            bottle1 = 0
        else:
            bottle1 -= pour

        #Incrementing step count
        step += 1

        # Go no further if the target is reached
        if bottle1 == target or bottle2 == target:
            return step

        # Fill if big bottle is empty
        if bottle1 == 0:
            bottle1 = bottle1_vol
            step += 1

        # Pour if the small bottle is full.
        if bottle2 == bottle2_vol:
            bottle2 = 0
            step += 1

    return step


def comparison(target, bottle1_vol, bottle2_vol):
    # Using variables to store the steps for both solutions to compare.
    solution_one = big_to_small(target, bottle1_vol, bottle2_vol)
    solution_two = big_to_small(target, bottle2_vol, bottle1_vol) # Using the pouring function from earlier, just swapping which is being poured from.

    if solution_one < solution_two:
        print "Solution 1 is quicker and it takes {} steps.".format(solution_one)
        return solution_one

    if solution_two < solution_one:
        print "Solution 2 is quicker and it takes {} steps.".format(solution_two)
        return solution_two

    if solution_one == solution_two:
        return "They are equal and it takes {} steps".format(solution_two)