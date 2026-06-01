import numpy as np
from collections import deque
from .qs import *

class QuantumCircuit:
    """have gate and methods"""
    I_gate = np.array([[1,0],[0,1]])
    X_gate = np.array([[0,1],[1,0]])
    Y_gate = np.array([[0,-1j],[1j,0]])
    Z_gate = np.array([[1,0],[0,-1]])
    H_gate = np.array([[1,1],[1,-1]])/np.sqrt(2)
    S_gate = np.array([[1,0],[0,1j]])
    T_gate = np.array([[1,0],[0,np.exp(1j*np.pi/4)]])
    P0 = np.array([[1,0],[0,0]]) # P0 ->|0><0|
    P1 = np.array([[0,0],[0,1]]) # P1 -> |1><1|
    _gateBase_1q = {"x", "y", "z", "h", "s", "t"}
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
    def add_S_gate(self, num: int) -> None:
        """add S gate in gateArray

        Args:
            num (int): target qubit index

        Raises:
            index error: target index is out of range
        """
        if num < 0 or self.num-1 < num:
            print("not applied S_gate(index error).")
            return None
        self.gateArray.append(("s",num))
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
    
    def get_info(self) -> str:
        """show circuit information
        (gateType (x,y,z,h,t,rx,ry,rx,cnot), qubit index (target, control), theta (if gate is rotation gate))

        Examples:
            >>> circuit = QuantumCircuit(2)
            >>> circuit.add_X_gate(0)
            >>> circuit.add_RX_gate(0, np.pi)
            >>> circuit.add_CNOT_gate(0, 1)
            >>> s = circuit.get_info()
            >>> print(s)
            gateType: x , target: 0
            gateType: rx , target: 0 , theta: 3.141592653589793
            gateType: cnot , control: 0 , target: 1
        """
        s = ""
        if len(self.gateArray) == 0:
            print("No gates.")
            return None
        for i, gateInfo in enumerate(self.gateArray):
            if gateInfo[0] in self._gateBase_1q:
                s += "gateType:" + str(gateInfo[0]) + ", target:" + str(gateInfo[1])
            if gateInfo[0] in self._gateRotate_1q:
                s += "gateType:" + str(gateInfo[0]) + ", target:" + str(gateInfo[1]) + ", theta:" + str(gateInfo[2])
            if gateInfo[0] in self._gateBase_2q:
                s += "gateType:" + str(gateInfo[0]) + ", control:" + str(gateInfo[1]) + ", target:" + str(gateInfo[2])
            if (i < len(self.gateArray)-1):
                s += "\n"
        return s

    def get_depth(self) -> int:
        """show circuit depth

        Examples:
            >>> circuit = QuantumCircuit(2)
            >>> circuit.add_X_gate(0)
            >>> circuit.add_RX_gate(0, np.pi)
            >>> circuit.add_CNOT_gate(0, 1)
            >>> depth = circuit.get_depth()
            >>> print("circuit depth: " + str(depth))
            circuit depth: 3
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

        # optional
        # state.state[np.abs(state.state) < 1e-12] = 0
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
        elif(key == "s"):
            matrix = self.S_gate
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
