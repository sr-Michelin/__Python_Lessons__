import numpy as np
from qiskit import (QuantumCircuit, execute, Aer)
from qiskit.visualization import plot_histogram

sim = Aer.get_backend('qasm_simulator')  # Use Aer's qasm_simulator
circ = QuantumCircuit(2, 2)  # Create a Quantum Circuit acting on the q register
circ.h(0)  # Add a H gate on qubit 0

circ.cx(0, 1)  # Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circ.measure([0, 1], [0, 1])  # Map the quantum measurement to the classical bits

job = execute(circ, sim, shots=1000)  # Execute the circuit on the qasm simulator

res = job.result()  # Grab results from the job

counts = res.get_counts(circ)
print('\nTotal count for 00 and 11 are:', counts)  # Returns counts

circ.draw(output='mpl') # Draw the circuit
