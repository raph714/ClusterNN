class TimingController(object):
    def __init__(self):
        self.connections = []
        self.neurons = []
        self.processing = True

    def set_connections(self, connections):
        self.connections = connections

    def add_connection(self, con):
        self.connections.append(con)

    def set_neurons(self, neurons):
        self.neurons = neurons

    def add_neuron(self, neuron):
        self.neurons.append(neuron)

    def cycle(self):
        for n in self.neurons:
            n.fire_signal()

        for c in self.connections:
            c.fire_signal()

        if self.processing:
            self.cycle()

    def start(self):
        self.processing = True
        self.cycle()

    def stop(self):
        for n in self.neurons:
            n.reset()
        for c in self.connections:
            c.reset()
        self.processing = False
