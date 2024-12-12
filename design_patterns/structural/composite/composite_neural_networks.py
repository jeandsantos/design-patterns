from __future__ import annotations

from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):
    def connect_to(self, other: Connectable):
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name: str):
        self.name: str = name
        self.inputs: list[Neuron] = []
        self.outputs: list[Neuron] = []

    def __str__(self):
        return f"Neuron {self.name} with {len(self.inputs)} inputs and {len(self.outputs)} outputs"

    def __iter__(self):
        yield self


class NeuralLayer(list, Connectable):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name: str = name
        for i in range(count):
            self.append(Neuron(f"{name}-{i}"))

    def __str__(self):
        return f"Layer {self.name} with {len(self)} neurons"


def main():
    neuron1 = Neuron("neuron1")
    neuron2 = Neuron("neuron2")
    layer1 = NeuralLayer("layer1", 3)
    layer2 = NeuralLayer("layer2", 4)

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print("neuron1:", neuron1)
    print("neuron2:", neuron2)
    print("layer1:", layer1)
    print("layer2:", layer2)


if __name__ == "__main__":
    main()
    # output:
    # neuron1: Neuron neuron1 with 0 inputs and 4 outputs
    # neuron2: Neuron neuron2 with 4 inputs and 0 outputs
    # layer1: Layer layer1 with 3 neurons
    # layer2: Layer layer2 with 4 neurons
