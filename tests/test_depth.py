from sqeleton import *
import numpy as np

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