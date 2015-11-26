from neuron import Neuron
from timing_controller import TimingController


def make_connections(from_neurons, to_neurons):
    #make a connection to each to_neuron from each from_neuron
    connections = []
    for from_neuron in from_neurons:
        for to_neuron in to_neurons:
            if from_neuron != to_neuron:
                connections.append(from_neuron.connect(to_neuron))
    return connections


def make_neurons(number, controller):
    n_list = []
    for n in range(0, number):
        n_list.append(Neuron(controller))
    return n_list


class Cluster(object):
    def __init__(self, in_n, out_n, cluster):
        self.input_neurons = make_neurons(in_n, self)
        self.output_neurons = make_neurons(out_n, self)
        self.cluster_neurons = make_neurons(cluster, self)

        #now go through and connect them all...
        make_connections(self.input_neurons, self.cluster_neurons)
        make_connections(self.cluster_neurons, self.cluster_neurons)
        make_connections(self.cluster_neurons, self.output_neurons)


class FeedForward(object):
    inputs = []

    def __init__(self, in_n, out_n, hidden):
        self.result = {}
        self.answers = None
        self.timing_controller = TimingController()

        self.input_neurons = make_neurons(in_n, self)
        self.output_neurons = make_neurons(out_n, self)
        self.hidden_neurons = make_neurons(hidden, self)

        self.timing_controller.set_neurons(self.input_neurons + self.output_neurons + self.hidden_neurons)

        #now go through and connect them all...
        connections = make_connections(self.input_neurons, self.hidden_neurons)
        connections = connections + make_connections(self.hidden_neurons, self.output_neurons)
        connections = connections + make_connections(self.output_neurons, [self, ])

        self.timing_controller.set_connections(connections)

        self.done_processing = False

    def process_input(self, i, a):
        #inputs should be the same dimension as our input_neuron array
        if len(i) != len(self.input_neurons):
            raise IndexError("Input does not have the same number of items as the net has input neurons.")

        if len(a) != len(self.output_neurons):
            raise IndexError("Answer does not have the same number of items as the net has output neurons.")

        # print "INPUTS %s, ANSWERS %s" % (i, a)
        #Set our answers
        self.answers = a

        #proecess our inputs
        for x in range(len(i)):
            value = i[x]
            # print "VALUE %s" % value
            neuron = self.input_neurons[x]
            neuron.receive_signal(signal=value, sender=self)

        self.timing_controller.start()

    def receive_signal(self, sender=None, signal=None):
        #on output, the output neuron should call this with the result.
        self.result[sender] = signal

        if len(self.result) == len(self.answers):
            print 'Guesses for answers', self.answers
            for x in range(len(self.output_neurons)):
                neuron = self.output_neurons[x]
                answer = self.answers[x]
                error = answer - self.result[neuron]

                print 'Answer was: %s, correct answer was: %s, error was: %s' % (self.result[neuron], answer, error)

                neuron.learn(error)

            #we're done, break the while loop in process_input
            self.timing_controller.stop()

            self.result = {}
