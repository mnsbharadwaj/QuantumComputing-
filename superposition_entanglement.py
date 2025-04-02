# Importing necessary libraries from Qiskit
from qiskit import QuantumCircuit, Aer, execute

# Step 1: Create a quantum circuit with 2 qubits and 2 classical bits for measurement
qc = QuantumCircuit(2, 2)

# Step 2: Create a superposition on the first qubit using the Hadamard gate
qc.h(0)  # Apply the Hadamard gate to the first qubit (qubit 0)

# Step 3: Create entanglement using the CNOT gate (controlled-NOT) between qubit 0 and qubit 1
qc.cx(0, 1)  # CNOT gate, control qubit 0, target qubit 1

# Step 4: Measure the qubits and store the result in the classical bits
qc.measure([0, 1], [0, 1])

# Step 5: Simulate the quantum circuit using the Aer simulator
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1000).result()

# Step 6: Get and print the results
counts = result.get_counts(qc)
print("Measurement results:", counts)
