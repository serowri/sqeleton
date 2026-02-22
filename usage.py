from sqeleton import *


state = QuantumState(2)
circuit = QuantumCircuit(2)
circuit.add_H_gate(0)
circuit.update_quantum_state(state)
state.get_state_vector()