"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. Defaults to the six sided dice.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    result=[]
    have_one=False
    for i in range(num_rolls):
        a=dice()
        result.append(a)
        if(a==1):
            have_one=True
    if have_one:
        return 1
    return sum(result)
    # END PROBLEM 1

def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    num,last=opponent_score//10,opponent_score%10
    num=num%10
    last=player_score%10
    return max(1,3*abs(num-last))
    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls==0:
        return boar_brawl(player_score,opponent_score)
    return roll_dice(num_rolls,dice=dice)
    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score

def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    result=[]
    for i in range(1,n+1):
        if n%i==0:
            result.append(i)
    return len(result)
    # END PROBLEM 4

def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    temp=num_factors(score)
    if temp==3  or temp == 4:
        answer=score+1
        while(True):
            if(is_prime(answer)):
                return answer
            answer+=1
    return score
    # END PROBLEM 4

def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    score=simple_update(num_rolls,player_score,opponent_score,dice)
    return sus_points(score)
    # END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while(score0 <goal and score1<goal):
        if who==0:
            score=score0
            oppo=score1
            strategy=strategy0
        if who==1:
            score=score1
            oppo=score0
            strategy=strategy1
        num=strategy(score,oppo)
        score=update(num,score,oppo,dice)
        if who==0:
            score0=score
        else: score1=score
        who=1-who
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    def f(a,b):
        return n
    return f
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    answer=[]
    for i in range(goal):
        for j in range(goal):
            answer.append(strategy(i,j))
    if(len(set(answer))==1):
        return True
    return False
    # END PROBLEM 7


def make_averaged(original_function, times_called=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TIMES_CALLED times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def result(*args):
        answer=0
        for i in range(times_called):
            answer+=original_function(*args)
        return answer/times_called
    return result
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, times_called=1000):
    """Return the number of dice (1 to 10) that gives the maximum average score for a turn.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    answer={}
    for i,j in enumerate(range(1,11)):
        answer[i+1]=make_averaged(roll_dice,times_called=times_called)(j,dice)
    return max(answer,key=lambda x:answer[x])
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6))) # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('boar_strategy win rate:', average_win_rate(boar_strategy))
    print('sus_strategy win rate:', average_win_rate(sus_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"



def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.
    """
    # BEGIN PROBLEM 10
    if boar_brawl(score,opponent_score)>=threshold:
        return 0
    return num_rolls
    # END PROBLEM 10


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11
    if sus_update(0,score,opponent_score)-score>=threshold:
        return 0
    return num_rolls
    # END PROBLEM 11
import math
DICE_DISTRIBUTIONS = {}

for j in range(1, 11):
    prob_map = {}
    # j 个 5 面骰子 (2,3,4,5,6) 的和的范围：最小 2*j，最大 6*j
    for k in range(2*j, 6*j + 1):
        N = 0
        # 容斥原理计算排列数
        # limit 是容斥项的上限
        limit = (k - 2*j) // 5 + 1
        for n in range(limit):
            # 使用 math.comb 替代 scipy，确保标准库兼容性
            term = (-1)**n * math.comb(j, n) * math.comb(k - j - 5*n - 1, j - 1)
            N += term
        prob_map[k] = N / (5**j)
    DICE_DISTRIBUTIONS[j] = prob_map

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    #基本做到了0.7以上的的胜率,大都强于sus_strategy策略2个点
    if sus_points(score+boar_brawl(score,opponent_score))>=GOAL:
        return 0
    answer={}
    answer[0]=sus_points(score+boar_brawl(score,opponent_score))-score
    err=(score-opponent_score)/GOAL/2
    def E(score,k):
        return sus_points(score+k)-score
    # for i,j in enumerate(range(1,11)):
    #     value_and_prob_j={}
    #     for k in range(2*j,6*j+1):
    #         N=0
    #         for n in range((k-2*j)//5+1):
    #             N+=(-1)**n*scipy.special.comb(j,n)*scipy.special.comb(k-j-5*n-1,j-1)
    #         value_and_prob_j[k]=N/(5**j)
    #     E_other=0
    #     E_other_square=0
    #     for q in value_and_prob_j:
    #         E_other+=value_and_prob_j[q]*E(score,q)
    #         E_other_square+=value_and_prob_j[q]*E(score,q)**2
    #     p1=(5/6)**j
    #     p2=1-(5/6)**j
    #     Expectation=p1*E_other+p2*E(score,1)
    #     answer[i+1]=Expectation-err*math.sqrt((p1*E_other_square+p2*E(score,1)**2)-Expectation**2)
    # return max(answer,key=lambda x:answer[x])
    def E_gain(current_score, dice_sum):
        return sus_points(current_score + dice_sum) - current_score
    for j in range(1, 11):
        value_and_prob_j = DICE_DISTRIBUTIONS[j]
        E_other, E_other_square= 0 ,0
        for k_sum, prob in value_and_prob_j.items():
            gain = E_gain(score, k_sum)
            E_other += prob * gain
            E_other_square += prob * (gain ** 2)
        p1 = (5/6)**j        
        p2 = 1 - p1          
        gain_pig_out = E_gain(score, 1)
        Expectation = p1 * E_other + p2 * gain_pig_out
        Total_Second_Moment = p1 * E_other_square + p2 * (gain_pig_out ** 2)
        variance = Total_Second_Moment - Expectation**2
        if variance < 0: variance = 0
        std_dev = math.sqrt(variance)
        answer[j] = Expectation - err * std_dev
    return max(answer, key=lambda x: answer[x])
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()