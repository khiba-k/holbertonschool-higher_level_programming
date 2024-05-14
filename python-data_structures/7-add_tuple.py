#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        sum1, sum2 = tuple_a[0] + tuple_b[0], 0 + tuple_b[1]
    elif len(tuple_b) == 1:
        sum1, sum2 = tuple_a[0] + tuple_b[0], tuple_a[1] + 0
    else:
        sum1, sum2 = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]

    new_tuple = (sum1, sum2)

    return new_tuple