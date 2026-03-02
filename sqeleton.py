import numpy as np
from collections import deque

class QuantumState:
    def __new__(cls, num: int):
        if num > 19:
            raise ValueError("Memory Attention!(Must n_qubits < 20)")
        return super().__new__(cls)

    def __init__(self, num: int):
        self.num = num
        self.state = (np.zeros((2**num, 1), dtype=complex))
        self.state[0][0] = 1

    def get_state_vector(self):
        print(self.state)

class QuantumCircuit:
    I_gate = np.array([[1,0],[0,1]])
    X_gate = np.array([[0,1],[1,0]])
    Y_gate = np.array([[0,-1j],[1j,0]])
    Z_gate = np.array([[1,0],[0,-1]])
    H_gate = np.array([[1,1],[1,-1]])/np.sqrt(2)
    T_gate = np.array([[1,0],[0,np.exp(1j*np.pi/4)]])
    P0 = np.array([[1,0],[0,0]]) # P0 ->|0><0|
    P1 = np.array([[0,0],[0,1]]) # P1 -> |1><1|

    def __new__(cls, num: int):
        if num > 19:
            raise ValueError("Memory Attention!(Must n_qubits < 20)")
        return super().__new__(cls)

    def __init__(self, num: int):
        self.num = num
        self.gateArray = deque()

    def add_X_gate(self, num: int):
        if num < 0 or self.num-1 < num:
            print("not applied X_gate(index error).")
            return None
        self.gateArray.append(("x",num))
        return None
    def add_Y_gate(self, num: int):
        if num < 0 or self.num-1 < num:
            print("not applied Y_gate(index error).")
            return None
        self.gateArray.append(("y",num))
        return None
    def add_Z_gate(self, num: int):
        if num < 0 or self.num-1 < num:
            print("not applied Z_gate(index error).")
            return None
        self.gateArray.append(("z",num))
        return None
    def add_H_gate(self, num: int):
        if num < 0 or self.num-1 < num:
            print("not applied H_gate(index error).")
            return None
        self.gateArray.append(("h",num))
        return None
    def add_T_gate(self, num: int):
        if num < 0 or self.num-1 < num:
            print("not applied T_gate(index error).")
            return None
        self.gateArray.append(("t",num))
        return None

    def add_CNOT_gate(self, a: int, b: int):
        if a<0 or self.num-1 < a or b<0 or self.num-1 < b:
            print("not applied CNOT_gate(index error).")
            return None
        self.gateArray.append(("cnot",a,b))
        return None
    
    def update_quantum_state(self, state: QuantumState):
        if(state.num != self.num):
            print("dimensions error!")
            self.gateArray.clear()
            return None
        for key, value1, *rest in self.gateArray:
            value2 = rest[0] if rest else None
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
            elif(key == "cnot"):
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
                continue
            else:
                return None
            
            for i in range(value1) :
                matrix = np.kron(matrix, self.I_gate)   
            for i in range(self.num - 1 - value1):
                matrix = np.kron(self.I_gate, matrix)
            state.state = np.matmul(matrix, state.state)

        self.gateArray.clear()
        state.state[np.abs(state.state) < 1e-12] = 0 #optional
        return None
    