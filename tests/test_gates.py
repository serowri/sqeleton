from sqeleton import *
import numpy as np
import random

def test_X_gate():
    state = QuantumState(1)
    circuit = QuantumCircuit(1)
    circuit.add_X_gate(0)
    circuit.update_quantum_state(state)

    expected = np.array([
        [0], [1]
    ], dtype=complex)

    assert np.allclose(state.state, expected)

    state = QuantumState(2)
    circuit = QuantumCircuit(2)
    circuit.add_X_gate(0)
    circuit.update_quantum_state(state)

    expected = np.array([
        [0], [1], [0], [0]
    ], dtype=complex)

    assert np.allclose(state.state, expected)    

def test_Y_gate():
    state = QuantumState(1)
    circuit = QuantumCircuit(1)
    circuit.add_Y_gate(0)
    circuit.update_quantum_state(state)

    expected = np.array([
        [0], [1j]
    ], dtype=complex)

    assert np.allclose(state.state, expected)

    state = QuantumState(2)
    circuit = QuantumCircuit(2)
    circuit.add_Y_gate(0)
    circuit.update_quantum_state(state)

    expected = np.array([
        [0], [1j], [0], [0]
    ], dtype=complex)

    assert np.allclose(state.state, expected)

def test_Z_gate():
    state = QuantumState(1)
    circuit = QuantumCircuit(1)
    circuit.add_Z_gate(0)
    circuit.update_quantum_state(state) 

    expected = np.array([
        [1], [0]
    ], dtype=complex)

    assert np.allclose(state.state, expected)

    state = QuantumState(2)
    circuit = QuantumCircuit(2)
    circuit.add_Z_gate(0)
    circuit.update_quantum_state(state) 

    expected = np.array([
        [1], [0], [0], [0]
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

    state = QuantumState(2)
    circuit = QuantumCircuit(2)
    circuit.add_H_gate(0)
    circuit.update_quantum_state(state)

    expected = np.array([
        [1/np.sqrt(2)], [1/np.sqrt(2)], [0], [0]
    ], dtype=complex)

    assert np.allclose(state.state, expected)

def test_T_gate():
    state = QuantumState(1)
    circuit = QuantumCircuit(1)
    circuit.add_T_gate(0)
    circuit.update_quantum_state(state)

    expected = np.array([
        [1], [0]
    ], dtype=complex)

    assert np.allclose(state.state, expected)

    state = QuantumState(2)
    circuit = QuantumCircuit(2)
    circuit.add_T_gate(0)
    circuit.update_quantum_state(state)

    expected = np.array([
        [1], [0], [0], [0]
    ], dtype=complex)

    assert np.allclose(state.state, expected)

def test_RX_gate():
    theta = random.random()
    state = QuantumState(1)
    circuit = QuantumCircuit(1)
    circuit.add_RX_gate(0, theta=theta)
    circuit.update_quantum_state(state)

    expected = np.array([
        [np.cos(theta/2)], [-1j*np.sin(theta/2)]
    ], dtype=complex)

    assert np.allclose(state.state, expected)

def test_RY_gate():
    theta = random.random()
    state = QuantumState(1)
    circuit = QuantumCircuit(1)
    circuit.add_RY_gate(0, theta=theta)
    circuit.update_quantum_state(state)

    expected = np.array([
        [np.cos(theta/2)], [np.sin(theta/2)]
    ], dtype=complex)

    assert np.allclose(state.state, expected)

def test_RZ_gate():
    theta = random.random()
    state = QuantumState(1)
    circuit = QuantumCircuit(1)
    circuit.add_RZ_gate(0, theta=theta)
    circuit.update_quantum_state(state)

    expected = np.array([
        [np.exp(-1j*theta/2)], [0]
    ], dtype=complex)

    assert np.allclose(state.state, expected)