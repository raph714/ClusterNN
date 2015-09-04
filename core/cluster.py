from neuron import Neuron


class Cluster(object):
    input_neurons = []
    output_neurons = []

    cluster_neurons = []

    def __init__(self, in_n=1, out_n=1, cluster=5):
        #make all our input, output and cluster neurons
        for n in range(0, in_n):
            self.input_neurons.append(Neuron())

        for n in range(0, out_n):
            self.output_neurons.append(Neuron())

        for n in range(0, cluster):
            self.cluster_neurons.append(Neuron())

        #now go through and connect them all...
        self.make_connections(self.input_neurons, self.cluster_neurons)
        self.make_connections(self.cluster_neurons, self.cluster_neurons)
        self.make_connections(self.cluster_neurons, self.output_neurons)

    def make_connections(self, from_neurons, to_neurons):
        #make a connection to each to_neuron from each from_neuron
        for from_neuron in from_neurons:
            for to_neuron in to_neurons:
                from_neuron.connect(to_neuron)
