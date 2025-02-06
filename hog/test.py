from dice import six_sided, make_test_dice
from ucb import main, trace, interact

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    sum=0
    score=0
    flag=0
    for i in range(1,num_rolls+1):
        score=dice()
        sum+=score
        if score==1:
            flag=1
    if flag==1:
        return 1
    else:
        return sum

    # END PROBLEM 1



def make_averaged(original_function, samples_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called SAMPLES_COUNT times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def simulator(*arg):
        result=0
        for i in range(0,samples_count):
            result+=original_function(*arg)
        return result/samples_count
    return simulator


    # END PROBLEM 8



def max_scoring_num_rolls(dice=six_sided, samples_count=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of SAMPLES_COUNT times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times_changer=make_averaged(roll_dice,samples_count)
    result1,score=0,0
    for i in range(1,11):
        a=times_changer(i,dice)
        if a>score:
            score=a
            result1=i
        print(a,score,result1)
    return result1
   
    # END PROBLEM 9




max_scoring_num_rolls(dice=six_sided, samples_count=1000)