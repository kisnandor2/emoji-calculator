#!/usr/bin/python
# -*- coding: utf-8 -*-
# The below code is from https://github.com/lucafmarques/Expression-Calculator-Python/blob/master/exp_calc.py
# since I was lazy to write it
# did a cleanup on the code as well
# the source code is under GPL3 licences which means this has to be GPL3 as well
# also translated the portuguese error messages

import operator
import math
from re import sub


def calculate(string):
    ops = {  # lambda x, y : x + y,
             # lambda x, y: x - y,
             # lambda x, y: x * y,
             # lambda x, y: x / y,
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        }
    stack = []
    if not string:
        return 0
    for i in string:
        try:
            stack.append(float(i))
        except ValueError:
            if stack:
                last = float(stack.pop())
                try:
                    try:
                        stack.append(ops[i](float(stack.pop()), last))
                    except ValueError:
                        raise ValueError('{} No negative numbers.'.format(i))
                    except IndexError:

                      # stack.append("{} No negative numbers.".format(i))

                        raise IndexError('Operators missing {}.'.format(i))
                except ZeroDivisionError:

                      # stack.append("Operators missing {}.".format(i))

                    pass
    if not stack:
        raise ValueError('Can not compute the expression')
    return stack[-1]


def parser(string):
    string = sub(r'([-+*/])(?=)', r' \1 ', string)
    ops = {
        '+': {'prec': 2, 'assoc': 'L'},
        '-': {'prec': 2, 'assoc': 'L'},
        '*': {'prec': 3, 'assoc': 'L'},
        '/': {'prec': 3, 'assoc': 'L'},
        }
    (stack, output) = ([], [])
    for i in string.split():
        try:
            float(i)
            output.append(i)
        except ValueError:
            while stack:
                last = stack[-1]
                if ops[i]['assoc'] == 'L' and ops[i]['prec'] \
                    <= ops[last]['prec'] or ops[i]['assoc'] == 'R' \
                    and ops[i]['prec'] < ops[last]['prec']:
                    output.append(stack.pop())
                else:
                    break
            stack.append(i)
    while stack:
        output.append(stack.pop())
    if output:
        return (output, 0)
    return ('Could not parse the input expression', 1)
