import re
import collections

def list_to_string(list):
    """Convert a list to its Prolog representation in string form.
    >>> list_to_string([['fe', 1], ['gwyn', 1]])
    '[[fe, 1], [gwyn, 1]]'
    """
    return re.sub(r"'(.*?)'", r'\1', str(list))


def prefs_to_tasks(prefs):
    """Convert a mapping of people->preferences to tasks->preferences.
    Takes a dictionary whose keys are individuals and whose values are
    the individual's task preferences in order. Returns a dictionary
    whose keys are tasks and whose values are a list of
    person/preference pairs, each as its own list. There is no
    guaranteed ordering on the keys, but the value lists are ordered
    according to the same order as the keys in the original
    dictionary.
    >>> prefs = {
    ... 'fe': ['task1', 'task2'], 'wei': ['task3', 'task4'],
    ... 'gwyn': ['task1', 'task3'], 'ting': ['task4', 'task3']
    ... }
    >>> tasks = prefs_to_tasks(prefs)
    >>> tasks['task1']
    [['fe', 1], ['gwyn', 1]]
    >>> tasks['task2']
    [['fe', 2]]
    >>> tasks['task3']
    [['wei', 1], ['gwyn', 2], ['ting', 2]]
    >>> tasks['task4']
    [['wei', 2], ['ting', 1]]
    """
    # A dictionary where the default value for each key is an empty list.
    # https://docs.python.org/3/library/collections.html#collections.defaultdict
    # for more details.
    tasks = collections.defaultdict(list) # use this below
    # replace with your solution
    for person, t in prefs.items():
        for i, task in enumerate(t): 
            if task in tasks:
                tasks[task].append([person, i+1])
            else:
                tasks[task] = [[person, i+1]]

    return tasks

def gen_query(prefs):
    """Generate a query for the given preferences.
    The query is for the match predicate, where the first argument is
    the set of preferences for each task, the second argument is the
    set of people, and the third argument is a variable for the
    result.
    There is no specified whitespace for the output, and there is no
    specified ordering on tasks or people. Possible output for the set
    of preferences in the docstring for prefs_to_tasks():

    match([[task1, [fe, 1], [gwyn, 1]],
           [task2, [fe, 2]],
           [task3, [wei, 1], [gwyn, 2], [ting, 2]],
           [task4, [wei, 2], [ting, 1]]],
          [fe, wei, gwyn, ting], Result).

    >>> prefs = {
    ... 'fe': ['task1', 'task2'], 'wei': ['task3', 'task4'],
    ... 'gwyn': ['task1', 'task3'], 'ting': ['task4', 'task3']
    ... }
    >>> query = gen_query(prefs)
    >>> ''.join(query.split())
    'match([[task1,[fe,1],[gwyn,1]],[task2,[fe,2]],[task3,[wei,1],[gwyn,2],[ting,2]],[task4,[wei,2],[ting,1]]],[fe,wei,gwyn,ting],Result).'
    """
    # replace with your solution

    x = prefs_to_tasks(prefs)

    output = "match("\
        + list_to_string(prefs_to_tasks(prefs))\
        + ","\
        + list_to_string([x[0] for x in (prefs.items())])\
        + ", X)."
    return output