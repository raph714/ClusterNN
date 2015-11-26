import random
from scipy.special import expit as sigmoid


class Connection(object):
    def __init__(self, input_neuron, output_neuron, new_weight=None):
        if new_weight:
            self.weight = new_weight
        else:
            self.weight = random.random()
        self.input_neuron = input_neuron
        self.output_neuron = output_neuron
        self.signal = 0

    def receive_signal(self, signal=None):
        if signal is None:
            signal = 0
        self.signal = signal
        # print "CON receive %s" % self.signal

    def fire_signal(self):
        if self.signal > 0:
            # print "CON send %s" % self.signal
            output_signal = self.weight * self.signal
            self.output_neuron.receive_signal(sender=self.input_neuron, signal=output_signal)
            self.signal = 0

    def output_neuron_did_transmit(self):
        """
        An opportunity to do something in response to the output neuron triggering
        """
        pass

    def learn(self, signal=None):
        if signal is None:
            output_signal = 0
        else:
            output_signal = self.weight / signal
        self.input_neuron.learn(sender=self.output_neuron, signal=output_signal)

    def reset(self):
        self.signal = 0


class Neuron(object):
    def __init__(self, controller):
        self.controller = controller

        #change these to sets
        self.outputs = []
        self.inputs = []
        self.threshold = 0.0

        self.current_input = 0

        self.error = 0
        self.timestep = 0
        self.error_count = 0

        self.times_fired = 0

    def receive_signal(self, sender=None, signal=None):
        if signal is None:
            signal = 0

        # print "NEURON receive %s" % signal
        self.current_input = self.current_input + signal
        # print "NEURON current Input %s" % self.current_input

    def fire_signal(self):
        if self.current_input > self.threshold:
            # print "NEURON send %s" % sigmoid(self.current_input)
            [x.receive_signal(signal=sigmoid(self.current_input)) for x in self.outputs]
            self.current_input = 0
            self.times_fired += 1

    def learn(self, sender=None, signal=None):
        if signal is None:
            signal = 0

    def connect(self, neuron):
        connection = Connection(self, neuron)
        self.outputs.append(connection)
        neuron.inputs.append(connection)
        return connection

    def reset(self):
        self.current_input = 0
        self.times_fired = 0

    """
    first get the error (target - actual output) for the output vs target.
    output from a nueron * error rate * learning rate

    add in timestep information.
    """

    #Explore the idea that a neuron can just fire whenever it's ready to fire, disregarding
    #the number of inputs it has received. Of course we would need a way of garunteeing
    #concurrency.

    # if self.current_input > self.threshold:
    #     [x.transmit(signal=self.current_input) for x in self.outputs]

    #     #maybe say somethin back to whoever just sent us the message.
    #     sender.output_neuron_did_transmit()
    #     self.timestep = self.timestep + 1
    #     self.current_input = 0
