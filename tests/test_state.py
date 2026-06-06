from sqeleton import *
import numpy as np
import random

#-------------------------------------------------#
# Quantum entanglement

# EPR, Bell
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

def test_set_computational_basis():
    n_qubits = 4
    state = QuantumState(n_qubits)
    choices = [i for i in range(state.dim)]
    random_choice = random.choice(choices)
    state.set_computational_basis(random_choice)
    expected = np.array([
        [1] if i == random_choice else [0] for i in range(state.dim)
    ], dtype=complex)

    assert np.allclose(state.state, expected)

def test_set_Haar_random():
    n_qubits = 4
    state = QuantumState(n_qubits)
    state.set_Haar_random_state()
    total = np.vdot(state.state, state.state)
    
    assert np.allclose(total, 1.0)
