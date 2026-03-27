import numpy as np
from collections import deque, defaultdict

class QuantumState:
    def __new__(cls, num: int):
        if num > 19:
            raise ValueError("Memory Attention!(Must n_qubits < 20)")
        return super().__new__(cls)

    def __init__(self, num: int):
        self.num = num
        self.state = (np.zeros((2**num, 1), dtype=complex))
        self.state[0][0] = 1
        self.digit = "0" + str(num) + "b"

    def get_state_vector(self) -> None:
        for i, vector in enumerate(self.state):
            print("|" + format(i, self.digit) +">:", end=" ")
            print(vector)
        return None
    
    def get_probability_vector(self) -> None:
        for i, vector in enumerate(self.state):
            print("|" + format(i, self.digit) + ">:", end=" ")
            print(vector.real**2+vector.imag**2)
        return None

    def sampling(self, count: int) -> None:
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
    I_gate = np.array([[1,0],[0,1]])
    X_gate = np.array([[0,1],[1,0]])
    Y_gate = np.array([[0,-1j],[1j,0]])
    Z_gate = np.array([[1,0],[0,-1]])
    H_gate = np.array([[1,1],[1,-1]])/np.sqrt(2)
    T_gate = np.array([[1,0],[0,np.exp(1j*np.pi/4)]])
    P0 = np.array([[1,0],[0,0]]) # P0 ->|0><0|
    P1 = np.array([[0,0],[0,1]]) # P1 -> |1><1|
    _gateBase_1q = {"x", "y", "z", "h", "t"}
    _gateBase_2q = {"cnot"}

    def __new__(cls, num: int):
        if num > 19:
            raise ValueError("Memory Attention!(Must n_qubits < 20)")
        return super().__new__(cls)

    def __init__(self, num: int):
        self.num = num
        self.gateArray = deque()

    def add_X_gate(self, num: int) -> None:
        if num < 0 or self.num-1 < num:
            print("not applied X_gate(index error).")
            return None
        self.gateArray.append(("x",num))
        return None
    def add_Y_gate(self, num: int) -> None:
        if num < 0 or self.num-1 < num:
            print("not applied Y_gate(index error).")
            return None
        self.gateArray.append(("y",num))
        return None
    def add_Z_gate(self, num: int) -> None:
        if num < 0 or self.num-1 < num:
            print("not applied Z_gate(index error).")
            return None
        self.gateArray.append(("z",num))
        return None
    def add_H_gate(self, num: int) -> None:
        if num < 0 or self.num-1 < num:
            print("not applied H_gate(index error).")
            return None
        self.gateArray.append(("h",num))
        return None
    def add_T_gate(self, num: int) -> None:
        if num < 0 or self.num-1 < num:
            print("not applied T_gate(index error).")
            return None
        self.gateArray.append(("t",num))
        return None

    def add_CNOT_gate(self, control: int, target: int) -> None:
        if control<0 or self.num-1 < control or target<0 or self.num-1 < target or control == target:
            print("not applied CNOT_gate(index error).")
            return None
        self.gateArray.append(("cnot",control,target))
        return None
    
    def get_info(self) -> None:
        if len(self.gateArray) == 0:
            print("No gates.")
            return None
        for gateInfo in self.gateArray:
            if gateInfo[0] in self._gateBase_1q:
                print("gateType:", gateInfo[0], ", target:", gateInfo[1])
            if gateInfo[0] in self._gateBase_2q:
                print("gateType:", gateInfo[0], ", control:", gateInfo[1], ", target:", gateInfo[2])
        return None

    def get_depth(self) -> None:
        backet = np.zeros(self.num, dtype=int)
        for key, value1, *rest in self.gateArray:
            value2 = rest[0] if rest else None
            if key in self._gateBase_1q:
                backet[value1] += 1
                
            if key in self._gateBase_2q:
                backet[value1] = max(backet[value1], backet[value2])+1
                backet[value2] = backet[value1]
                left = min(value1, value2)
                right = max(value1, value2)
                backet[left:right] = backet[value1]
                
            backet[backet < (backet[value1]-1)] = backet[value1]-1
        print("circuit depth :", np.max(backet))
        return None

    
    def update_quantum_state(self, state: QuantumState) -> None:
        if(state.num != self.num):
            print("dimensions error!")
            self.gateArray.clear()
            return None
        for key, value1, *rest in self.gateArray:
            value2 = rest[0] if rest else None
            if key in self._gateBase_1q:
                matrix = self._gate_validator(key)
                self._apply_1q_gate(state, matrix, value1)
                continue
            if key == "cnot":
                self._apply_cnot_gate(state, value1, value2)
                continue
            else:
                return None

        state.state[np.abs(state.state) < 1e-12] = 0 #optional
        return None
    
    def _gate_validator(self, key):
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
    
    def _apply_1q_gate(self, state: QuantumState, matrix, value1: int) -> None:
        for i in range(value1) :
            matrix = np.kron(matrix, self.I_gate)
        for i in range(self.num - 1 - value1):
            matrix = np.kron(self.I_gate, matrix)
        state.state = np.matmul(matrix, state.state)
        return None

    def _apply_cnot_gate(self, state: QuantumState, value1: int, value2: int) -> None:
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
    