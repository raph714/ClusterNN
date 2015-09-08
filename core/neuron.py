import random


class Connection(object):
    weight = 1.0
    input_neuron = None
    output_neuron = None

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
    threshold = 1.0
    current_input = 0

    outputs = None

    def __init__(self):
        self.outputs = []

    def process_signal(self, sender=None, signal=None):
        if sender is None or signal is None:
            return

        self.current_input = self.current_input + signal

        if self.current_input > self.threshold:
            [x.transmit(signal=self.current_input) for x in self.outputs]

            #maybe say somethin back to whoever just sent us the message.
            sender.output_neuron_did_transmit()
            self.current_input = 0

    def connect(self, neuron):
        connection = Connection(self, neuron)
        self.outputs.append(connection)
        return connection

    """
    first get the error (target - actual output) for the output vs target.
    output from a nueron * error rate * learning rate

    record that a neuron fired.

    add in timestep information.
    """
