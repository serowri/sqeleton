# Sqeleton
Sqeleton is a quantum circuit simulator.    

Sqeleton has minimum functions such as QuantumState(state vector), QuantumCircuit(1q-gate(pauli,H,T) and 2q-gate(CNOT)).

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

state = QuantumState(2)
circuit = QuantumCircuit(2)
circuit.add_H_gate(0)
circuit.add_CNOT_gate(0,1)
circuit.update_quantum_state(state)
state.get_state_vector()
```

# Note
Sqeleton is so short and simple that lack precision(now especially calculation results).  
Sqeleton is very slow.  
Now available add_#_gate() (#: choose from {X,Y,Z,H,T,CONT}).

# License
"Sqeleton" is under [MIT license]
