# Sqeleton
Sqeleton is a quantum circuit simulator.    

Sqeleton has minimum functions such as QuantumState(state vector), QuantumCircuit(1q-gate(pauli,H,T) and 2q-gate(CNOT)).

# Architecture
## Class: QuantumState
n-qubits QuantumState is implemented by numpy column vector(2^n) and set zero state.  

get_state_vector() method shows n-qubits state vector.

```bash
2qubits
[[0.70710678+0.j]  <- |00>
 [0.        +0.j]  <- |01>
 [0.        +0.j]  <- |10>
 [0.70710678+0.j]] <- |11>
```

## Class: QuantumCircuit
Extended single- and two-qubit gate matrices to n-qubit systems by explicitly constructing tensor-product (np.kron(A,B)) operators, derived and validated through manual linear algebra calculations (np.matmul(C,D)).  

Deque has applied gates order and is used when call update_quantum_state() method.

# Feature
Easy to understand(100LOC python) and support to understand how recently quantum circuit simulators are built by reading sqeleton code.   

Sqeleton has simulator core logic.


# Requirement
* numpy

# Usage
clone sqeleton.py from this repository and import it.  

usage.py is a simple example file for how to use this simulator quickly. 


```bash
git clone https://github.com/serowri/sqeleton.git
cd sqeleton
python usage.py
```

# Sample Python Code
```python
from sqeleton import *

num = 2
state = QuantumState(num)
circuit = QuantumCircuit(num)
circuit.add_H_gate(0)
circuit.add_CNOT_gate(0,1)
circuit.update_quantum_state(state)
state.get_state_vector()
```

# Note
Sqeleton is so short and simple that lack precision(now especially calculation results).  
Sqeleton is very slow.  
Now available add_#_gate() (#: choose from {X,Y,Z,H,T,CNOT}).

# License
"Sqeleton" is under [MIT license]
