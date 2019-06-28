stages = iter(['alpha','beta','gamma'])

try:
    next(stages)
    next(stages)
    next(stages)
    next(stages)
except StopIteration as ex:
    err_msg = 'Ran out of iterations'

