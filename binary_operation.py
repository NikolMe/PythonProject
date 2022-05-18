import re
from unittest import result


def inverse(a):
    for i in range(len(a)):
        if a[i]: a[i] = 0
        else: a[i] = 1
    return a


def and_operation(a, b):
    result = []
    for i in range(len(a)):
        result.append((a[i] and b[i]))
    return result


def or_operatoin(a, b):
    result = []
    for i in range(len(a)):
        result.append((a[i] or b[i]))
    return result


def implication(a, b):
    result = []
    for i in range(len(a)):
        if a[i] == 1 and b[i] == 0: result.append(0)
        else: result.append(1)
    return result


def equal(a, b):
    result = []
    for i in range(len(a)):
        result.append((a[i] == b[i]))
    return result


def Jeg_op(a, b):
    result = []
    for i in range(len(a)):
        if a[i] != b[i]: result.append(1)
        else: result.append(0)
    return result


def shef_oper(a, b):
    result = []
    for i in range(len(a)):
        if a[i] and b[i] == 1: result.append(0)
        else: result.append(1)
    return result


def pir_oper(a, b):
    result = []
    for i in range(len(a)):
        if a[i] and b[i] == 0: result.append(1)
        else: result.append(0)
    return result

