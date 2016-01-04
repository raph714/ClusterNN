#!/usr/bin/env python
from net import FeedForward


def test_ff():
    #basic addition test, make some
    f = FeedForward(2, 3, 5)
    inputs = [[1, 2], [1, 2]]
    answers = [[0, 1, 1], [0, 1, 1]]

    #do this a couple times so we can make sure the outputs match for the same set of data.
    x = 0
    while x < 100:
        x += 1
        for i in range(len(inputs)):
            f.process_input(inputs[i], answers[i])

        print '\n\n'


if __name__ == '__main__':
    test_ff()
