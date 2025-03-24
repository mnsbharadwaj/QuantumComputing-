from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1, 1)
qc.h(0)  # Apply Hadamard gate to put qubit in superposition
qc.measure(0, 0)  # Measure the qubit

# Simulate the circuit
simulator = Aer.get_backend('aer_simulator')
task = execute(qc, simulator, shots=1024)
result = task.result()
outcome = result.get_counts()

# Display results
plot_histogram(outcome)
plt.show()

# Creating an entangled state (Bell pair)
bell_circuit = QuantumCircuit(2, 2)
bell_circuit.h(0)  # Put qubit 0 into superposition
bell_circuit.cx(0, 1)  # Entangle qubit 0 and 1
bell_circuit.measure([0,1], [0,1])  # Measure both qubits

# Simulate entangled state
task2 = execute(bell_circuit, simulator, shots=1024)
result2 = task2.result()
outcome2 = result2.get_counts()

# Display entanglement results
plot_histogram(outcome2)
plt.show()