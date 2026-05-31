import numpy as np
from collections import defaultdict
import random

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
        self.dim = 2**num
        self.state = (np.zeros((self.dim, 1), dtype=complex))
        self.state[0][0] = 1
        self.digit = "0" + str(num) + "b"

    def set_computational_basis(self, num: int) -> None:
        """set state

        Args:
            num (int): computational basis index

        Examples:
            >>> state = QuantumState(2)
            >>> state.set_computational_basis(3)
        """
        if (num < 0 or num > self.dim-1):
            raise IndexError("argment must be within 0 and 2^n")
        self.state[:] = 0
        self.state[num][0] = 1
        return None
    
    def set_Haar_random_state(self, seed=random.random()) -> None:
        """set random state

        Args:
            seed (float): optional random seed

        Examples:
            >>> state = QuantumState(2)
            >>> state.set_Haar_random_state()
        """
        tmp = 0
        random.seed(seed)
        for i in range(self.dim):
            real, imag = random.uniform(-1, 1), random.uniform(-1, 1)
            self.state[i][0] = real + imag*1j
            tmp += self.state[i][0] * self.state[i][0].conjugate()
        self.state[:] = self.state[:] / np.sqrt(tmp)

        return None

    def get_state_vector(self) -> str:
        """show state vector

        Examples:
            >>> state = QuantumState(2)
	        >>> s = state.get_state_vector()
            >>> print(s)
            |00>: [1.+0.j]
            |01>: [0.+0.j]
            |10>: [0.+0.j]
            |11>: [0.+0.j]
        """
        s = ""
        for i, vector in enumerate(self.state):
            s += "|" + format(i, self.digit) +">: " + str(vector)
            if (i < self.dim-1):
                s += "\n"
        return s
    
    def get_probability_vector(self) -> str:
        """show probability vector

        Examples:
            >>> state = QuantumState(2)
            >>> s = state.get_probability_vector()
            >>> print(s)
            |00>: [1.]
            |01>: [0.]
            |10>: [0.]
            |11>: [0.]
        """
        s = ""
        for i, vector in enumerate(self.state):
            s += "|" + format(i, self.digit) + ">: " + str(vector.real**2+vector.imag**2)
            if (i < self.dim-1):
                s += "\n"
        return s

    def sampling(self, count: int) -> str:
        """sampling in the computational basis

        Args:
            count (int): sampling number

        Examples:
            >>> state = QuantumState(2)
            >>> s = state.sampling(1000)
            >>> print(s)
            |00>: 1000
            |01>: 0
            |10>: 0
            |11>: 0
        """
        s = ""
        probability_list = [vector[0].real**2+vector[0].imag**2 for vector in self.state] #note: self.state is 2-dimensional array
        bitarray = [format(i, self.digit) for i in range(self.dim)]
        result = np.random.choice(bitarray, size=count, replace=True, p=probability_list)
        sampling_result = defaultdict(list)
        for i in range(self.dim):
            sampling_result[format(i, self.digit)] = 0
        for i in range(count):
            sampling_result[result[i]] += 1
        for i, key in enumerate(bitarray):
            s += "|" + str(key) + ">: " + str(sampling_result[key])
            if (i < self.dim-1):
                s += "\n"
        return s
