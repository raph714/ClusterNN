#!/usr/bin/env python
from net import FeedForward


def test_ff():
    #basic addition test, make some
    f = FeedForward(2, 1, 1)
    inputs = [[.5, .4], [.3, .2], [.1, .2], [2, 5]]
    answers = [[.9, ], [.5, ], [.3, ], [7, ]]

    #do this a couple times so we can make sure the outputs match for the same set of data.
    for i in range(len(inputs)):
        f.process_input(inputs[i], answers[i])

    print '\n\n'

    for i in range(len(inputs)):
        f.process_input(inputs[i], answers[i])

    print '\n\n'

    for i in range(len(inputs)):
        f.process_input(inputs[i], answers[i])


if __name__ == '__main__':
    test_ff()
