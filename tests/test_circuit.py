from sqeleton import *
import numpy as np
import random

#--------------------------------------------------#
# gate tests

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

#--------------------------------------------------#
# get_depth() tests

def test_zero_depth():
    circuit = QuantumCircuit(3)
    depth = circuit.get_depth()

    expected = 0

    assert depth == expected

def test_one_depth():
    circuit_a = QuantumCircuit(3)
    circuit_a.add_CNOT_gate(0, 1)
    depth_a = circuit_a.get_depth()
    expected_a = 1

    assert depth_a == expected_a

    circuit_b = QuantumCircuit(3)
    circuit_b.add_H_gate(1)
    circuit_b.add_CNOT_gate(0, 2)
    depth_b = circuit_b.get_depth()
    expected_b = 1

    assert depth_b == expected_b

    circuit_c = QuantumCircuit(3)
    circuit_c.add_X_gate(0)
    circuit_c.add_Y_gate(1)
    circuit_c.add_Z_gate(2)
    depth_c = circuit_c.get_depth()
    expected_c = 1

    assert depth_c == expected_c

def test_depth():
    circuit = QuantumCircuit(3)
    circuit.add_H_gate(0)
    circuit.add_H_gate(0)
    circuit.add_H_gate(0)
    circuit.add_H_gate(0)
    circuit.add_H_gate(0)
    circuit.add_H_gate(0)
    circuit.add_H_gate(1)
    circuit.add_CNOT_gate(2, 1)
    depth = circuit.get_depth()
    expected = 6

    assert depth == expected
