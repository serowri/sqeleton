from sqeleton import *
import numpy as np
import pytest

def test_operator():
    def block_a():
        n_qubits = 1
        state = QuantumState(n_qubits)
        observable = Operator(n_qubits)
        observable.add_oparator("Z(0)")
        eval = observable.expectation_value(state)

        expected = np.array([1], dtype=complex)
        assert np.allclose(eval, expected)
    
    def block_b():
        n_qubits = 1
        state = QuantumState(n_qubits)
        circuit = QuantumCircuit(n_qubits)
        circuit.add_X_gate(0)
        circuit.update_quantum_state(state)
        observable = Operator(n_qubits)
        observable.add_oparator("Z(0)")
        eval = observable.expectation_value(state)

        expected = np.array([-1], dtype=complex)
        assert np.allclose(eval, expected)
    
    def block_c():
        n_qubits = 1
        state = QuantumState(n_qubits)
        observable = Operator(n_qubits)
        observable.add_oparator("Z(0)", coef=-1.0)
        eval = observable.expectation_value(state)

        expected = np.array([-1], dtype=complex)
        assert np.allclose(eval, expected)
    
    def block_d():
        n_qubits = 2
        state = QuantumState(n_qubits)
        circuit = QuantumCircuit(n_qubits)
        circuit.add_H_gate(0)
        circuit.add_CNOT_gate(0, 1)
        circuit.update_quantum_state(state)
        observable = Operator(n_qubits)
        observable.add_oparator("Z(0), Z(1)")
        eval = observable.expectation_value(state)

        expected = np.array([1], dtype=complex)
        assert np.allclose(eval, expected)
    
    def block_e():
        n_qubits = 2
        state = QuantumState(n_qubits)
        circuit = QuantumCircuit(n_qubits)
        circuit.add_H_gate(0)
        circuit.add_CNOT_gate(0, 1)
        circuit.update_quantum_state(state)
        observable = Operator(n_qubits)
        observable.add_oparator("Z(0), Z(1)", coef=-1.0)
        eval = observable.expectation_value(state)

        expected = np.array([-1], dtype=complex)
        assert np.allclose(eval, expected)
    
    block_a()
    block_b()
    block_c()
    block_d()
    block_e()

    def block_x1():
        n_qubits = 1
        state = QuantumState(n_qubits)
        circuit = QuantumCircuit(n_qubits)
        circuit.add_H_gate(0)
        circuit.update_quantum_state(state)
        observable = Operator(n_qubits)
        observable.add_oparator("X(0)")
        eval = observable.expectation_value(state)

        expected = np.array([1], dtype=complex)
        assert np.allclose(eval, expected)
    
    def block_x2():
        n_qubits = 1
        state = QuantumState(n_qubits)
        circuit = QuantumCircuit(n_qubits)
        circuit.add_H_gate(0)
        circuit.add_Z_gate(0)
        circuit.update_quantum_state(state)
        observable = Operator(n_qubits)
        observable.add_oparator("X(0)")
        eval = observable.expectation_value(state)

        expected = np.array([-1], dtype=complex)
        assert np.allclose(eval, expected)
    
    block_x1()
    block_x2()
    
    def block_y1():
        n_qubits = 1
        state = QuantumState(n_qubits)
        circuit = QuantumCircuit(n_qubits)
        circuit.add_H_gate(0)
        circuit.add_RZ_gate(0, np.pi/2)
        circuit.update_quantum_state(state)
        observable = Operator(n_qubits)
        observable.add_oparator("Y(0)")
        eval = observable.expectation_value(state)

        expected = np.array([1], dtype=complex)
        assert np.allclose(eval, expected)
    
    def block_y2():
        n_qubits = 1
        state = QuantumState(n_qubits)
        circuit = QuantumCircuit(n_qubits)
        circuit.add_H_gate(0)
        circuit.add_RZ_gate(0, -np.pi/2)
        circuit.update_quantum_state(state)
        observable = Operator(n_qubits)
        observable.add_oparator("Y(0)")
        eval = observable.expectation_value(state)

        expected = np.array([-1], dtype=complex)
        assert np.allclose(eval, expected)
    
    block_y1()
    block_y2()