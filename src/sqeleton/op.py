import numpy as np
from collections import deque
import re
from .qs import *

class Operator:
    I = np.array([[1, 0], [0 ,1]])
    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.array([[1, 0], [0, -1]])
    _pauliSet = {"I", "X", "Y", "Z"}

    def __init__(self, num):
        """inits operator class

        Args:
            num (int): number of qubit

        Examples:
            >>> n_qubits = 2
            >>> observable = Operator(n_qubits)
        """
        self.num = num
        self.observableArray = deque()

    def add_operator(self, s, coef=1.0) -> None:
        """add operator

        Args:
            s (str): operator string
            coef (any): coefficiency default(1.0)

        Examples:
            >>> observable = Operator(2)
            >>> observable.add_operator("Z(0), Z(1)", coef=2.0)
        """
        numSet = set()
        tmp = {}
        s = re.sub(r"\s+", "", s)
        args = s.split(",")
        for arg in args:
            if arg[0] not in self._pauliSet:
                print("error: invalid operator.")
                return None
            if arg[0] == "I":
                index = self._i_index(arg)
            if arg[0] == "X":
                index = self._x_index(arg)
            if arg[0] == "Y":
                index = self._y_index(arg)
            if arg[0] == "Z":
                index = self._z_index(arg)
            if index in numSet:
                print("error: index duplicated.")
                return None
            if int(index) < 0 or self.num-1 < int(index):
                print("error: index out of range.")
                return None
            numSet.add(index)
            tmp[f"{index}"] = f"{arg[0]}"
        
        self.observableArray.append((coef, tmp))
        return None

    def expectation_value(self, state: QuantumState):
        """calculate expectation value

        Args:
            state (QuantumState): state vector

        Examples:
            >>> n_qubits = 2
            >>> state = QuantumState(n_qubits)
            >>> observable = Operator(n_qubits)
            >>> observable.add_operator("Z(0), Z(1)", coef=2.0)
            >>> value = observable.expectation_value(state)
            >>> print(value)
            [2.+0.j]
        """
        if state.num != self.num:
            print("dimensions error!")
            return None
        matrix = (np.zeros((2**self.num, 2**self.num), dtype=complex))
        for i in range(len(self.observableArray)):
            matrix += self._matrixGenerator(self.observableArray[i])
        res = np.matmul(state.state.conjugate().T, np.matmul(matrix, state.state))
        return res[0]


    def _i_index(self, arg) -> int:
        """internal: index getter

        Args:
            arg (str): pauli operator and index

        Returns:
            index
        """
        pattern = r"I\(\d\)"
        results = re.findall(pattern, arg)
        if len(results) == 1:
            return re.findall(r"\d", results[0])[0]
        print("error: must be format I(num)")
        return -1

    def _x_index(self, arg) -> int:
        """internal: index getter

        Args:
            arg (str): pauli operator and index

        Returns:
            index
        """
        pattern = r"X\(\d\)"
        results = re.findall(pattern, arg)
        if len(results) == 1:
            return re.findall(r"\d", results[0])[0]
        print("error: must be format X(num)")
        return -1

    def _y_index(self, arg) -> int:
        """internal: index getter

        Args:
            arg (str): pauli operator and index

        Returns:
            index
        """
        pattern = r"Y\(\d\)"
        results = re.findall(pattern, arg)
        if len(results) == 1:
            return re.findall(r"\d", results[0])[0]
        print("error: must be format Y(num)")
        return -1

    def _z_index(self, arg) -> int:
        """internal: index getter

        Args:
            arg (str): pauli operator and index

        Returns:
            index
        """
        pattern = r"Z\(\d\)"
        results = re.findall(pattern, arg)
        if len(results) == 1:
            return re.findall(r"\d", results[0])[0]
        print("error: must be format Z(num)")
        return -1

    def _matrixGenerator(self, observable):
        """internal: Expand matrix based on given pauli operators

        Args:
            observable: operator array

        Returns:
            tmp: Expanded matrix
        """
        tmp = observable[0]
        for i in range(self.num):
            operator = observable[1].get(str(f"{i}"), "I")
            if operator == "I":
                tmp = np.kron(self.I, tmp)
            elif operator == "X":
                tmp = np.kron(self.X, tmp)
            elif operator == "Y":
                tmp = np.kron(self.Y, tmp)
            elif operator == "Z":
                tmp = np.kron(self.Z, tmp)
        return tmp
