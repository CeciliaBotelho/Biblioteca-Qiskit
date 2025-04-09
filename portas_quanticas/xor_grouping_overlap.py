from qiskit import QuantumRegister, QuantumCircuit

def xor_grouping_overlap(circuit, qubits):
    #-------------Grouping---------
    # Aplicar a porta NOT no primeiro qubit (qubits[0])
    circuit.x(qubits[0])
    # Aplicar a porta NOT no segundo qubit (qubits[1])
    circuit.x(qubits[1])

    # Aplicar a porta Toffoli com controle nos qubits[0] e qubits[1], e alvo no qubits[4]
    circuit.ccx(qubits[0], qubits[1], qubits[4])

    # Aplicar a porta NOT no primeiro qubit (qubits[0])
    circuit.x(qubits[0])
    # Aplicar a porta NOT no segundo qubit (qubits[1])
    circuit.x(qubits[1])
    #circuit.barrier()

    # Aplicar a porta NOT no terceiro qubit (qubits[2])
    circuit.x(qubits[2])
    # Aplicar a porta NOT no quarto qubit (qubits[3])
    circuit.x(qubits[3])

    # Aplicar a porta Toffoli com controle nos qubits[2] e qubits[3], e alvo no qubits[5]
    circuit.ccx(qubits[2], qubits[3], qubits[5])

    # Aplicar a porta NOT no terceiro qubit (qubits[2])
    circuit.x(qubits[2])
    # Aplicar a porta NOT no quarto qubit (qubits[3])
    circuit.x(qubits[3])
    #circuit.barrier()

    # Aplicar a porta Toffoli com controle nos qubits[4] e qubits[5], e alvo no qubits[6]
    circuit.ccx(qubits[4], qubits[5], qubits[6])
    # Aplicar a porta NOT no sétimo qubit (qubits[6])
    circuit.x(qubits[6])
    #circuit.barrier()


    #-------------Overlap---------
    # Aplicar a porta Toffoli com controle nos qubits[0] e qubits[1], e alvo no qubits[7]
    circuit.ccx(qubits[0], qubits[1], qubits[7])
    # Aplicar a porta Toffoli com controle nos qubits[2] e qubits[3], e alvo no qubits[8]
    circuit.ccx(qubits[2], qubits[3], qubits[8])
    # Aplicar a porta Toffoli com controle nos qubits[7] e qubits[8], e alvo no qubits[9]
    circuit.ccx(qubits[7], qubits[8], qubits[9])
    #circuit.barrier()


    #-------------DIF----------------
    # Aplicar a porta NOT no décimo qubit (qubits[9])
    circuit.x(qubits[9])

    # Aplicar a porta Toffoli com controle nos qubits[6] e qubits[9], e alvo no qubits[10]
    circuit.ccx(qubits[6], qubits[9], qubits[10])