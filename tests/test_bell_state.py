from sqeleton import *
import numpy as np
import pytest

def test_bell_state():
    state = QuantumState(2)
    circuit = QuantumCircuit(2)
    circuit.add_H_gate(0)
    circuit.add_CNOT_gate(0,1)
    circuit.update_quantum_state(state)

    expected = np.array([
        [1/np.sqrt(2)], [0], [0], [1/np.sqrt(2)]
    ], dtype=complex)
    
    assert np.allclose(state.state, expected)