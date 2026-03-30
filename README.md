# Sqeleton
Sqeleton is a quantum circuit simulator and not for practical use simulator.    

Sqeleton has minimum functions such as QuantumState(state vector), QuantumCircuit(1q-gate(pauli,Rotation pauli,H,T) and 2q-gate(CNOT)).

# Architecture
## Class: QuantumState
n-qubits QuantumState is implemented by numpy column vector($2^n$) and set zero state.  

**Public Method**
- get_state_vector
- get_probability_vector
- sampling

## Class: QuantumCircuit
Create matrix($2^n*2^n$) directly for each gate.  
Extended single- and two-qubit gate matrices to n-qubit systems by explicitly constructing tensor-product (`np.kron(A,B)`) operators, derived and validated through manual linear algebra calculations (`np.matmul(C,D)`).  

**Public Method**
- add_#_gate (#: X, Y, Z, H, T , RX, RY, RZ and CNOT)
- update_quantum_state
- get_info
- get_depth

# Feature
Sqeleton is not suited for practical use but for education and beginners.
- Directly generate matrix($2^n*2^n$)
- Consume your device memory massively

Most of practical use quantum circuit simulators don't directly create large matrix.  
Support to understand how recently quantum circuit simulators are built by reading sqeleton code.  
Sqeleton has simulator core logic but not opimized for practical use.


# Requirement
* numpy
* uv

# Usage
Clone sqeleton.py from this repository and import it.  

usage.py is a simple example file for how to use this simulator quickly. 


```bash
git clone https://github.com/serowri/sqeleton.git
cd sqeleton
uv run python usage.py
```

or simply copy row code of src/sqeleton.py and import it. (only need numpy)

# Sample Python Code
```python
from src.sqeleton import *

n_qubits = 2
state = QuantumState(n_qubits)
circuit = QuantumCircuit(n_qubits)
circuit.add_H_gate(0)
circuit.add_CNOT_gate(0,1)
circuit.update_quantum_state(state)
state.get_state_vector()
state.get_probability_vector()
state.sampling(1000)
```

# Note
Right end qubit is LSB: $|q_n,...,q_1,q_0>$  
Sqeleton is so simple and slow. ~~that lack precision(now especially calculation results)~~    
Limitation: `n-qubits < 20`.


# Looking forward to your comments!
> [Discussion](https://github.com/serowri/sqeleton/discussions/6)

# MIT License