from sqeleton import *
import numpy as np

def test_X_gate():
    state = QuantumState(1)
    circuit = QuantumCircuit(1)
    circuit.add_X_gate(0)
    circuit.update_quantum_state(state)

    expected = np.array([
        [0], [1]
    ], dtype=complex)

    assert np.allclose(state.state, expected)

def test_H_gate():
    state = QuantumState(1)
    circuit = QuantumCircuit(1)
    circuit.add_H_gate(0)
    circuit.update_quantum_state(state)

    expected = np.array([
        [1/np.sqrt(2)], [1/np.sqrt(2)]
    ], dtype=complex)

    assert np.allclose(state.state, expected)