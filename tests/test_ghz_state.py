from sqeleton import *
import numpy as np

def test_ghz_3q_0():
    state = QuantumState(3)
    circuit = QuantumCircuit(3)
    circuit.add_H_gate(0)
    circuit.add_CNOT_gate(0,1)
    circuit.add_CNOT_gate(0,2)
    circuit.update_quantum_state(state)

    expected = np.array([
        [1/np.sqrt(2)], [0], [0], [0], [0], [0], [0], [1/np.sqrt(2)]
    ], dtype=complex)

    assert np.allclose(state.state, expected)

def test_ghz_3q_1():
    state = QuantumState(3)
    circuit = QuantumCircuit(3)
    circuit.add_H_gate(0)
    circuit.add_CNOT_gate(0,1)
    circuit.add_CNOT_gate(1,2)
    circuit.update_quantum_state(state)

    expected = np.array([
        [1/np.sqrt(2)], [0], [0], [0], [0], [0], [0], [1/np.sqrt(2)]
    ], dtype=complex)

    assert np.allclose(state.state, expected)