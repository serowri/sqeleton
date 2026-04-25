import numpy as np
from collections import deque, defaultdict
import re

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


class QuantumCircuit:
    """have gate and methods"""
    I_gate = np.array([[1,0],[0,1]])
    X_gate = np.array([[0,1],[1,0]])
    Y_gate = np.array([[0,-1j],[1j,0]])
    Z_gate = np.array([[1,0],[0,-1]])
    H_gate = np.array([[1,1],[1,-1]])/np.sqrt(2)
    T_gate = np.array([[1,0],[0,np.exp(1j*np.pi/4)]])
    P0 = np.array([[1,0],[0,0]]) # P0 ->|0><0|
    P1 = np.array([[0,0],[0,1]]) # P1 -> |1><1|
    _gateBase_1q = {"x", "y", "z", "h", "t"}
    _gateRotate_1q = {"rx", "ry", "rz"}
    _gateBase_2q = {"cnot"}

    def __new__(cls, num: int):
        """validate number of qubit"""
        if num > 19:
            raise ValueError("Memory Attention!(Must n_qubits < 20)")
        return super().__new__(cls)

    def __init__(self, num: int):
        """inits a `QuantumCircuit`.

        Args:
            num (int): number of qubit

        Examples:
            >>> circuit = QuantumCircuit(2)
        """
        self.num = num
        self.gateArray = deque()

    def add_X_gate(self, num: int) -> None:
        """add X gate in gateArray

        Args:
            num (int): target qubit index

        Raises:
            index error: target index is out of range

        Examples:
            >>> circuit = QuantumCircuit(2)
            >>> circuit.add_X_gate(0)
        """
        if num < 0 or self.num-1 < num:
            print("not applied X_gate(index error).")
            return None
        self.gateArray.append(("x",num))
        return None
    def add_Y_gate(self, num: int) -> None:
        """add Y gate in gateArray

        Args:
            num (int): target qubit index

        Raises:
            index error: target index is out of range
        """
        if num < 0 or self.num-1 < num:
            print("not applied Y_gate(index error).")
            return None
        self.gateArray.append(("y",num))
        return None
    def add_Z_gate(self, num: int) -> None:
        """add Z gate in gateArray

        Args:
            num (int): target qubit index

        Raises:
            index error: target index is out of range
        """
        if num < 0 or self.num-1 < num:
            print("not applied Z_gate(index error).")
            return None
        self.gateArray.append(("z",num))
        return None
    def add_H_gate(self, num: int) -> None:
        """add H gate in gateArray

        Args:
            num (int): target qubit index

        Raises:
            index error: target index is out of range
        """
        if num < 0 or self.num-1 < num:
            print("not applied H_gate(index error).")
            return None
        self.gateArray.append(("h",num))
        return None
    def add_T_gate(self, num: int) -> None:
        """add T gate in gateArray

        Args:
            num (int): target qubit index

        Raises:
            index error: target index is out of range
        """
        if num < 0 or self.num-1 < num:
            print("not applied T_gate(index error).")
            return None
        self.gateArray.append(("t",num))
        return None
    
    def add_RX_gate(self, num: int, theta: float) -> None:
        """add RX gate in gateArray

        Args:
            num (int): target qubit index
            theta (float): rotate angle

        Raises:
            index error: target index is out of range

        Examples:
            >>> circuit = QuantumCircuit(2)
            >>> circuit.add_RX_gate(0, np.pi)
        """
        if num < 0 or self.num-1 < num:
            print("not applied RX_gate(index error).")
            return None
        self.gateArray.append(("rx",num,theta))
        return None
    def add_RY_gate(self, num: int, theta: float) -> None:
        """add RY gate in gateArray

        Args:
            num (int): target qubit index
            theta (float): rotate angle

        Raises:
            index error: target index is out of range
        """
        if num < 0 or self.num-1 < num:
            print("not applied RY_gate(index error).")
            return None
        self.gateArray.append(("ry",num,theta))
        return None
    def add_RZ_gate(self, num: int, theta: float) -> None:
        """add RZ gate in gateArray

        Args:
            num (int): target qubit index
            theta (float): rotate angle

        Raises:
            index error: target index is out of range
        """
        if num < 0 or self.num-1 < num:
            print("not applied RZ_gate(index error).")
            return None
        self.gateArray.append(("rz",num,theta))
        return None

    def add_CNOT_gate(self, control: int, target: int) -> None:
        """add CNOT gate in gateArray

        Args:
            control (int): control qubit index
            target (int): target qubit index

        Raises:
            index error: target index is out of range

        Examples:
            >>> circuit = QuantumCircuit(2)
            >>> circuit.add_CNOT_gate(0, 1)
        """
        if control<0 or self.num-1 < control or target<0 or self.num-1 < target or control == target:
            print("not applied CNOT_gate(index error).")
            return None
        self.gateArray.append(("cnot",control,target))
        return None
    
    def get_info(self) -> None:
        """show circuit information
        (gateType (x,y,z,h,t,rx,ry,rx,cnot), qubit index (target, control), theta (if gate is rotation gate))

        Examples:
            >>> circuit = QuantumCircuit(2)
            >>> circuit.add_X_gate(0)
            >>> circuit.add_RX_gate(0, np.pi)
            >>> circuit.add_CNOT_gate(0, 1)
            >>> circuit.get_info()
            gateType: x , target: 0
            gateType: rx , target: 0 , theta: 3.141592653589793
            gateType: cnot , control: 0 , target: 1
        """
        if len(self.gateArray) == 0:
            print("No gates.")
            return None
        for gateInfo in self.gateArray:
            if gateInfo[0] in self._gateBase_1q:
                print("gateType:", gateInfo[0], ", target:", gateInfo[1])
            if gateInfo[0] in self._gateRotate_1q:
                print("gateType:", gateInfo[0], ", target:", gateInfo[1], ", theta:", gateInfo[2])
            if gateInfo[0] in self._gateBase_2q:
                print("gateType:", gateInfo[0], ", control:", gateInfo[1], ", target:", gateInfo[2])
        return None

    def get_depth(self) -> int:
        """show circuit depth

        Examples:
            >>> circuit = QuantumCircuit(2)
            >>> circuit.add_X_gate(0)
            >>> circuit.add_RX_gate(0, np.pi)
            >>> circuit.add_CNOT_gate(0, 1)
            >>> circuit.get_depth()
            circuit depth : 3
        """
        backet = np.zeros(self.num, dtype=int)
        for key, value1, *rest in self.gateArray:
            value2 = rest[0] if rest else None
            if key in (self._gateBase_1q | self._gateRotate_1q):
                backet[value1] += 1

            if key in self._gateBase_2q:
                backet[value1] = max(backet[value1], backet[value2])+1
                backet[value2] = backet[value1]

        return np.max(backet)

    
    def update_quantum_state(self, state: QuantumState) -> None:
        """interface of calling internal apply methods

        Args:
            state (QuantumState): target state to apply circuit

        Examples:
            >>> state = QuantumState(2)
            >>> circuit = QuantumCircuit(2)
            >>> circuit.update_quantum_state(state)
        """
        if(state.num != self.num):
            print("dimensions error!")
            self.gateArray.clear()
            return None
        for key, value1, *rest in self.gateArray:
            value2 = rest[0] if rest else None
            if key in self._gateBase_1q:
                self._apply_1q_gate(state, self._gate_validator(key), value1)
                continue
            if key in self._gateRotate_1q:
                self._apply_1q_gate(state, self._rotate_gate_generator(key, value2), value1)
                continue
            if key == "cnot":
                self._apply_cnot_gate(state, value1, value2)
                continue
            else:
                return None

        state.state[np.abs(state.state) < 1e-12] = 0 #optional
        return None
    
    def _gate_validator(self, key):
        """internal: gate validator

        Args:
            key (str): gate one of the _gateBase_1q set

        Returns:
            matrix (NDArray): row matrix (2*2)
        """
        if(key == "x"):
            matrix = self.X_gate
        elif(key == "y"):
            matrix = self.Y_gate
        elif(key == "z"):
            matrix = self.Z_gate
        elif(key == "h"):
            matrix = self.H_gate
        elif(key == "t"):
            matrix = self.T_gate
        return matrix

    def _rotate_gate_generator(self, key: str, theta):
        """internal: generate rotate gate

        Args:
            key (str): gate one of the _gateRotate_1q set
            theta (float): rotation angle

        Returns:
            no name (NDArray): row matrix (2*2)
        """
        if key == "rx":
            return np.array([[np.cos(theta/2), -1j*np.sin(theta/2)], [-1j*np.sin(theta/2), np.cos(theta/2)]])
        if key == "ry":
            return np.array([[np.cos(theta/2), -1j*np.sin(theta/2)], [np.sin(theta/2), np.cos(theta/2)]])
        if key == "rz":
            return np.array([[np.exp(-1j*theta/2), 0], [0, np.exp(1j*theta/2)]])
    
    def _apply_1q_gate(self, state: QuantumState, matrix, value1: int) -> None:
        """internal: apply row matrix (1q) to state vector

        Args:
            state (QuantumState): state vector
            matrix (NDArray): row matrix (2*2)
            value1 (int): target qubit index
        """
        for i in range(value1) :
            matrix = np.kron(matrix, self.I_gate)
        for i in range(self.num - 1 - value1):
            matrix = np.kron(self.I_gate, matrix)
        state.state = np.matmul(matrix, state.state)
        return None

    def _apply_cnot_gate(self, state: QuantumState, value1: int, value2: int) -> None:
        """internal: apply cnot-gate to state vector

        Args:
            state (QuantumState): state vector
            value1 (int): control qubit index
            value2 (int): target qubit index
        """
        alpha = self.P0
        beta = self.P1
        for i in range(value1):
            alpha = np.kron(alpha, self.I_gate)
        for i in range(self.num - 1 - value1):
            alpha = np.kron(self.I_gate ,alpha)
                
        for i in range(value1):
            if(i == value2):
                beta = np.kron(beta, self.X_gate)
                continue
            beta = np.kron(beta, self.I_gate)
        for i in range(self.num - 1 - value1):
            if(i+value1+1 == value2):
                beta = np.kron(self.X_gate, beta)
                continue
            beta = np.kron(self.I_gate, beta)
        state.state = np.matmul(alpha+beta, state.state)

        return None
    

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

    def add_oparator(self, s, coef=1.0) -> None:
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
            >>> observable.expectation_value(state)
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