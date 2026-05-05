import numpy as np
from collections import defaultdict

class QuantumState:
    """manage state vector"""

    def __new__(cls, num: int):
        """validate number of qubit"""

        if num > 19:
            raise ValueError("Memory Attention!(Must n_qubits < 20)")
        return super().__new__(cls)

    def __init__(self, num: int):
        """inits a `QuantumState`.

        Args:
            num (int): number of qubit

        Examples:
            >>> state = QuantumState(2)
        """
        self.num = num
        self.state = (np.zeros((2**num, 1), dtype=complex))
        self.state[0][0] = 1
        self.digit = "0" + str(num) + "b"

    def get_state_vector(self) -> None:
        """show state vector

        Examples:
            >>> state = QuantumState(2)
	        >>> state.get_state_vector()
            |00>: [1.+0.j]
            |01>: [0.+0.j]
            |10>: [0.+0.j]
            |11>: [0.+0.j]
        """
        for i, vector in enumerate(self.state):
            print("|" + format(i, self.digit) +">:", end=" ")
            print(vector)
        return None
    
    def get_probability_vector(self) -> None:
        """show probability vector

        Examples:
            >>> state = QuantumState(2)
            >>> state.get_probability_vector()
            |00>: [1.]
            |01>: [0.]
            |10>: [0.]
            |11>: [0.]
        """
        for i, vector in enumerate(self.state):
            print("|" + format(i, self.digit) + ">:", end=" ")
            print(vector.real**2+vector.imag**2)
        return None

    def sampling(self, count: int) -> None:
        """sampling in the computational basis

        Args:
            count (int): sampling number

        Examples:
            >>> state = QuantumState(2)
            >>> state.sampling(1000)
            |00>: 1000
            |01>: 0
            |10>: 0
            |11>: 0
        """
        probability_list = [vector[0].real**2+vector[0].imag**2 for vector in self.state] #note: self.state is 2-dimensional array
        bitarray = [format(i, self.digit) for i in range(2**self.num)]
        result = np.random.choice(bitarray, size=count, replace=True, p=probability_list)
        sampling_result = defaultdict(list)
        for i in range(2**self.num):
            sampling_result[format(i, self.digit)] = 0
        for i in range(count):
            sampling_result[result[i]] += 1
        for key in bitarray:
            print("|" + key + ">:", end=" ")
            print(sampling_result[key])
        return None