from neuron import Neuron


def make_connections(from_neurons, to_neurons):
        #make a connection to each to_neuron from each from_neuron
        for from_neuron in from_neurons:
            for to_neuron in to_neurons:
                if from_neuron != to_neuron:
                    from_neuron.connect(to_neuron)


def make_neurons(number):
    n_list = []
    for n in range(0, number):
        n_list.append(Neuron())
    return n_list


class Cluster(object):
    def __init__(self, in_n, out_n, cluster):
        self.input_neurons = make_neurons(in_n)
        self.output_neurons = make_neurons(out_n)
        self.cluster_neurons = make_neurons(cluster)

        #now go through and connect them all...
        make_connections(self.input_neurons, self.cluster_neurons)
        make_connections(self.cluster_neurons, self.cluster_neurons)
        make_connections(self.cluster_neurons, self.output_neurons)


class FeedForward(object):
    def __init__(self, in_n, out_n, hidden):
        self.input_neurons = make_neurons(in_n)
        self.output_neurons = make_neurons(out_n)
        self.hidden_neurons = make_neurons(hidden)

        #now go through and connect them all...
        make_connections(self.input_neurons, self.hidden_neurons)
        make_connections(self.hidden_neurons, self.output_neurons)
