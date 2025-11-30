"""Typing test implementation"""

from utils import (
    lower,
    split,
    remove_punctuation,
    lines_from_file,
    count,
    deep_convert_to_tuple,
)
from ucb import main, interact, trace
from datetime import datetime
import random


###########
# Phase 1 #
###########


def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which the SELECT returns True.
    If there are fewer than K such paragraphs, return an empty string.

    Arguments:
        paragraphs: a list of strings representing paragraphs
        select: a function that returns True for paragraphs that meet its criteria
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    answer=list(filter(select,paragraphs))
    return answer[k] if len(list(answer))>k else ''
    # END PROBLEM 1


def about(subject):
    """Return a function that takes in a paragraph and returns whether
    that paragraph contains one of the words in SUBJECT.

    Arguments:
        subject: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in subject]), "subjects should be lowercase."
    # BEGIN PROBLEM 2
    def answer(string_input):
        new=''.join(c for c in string_input if (c.isalpha() or c==' '))
        new=new.lower().split(' ')
        for  i in new:
            for j in subject:
                if i==j:
                    return True
        return False
    return answer
    # END PROBLEM 2


def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    compared to the corresponding words in SOURCE.

    Arguments:
        typed: a string that may contain typos
        source: a model string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    count=0
    if len(source_words)==0 or len(typed_words)==0:
           if len(source_words)==0 and len(typed_words)==0:
            return 100.0
           return 0.0
    for i,j in zip(typed_words,source_words):
        if i==j:
            count+=1
    return round(count/len(typed_words)*100,2)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, "Elapsed time must be positive"
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return round(len(typed)/5/elapsed*60,2)
    # END PROBLEM 4

################
# Phase 4 (EC) #
################


def memo(f):
    """A general memoization decorator."""
    cache = {}

    def memoized(*args):
        immutable_args = deep_convert_to_tuple(args)  # convert *args into a tuple representation
        if immutable_args not in cache:
            result = f(*immutable_args)
            cache[immutable_args] = result
            return result
        return cache[immutable_args]

    return memoized


def memo_diff(diff_function):
    """A memoization function."""
    cache = {}

    def memoized(typed, source, limit):
        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        find=(typed,source)
        if  find in cache:
            if cache[find]>limit:
                return limit+1
            else:
                return cache[find]
        else:
            temp=diff_function(typed,source,limit)
            if temp<=limit:
                cache[find]=temp
            return temp
        # END PROBLEM EC
    return memoized


###########
# Phase 2 #
###########


def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD based on DIFF_FUNCTION. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    difference is greater than LIMIT, return TYPED_WORD instead.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if typed_word in word_list:
        return typed_word
    min_diff=min(word_list,key=lambda x:diff_function(typed_word,x,limit))
    if diff_function(typed_word,min_diff,limit)>limit:
        return typed_word
    return min_diff
    # END PROBLEM 5

# @memo_diff
def furry_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> furry_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> furry_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> furry_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> furry_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> furry_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    if typed=="" or source=="":
        return abs(len(typed)-len(source))
    if limit==-1:
        return 0
    if typed[0]==source[0]:
        return furry_fixes(typed[1:],source[1:],limit=limit)
    else : 
        return 1+furry_fixes(typed[1:],source[1:],limit=limit-1)
    # END PROBLEM 6


def minimum_mewtations(typed, source, limit):
    """A diff function for autocorrect that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if typed=="" or source=="":
        return abs(len(typed)-len(source))
    if abs(len(typed)-len(source))>limit:
        return limit+1
    if limit==-1:
        return 0
    if typed[0]==source[0]:
        return minimum_mewtations(typed[1:],source[1:],limit)
    else:
        return 1+min(minimum_mewtations(typed,source[1:],limit-1),minimum_mewtations(typed[1:],source,limit-1),minimum_mewtations(typed[1:],source[1:],limit-1))

    # if ___________: # Base cases should go here, you may add more base cases as needed.
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END
    # # Recursive cases should go below here
    # if ___________: # Feel free to remove or add additional cases
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END
    # else:
    #     add = ... # Fill in these lines
    #     remove = ...
    #     substitute = ...
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"

    #     # END
    

# Ignore the line below
minimum_mewtations = count(minimum_mewtations)
minimum_mewtations = memo_diff(minimum_mewtations)


layout = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]

coords = {}
for r, row in enumerate(layout):
    for c, char in enumerate(row):
        coords[char] = (r, c)

KEY_DIST = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for c1 in alphabet:
    for c2 in alphabet:
        if c1 == c2:
            KEY_DIST[(c1, c2)] = 0
            continue
        r1, col1 = coords[c1]
        r2, col2 = coords[c2]
        dist = max(abs(r1 - r2), abs(col1 - col2))  
        if dist == 1:
            cost = 2  # 相邻
        elif dist == 2:
            cost = 6  
        else:
            cost = 8 
        KEY_DIST[(c1, c2)] = cost

#大概1750 wpm速度 correct/incorrect在3以上
@memo_diff
def final_diff(typed, source, limit):
    while len(typed) >=2 and len(source) >=2 and typed[0] == source[0]:
        typed = typed[1:]
        source = source[1:]

    if typed == "" or source == "":
        return 4*abs(len(typed) - len(source))
    if 4*abs(len(typed) - len(source)) > limit:
        return limit + 1
    if limit < 0: 
        return 1
    if typed == source:
        return 0
    if len(typed) >= 2 and len(source) >= 2 and typed[0] == source[1] and typed[1] == source[0]:
        return 3 + final_diff(typed[2:], source[2:], limit - 3)

    if typed[0] == source[0]:
        return final_diff(typed[1:], source[1:], limit)
    
    else:
        t_char = typed[0].lower()
        s_char = source[0].lower()
        sub_cost = KEY_DIST.get((t_char, s_char), 4)
        
        sub_result = 1000
        if sub_cost <= limit:
            sub_result = sub_cost + final_diff(typed[1:], source[1:], limit - sub_cost)
        add = 4 + final_diff(typed, source[1:], limit - 4)
        remove = 4 + final_diff(typed[1:], source, limit - 4)
        
        return min(add, remove, sub_result)

FINAL_DIFF_LIMIT = 6*4  # REPLACE THIS WITH YOUR LIMIT

###########
# Phase 3 #
###########


def report_progress(typed, source, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        source: a list of the words in the typing source
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> source = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, source, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], source, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    num=0
    result={}
    for i ,j in zip(typed,source):
        if i==j:
            num+=1
        else:
            break
    result["id"]=user_id
    result["progress"]=num/len(source)
    upload(result)
    return num/len(source)
    # END PROBLEM 8


def time_per_word(words, timestamps_per_player):
    """Return a dictionary {'words': words, 'times': times} where times
    is a list of lists that stores the durations it took each player to type
    each word in words.

    Arguments:
        words: a list of words, in the order they are typed.
        timestamps_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time the
                          player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> result = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> result['words']
    ['collar', 'plush', 'blush', 'repute']
    >>> result['times']
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    tpp = timestamps_per_player  # A shorter name (for convenience)
    # BEGIN PROBLEM 9
    times=[]
    for i in tpp:
        add_item=[k-j for j,k in zip(i[:-1],i[1:])]
        times.append(add_item)
    # END PROBLEM 9
    return {'words': words, 'times': times}


def fastest_words(words_and_times):
    """Return a list of lists indicating which words each player typed fastests.

    Arguments:
        words_and_times: a dictionary {'words': words, 'times': times} where
        words is a list of the words typed and times is a list of lists of times
        spent by each player typing each word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words({'words': ['Just', 'have', 'fun'], 'times': [p0, p1]})
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    check_words_and_times(words_and_times)  # verify that the input is properly formed
    words, times = words_and_times['words'], words_and_times['times']
    player_indices = range(len(times))  # contains an *index* for each player
    word_indices = range(len(words))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    sorted_player=[]
    for i in range(len(times[0])):
        item=[j[i] for j in times]
        sorted_player.append(item.index(min(item)))
    result=[[] for i in player_indices]
    for i,j in zip(words,sorted_player):
        result[j].append(i)
    return result
    # END PROBLEM 10

def check_words_and_times(words_and_times):
    """Check that words_and_times is a {'words': words, 'times': times} dictionary
    in which each element of times is a list of numbers the same length as words.
    """
    assert 'words' in words_and_times and 'times' in words_and_times and len(words_and_times) == 2
    words, times = words_and_times['words'], words_and_times['times']
    assert all([type(w) == str for w in words]), "words should be a list of strings"
    assert all([type(t) == list for t in times]), "times should be a list of lists"
    assert all([isinstance(i, (int, float)) for t in times for i in t]), "times lists should contain numbers"
    assert all([len(t) == len(words) for t in times]), "There should be one word per time."


def get_time(times, player_num, word_index):
    """Return the time it took player_num to type the word at word_index,
    given a list of lists of times returned by time_per_word."""
    num_players = len(times)
    num_words = len(times[0])
    assert word_index < len(times[0]), f"word_index {word_index} outside of 0 to {num_words-1}"
    assert player_num < len(times), f"player_num {player_num} outside of 0 to {num_players-1}"
    return times[player_num][word_index]


enable_multiplayer = True  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file("data/sample_paragraphs.txt")
    random.shuffle(paragraphs)
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print("No more paragraphs about", topics, "are available.")
            return
        print("Type the following paragraph and then press enter/return.")
        print("If you only type part of it, you will be scored only on that part.\n")
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print("Goodbye.")
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print("Words per minute:", wpm(typed, elapsed))
        print("Accuracy:        ", accuracy(typed, source))

        print("\nPress enter/return for the next paragraph or type q to quit.")
        if input().strip() == "q":
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument("topic", help="Topic word", nargs="*")
    parser.add_argument("-t", help="Run typing test", action="store_true")

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)