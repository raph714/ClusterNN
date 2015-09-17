import random
import math


class Connection(object):
    def __init__(self, input_neuron, output_neuron, new_weight=None):
        if new_weight:
            self.weight = new_weight
        else:
            self.weight = random.random()
        self.input_neuron = input_neuron
        self.output_neuron = output_neuron

    def transmit(self, signal=None):
        if signal is None:
            return

        output_signal = self.weight * signal
        self.output_neuron.process_signal(sender=self, signal=output_signal)

    def output_neuron_did_transmit(self):
        """
        An opportunity to do something in response to the output neuron triggering
        """
        pass


class Neuron(object):
    def __init__(self):
        #change these to sets
        self.outputs = []
        self.inputs = []
        self.threshold = 1.0

        self.current_input = 0
        self.input_count = 0

        self.error = 0
        self.timestep = 0
        self.error_count = 0

    def process_signal(self, sender=None, signal=None):
        if sender is None or signal is None:
            return

        self.current_input = self.current_input + signal
        self.input_count = self.input_count + 1

        if self.input_count == len(self.inputs):
            [x.transmit(signal=self.sigmoid(self.current_input)) for x in self.outputs]

        return

        # if self.current_input > self.threshold:
        #     [x.transmit(signal=self.current_input) for x in self.outputs]

        #     #maybe say somethin back to whoever just sent us the message.
        #     sender.output_neuron_did_transmit()
        #     self.timestep = self.timestep + 1
        #     self.current_input = 0

    def connect(self, neuron):
        connection = Connection(self, neuron)
        self.outputs.append(connection)
        neuron.inputs.append(connection)
        return connection

    def sigmoid(self, x):
        if x < -100:
            return 0.0
        if x > 100:
            return 1.0
        return 1/(1 + math.exp(-x))

    """
    first get the error (target - actual output) for the output vs target.
    output from a nueron * error rate * learning rate

    add in timestep information.
    """
