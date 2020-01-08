#!/usr/bin/python3

import math
from math import sqrt
import sys

values = []
differences = []
errors = []


def moyenne(a, period):
    moy = 0
    i = 0
    while (i < period):
        if (differences[a + i] > 0):
            moy = moy + differences[a + i]
        i = i + 1
    moy = moy / period
    return (moy)

def moyenne2(a, period):
    moy = 0
    i = 0
    while (i < period):
        moy = moy + values[a + i]
        i = i + 1
    moy = moy / period
    return (moy)

def ratio(period):
    l = len(values)
    act = values[l - 1]
    old = values[l - 1 - period]
    rate = 100
    if (old != 0):
        rate = (act - old) / old
    return (round(rate, 2) * 100)

def deviation(a, period):
    moy = 0
    i = 0
    while (i < period):
        moy = moy + values[a + i]
        i = i + 1
    moy = moy / period
    i = 0
    var = 0
    while i < period:
        var += pow(values[i + a] - moy, 2)
        i = i + 1
    var = var / period
    return (sqrt(var))

def sortSecond(val):
    return val[1]

def sortThird(val):
    return val[2]

def find_abberation(a, period, s):
    i = 0
    m = moyenne2(a, period)

    value = values[a + period - 1]
    if (value >= m + s):
        if (m + 2 * s == 0):
            percent = 3000000
        else:
            percent = value / (m + 2 * s) * 100
        errors.append([value, percent, 1])
    elif (value <= m - s):
        if (value == 0):
            percent = 3000000
        else:
            percent = (m - 2 * s) / value * 100
        errors.append([value, percent, 1])

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit(84)
    arg1 = sys.argv[1]
    if (arg1 == "-h"):
        print("SYNOPSIS\n    ./groundhog period\nDESCRIPTION\n    period        the number of days defining a period")
        exit(0)
    try:
        period = int(sys.argv[1])
    except:
        sys.exit(84)
    if (period <= 0):
        sys.exit(84)
    string = input()
    nb_switch = 0
    old_r = 0
    switch = 0
    while string != "STOP":
        try:
            value = float(string)
        except:
            sys.exit(84)
        if (len(values) > 0):
            diff = value - values[len(values) - 1]
            differences.append(diff)
        values.append(value)
        if (len(differences) >= period):
            g = moyenne(len(differences) - period, period)
            print("g=%.2f" % g, end='')
        else:
            print("g=nan", end='')
        print("\t\t", end='')
        if (len(values) > period):
            r = ratio(period)
            print("r=%.0f%%" % r, end='')
            if (r > 0 and old_r < 0):
                switch = 1
            elif (r < 0 and old_r > 0):
                switch = 1
            else:
                switch = 0
            old_r = r
        else:
            print("r=nan%", end='')
        print("\t\t", end='')
        if (len(values) >= period):
            s = deviation(len(values) - period, period)
            print("s=%.2f" % s, end='')
            if (len(values) > period):
                find_abberation(len(values) - period, period, round(s, 2))
        else:
            print("s=nan", end='')
        if (switch == 1):
            print("\t\ta switch occurs", end='')
            nb_switch += 1
        print("")
        try:
            string = input()
        except:
            sys.exit(84)

    # print("STOP")
    try:
        print("Global tendency switched %d times" % nb_switch)
        errors.sort(key = sortThird, reverse = True)
        errors2 = []
        i = 0
        while (errors[i][2] >= 2 and i < 5):
            errors2.append(errors[i])
            i = i + 1
            errors = errors[i:]
        errors2.sort(key = sortSecond, reverse = True)
        errors.sort(key = sortSecond, reverse = True)
        j = 0
        while (i < 5):
            errors2.append(errors[j])
            j = j + 1
            i = i + 1
        i = 0
        print("5 weirdest values are [", end='')
        while (i < 5):
            print(errors2[i][0], end='')
            if (i != 4):
                print(", ", end='')
            i = i + 1
        print("]")
    except:
        sys.exit(84)
    sys.exit(0)
