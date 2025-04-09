from qiskit import QuantumRegister, QuantumCircuit

def xnor_grouping_overlap(circuit, qubits):
    #-------------Grouping---------
    # Aplicar Toffoli com controle nos dois primeiros qubits e alvo no quinto qubit
    circuit.ccx(qubits[0], qubits[1], qubits[4])
    
    # Aplicar a porta Toffoli com controle nos qubits[2] e qubits[3], e alvo no qubits[5]
    circuit.ccx(qubits[2], qubits[3], qubits[5])
    
    # Aplicar a porta Toffoli com controle nos qubits[4] e qubits[5], e alvo no qubits[6]
    circuit.ccx(qubits[4], qubits[5], qubits[6])

    # Aplicar a porta NOT no sétimo qubit (qubits[6])
    circuit.x(qubits[6])
    #circuit.barrier()


    #-------------Overlap---------
    # Aplicar a porta NOT no primeiro qubit (qubits[1])
    circuit.x(0)
    # Aplicar a porta NOT no segundo qubit (qubits[0])
    circuit.x(1)

    # Aplicar a porta Toffoli com controle nos qubits[0] e qubits[1], e alvo no qubits[7]
    circuit.ccx(0, 1, 7)

    # Aplicar a porta NOT no primeiro qubit (qubits[1])
    circuit.x(0)
    # Aplicar a porta NOT no segundo qubit (qubits[0])
    circuit.x(1)
    #circuit.barrier()

    # Aplicar a porta NOT no terceiro qubit (qubits[2])
    circuit.x(2)
    # Aplicar a porta NOT no quarto qubit (qubits[3])
    circuit.x(3)

    # Aplicar a porta Toffoli com controle nos qubits[2] e qubits[3], e alvo no qubits[8]
    circuit.ccx(2, 3, 8)

    # Aplicar a porta NOT no terceiro qubit (qubits[2])
    circuit.x(2)
    # Aplicar a porta NOT no quarto qubit (qubits[3])
    circuit.x(3)
    #circuit.barrier()

    # Aplicar a porta Toffoli com controle nos qubits[7] e qubits[8], e alvo no qubits[9]
    circuit.ccx(7, 8, 9)
    #circuit.barrier()


    #-------------DIF----------------
    # Aplicar a porta NOT no décimo qubit (qubits[10])
    circuit.x(9)

    # Aplicar a porta Toffoli com controle nos qubits[6] e qubits[9], e alvo no qubits[10]
    circuit.ccx(6, 9, 10)

    # Aplicar a porta NOT no décimo primeiro qubit (qubits[10])
    circuit.x(10)