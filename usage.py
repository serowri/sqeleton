from src.sqeleton import *


state = qs(2) # state = QuantumState(2)
circuit = qc(2) # circuit = QuantumCircuit(2)
circuit.add_H_gate(0)
circuit.add_CNOT_gate(0,1)
circuit.update_quantum_state(state)
state.get_state_vector()