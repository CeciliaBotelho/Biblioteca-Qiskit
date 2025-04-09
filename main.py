from qiskit import QuantumCircuit
import numpy as np
import matplotlib.pyplot as plt
from qiskit.qasm3 import dump

from portas_quanticas.funcao_pertinencia import inicializa_circuito_com_probabilidades
from portas_quanticas.t_norma import toffoli_circuit_interactive
from portas_quanticas.t_conorma import apply_or_fuzzy_generic
from portas_quanticas.dif import diff_fuzzy
from portas_quanticas.grouping import add_grouping_function
from portas_quanticas.xor import add_xor_fuzzy
from portas_quanticas.overlap import overlap_function
from portas_quanticas.implicacaoSN import implication
from portas_quanticas.ql import ql_implication
from portas_quanticas.xor_ominus import xor_ominus
from portas_quanticas.xor_otimes import xor_otimes
from portas_quanticas.xor_oplus import xor_oplus
from portas_quanticas.xor_grouping_overlap import xor_grouping_overlap
from portas_quanticas.xnor_grouping_overlap import xnor_grouping_overlap
from portas_quanticas.medirqubits import medir_qubits

def mostrar_menu():
    print("Selecione a porta quântica desejada:")
    print("1: T Norma do Produto (equivalente à porta Toffoli)")
    print("2: Aplicar operação OR fuzzy")
    print("3: Aplicar operação de Diferença Fuzzy")
    print("4: Aplicar função de Grouping")
    print("5: Aplicar XOR Fuzzy")
    print("6: Aplicar função de Overlap")  
    print("7: Aplicar função de Implicação (S, N)")  
    print("8: Aplicar XOR Fuzzy ominus")
    print("9: Aplicar XOR Fuzzy otimes")
    print("10: Aplicar XOR Fuzzy oplus")
    print("11: Aplicar função de Implicação (QL)")
    print("12: Aplicar XOR Fuzzy Grouping Overlap")
    print("13: Aplicar XNOR Fuzzy Grouping Overlap")
    print("14: Realizar medição")
    print("0: Sair")
    escolha = input("Digite o número da sua escolha e pressione Enter: ")
    return escolha

def get_qubit_indices():
    control_qubits = list(map(int, input("Digite os índices dos qubits de controle, separados por espaço (começando de 0): ").split()))
    target_qubits = list(map(int, input("Digite os índices dos qubits alvo, separados por espaço (começando de 0): ").split()))
    aux_qubits = list(map(int, input("Digite os índices dos qubits auxiliares, separados por espaço (começando de 0): ").split()))
    return control_qubits, target_qubits, aux_qubits

def salvar_circuito_qasm(circuito):
    with open("circuito.qasm", "w") as file:
        dump(circuito, file)  # Salva em formato QASM 3
    print("Circuito salvo em 'circuito.qasm' para IBM Quantum Experience.")

def mostrar_circuito(circuito):
    circuito.draw(output='mpl')
    plt.show()

def main():
    num_qubits = int(input("Quantos qubits você quer no circuito? "))
    probabilidades = [float(x) for x in input("Digite as probabilidades para cada qubit, separadas por espaço: ").split()]

    my_circuit = inicializa_circuito_com_probabilidades(num_qubits, probabilidades)
    if my_circuit is None:
        return

    while True:

        escolha = mostrar_menu()
        if escolha == '1':
            toffoli_circuit_interactive(my_circuit)
            print("Desenhando o circuito:")
        elif escolha == '2':
            control_indices = list(map(int, input("Digite os índices dos qubits de controle, separados por espaço (começando de 0): ").split()))
            target_index = int(input("Digite o índice do qubit alvo para a operação OR fuzzy: "))
            apply_or_fuzzy_generic(my_circuit, control_indices, target_index)
            print("Circuito com operação OR fuzzy aplicada:")
        elif escolha == '3':
            qubit1 = int(input("Digite o índice do primeiro qubit para DIF: "))
            qubit2 = int(input("Digite o índice do segundo qubit para DIF: "))
            aux_qubit = int(input("Digite o índice do qubit auxiliar para DIF: "))
            diff_fuzzy(my_circuit, qubit1, qubit2, aux_qubit)
            print("Circuito com operação de Diferença Fuzzy aplicada:")
        elif escolha == '4':  # Adicionando a nova operação de Grouping
            qubit_indices = list(map(int, input("Digite os índices de todos os qubits para Grouping, separados por espaço: ").split()))
            add_grouping_function(my_circuit, qubit_indices)
            print("Circuito com função de Grouping aplicada:")
        elif escolha == '5':  # Chamada para a função XOR Fuzzy
            add_xor_fuzzy(my_circuit)
            print("Circuito com XOR Fuzzy aplicado:")
        elif escolha == '6':  # Opção para Overlap
            if num_qubits < 7:
                print("O número mínimo de qubits para utilizar a opção Overlap é 7.")
            else:
                selected_qubits = list(map(int, input("Digite os índices de 7 qubits para Overlap, separados por espaço (começando de 0): ").split()))
                if len(selected_qubits) != 7:
                    print("Erro: Você deve selecionar exatamente 7 qubits.")
                else:
                    overlap_function(my_circuit, selected_qubits)
                    print("Circuito com Overlap aplicado:")

        elif escolha == '7':  # Implementação da chamada para a função de Implicação (S, N)
            control_qubit = int(input("Digite o índice do qubit de controle (premissa da implicação): "))
            input_qubit = int(input("Digite o índice do qubit de entrada para a operação fuzzy: "))
            target_qubit = int(input("Digite o índice do qubit alvo: "))

            # Verificar se os índices inseridos são válidos
            if control_qubit == input_qubit or control_qubit == target_qubit or input_qubit == target_qubit:
                print("Erro: Os qubits devem ser diferentes entre si.")
            elif max(control_qubit, input_qubit, target_qubit) >= num_qubits:
                print("Erro: Índice de qubit inválido. Certifique-se de que os índices estão dentro do número de qubits do circuito.")
            else:
                # Aplicar a operação de implicação fuzzy no circuito
                implication(my_circuit, control_qubit, input_qubit, target_qubit)
                
                # Adicionar uma barreira para melhor visualização do circuito
                my_circuit.barrier()
                
                print("Circuito com função de Implicação (S, N) aplicada:")

        elif escolha == '8':  # Opção para XOR Fuzzy ôminus
            if num_qubits < 5:
                print("O número mínimo de qubits para utilizar a opção XOR ôminus é 5.")
                continue
            selected_qubits = list(map(int, input("Digite os índices de 5 qubits para o circuito XOR ôminus, separados por espaço (começando de 0): ").split()))
            if len(selected_qubits) != 5:
                print("Erro: Você deve selecionar exatamente 5 qubits.")
                continue
            xor_ominus(my_circuit, selected_qubits)
            print("Circuito com XOR Fuzzy ôminus aplicado:")

        elif escolha == '9':  # Opção para XOR Fuzzy ôtimes
            if num_qubits < 7:
                print("O número mínimo de qubits para utilizar a opção XOR ôtimes é 7.")
            else:
                selected_qubits = list(map(int, input("Digite os índices de 7 qubits para o circuito XOR ôtimes, separados por espaço (começando de 0): ").split()))
                if len(selected_qubits) != 7:
                    print("Erro: Você deve selecionar exatamente 7 qubits.")
                else:
                    xor_otimes(my_circuit, selected_qubits)
                    print("Circuito com XOR Fuzzy ôtimes aplicado:")

        elif escolha == '10':  # Opção para XOR Fuzzy ôplus
            if num_qubits < 7:
                print("O número mínimo de qubits para utilizar a opção XOR ôplus é 7.")
            else:
                selected_qubits = list(map(int, input("Digite os índices de 7 qubits para o circuito XOR ôplus, separados por espaço (começando de 0): ").split()))
                if len(selected_qubits) != 7:
                    print("Erro: Você deve selecionar exatamente 7 qubits.")
                else:
                    xor_oplus(my_circuit, selected_qubits)
                    print("Circuito com XOR Fuzzy ôplus aplicado:")
        
        elif escolha == '11':  # Implementação da chamada para a função de Implicação QL
            control_qubit1 = int(input("Digite o índice do primeiro qubit de controle para IMP: "))
            control_qubit2 = int(input("Digite o índice do segundo qubit de controle para IMP: "))
            target_qubit = int(input("Digite o índice do qubit alvo para IMP: "))
            aux_qubit1 = int(input("Digite o índice do primeiro qubit auxiliar para IMP: "))
            aux_qubit2 = int(input("Digite o índice do segundo qubit auxiliar para IMP: "))
            ql_implication(my_circuit, control_qubit1, control_qubit2, target_qubit, aux_qubit1, aux_qubit2)
            print("Circuito com função de Implicação QL aplicada:")

        elif escolha == '12':  # Implementação da chamada para a função de XOR G O
            if num_qubits < 11:
                print("O número mínimo de qubits para utilizar a opção XOR Grouping Overlap é 11.")
            else:
                selected_qubits = list(map(int, input("Digite os índices de 11 qubits para o circuito XOR Grouping Overlap, separados por espaço (começando de 0): ").split()))
                if len(selected_qubits) != 11:
                    print("Erro: Você deve selecionar exatamente 11 qubits.")
                else:
                    xor_grouping_overlap(my_circuit, selected_qubits)
                    print("Circuito com XOR Fuzzy ôplus aplicado:")

        elif escolha == '13':  # Implementação da chamada para a função de XNOR G O
            if num_qubits < 11:
                print("O número mínimo de qubits para utilizar a opção XNOR Grouping Overlap é 11")
            else:
                selected_qubits = list(map(int, input("Digite os índices de 11 qubits para o circuito XNOR Grouping Overlap, separados por espaço (começando de 0): ").split()))
                if len(selected_qubits) != 11:
                    print("Erro: Você deve selecionar exatamente 11 qubits.")
                else:
                    xnor_grouping_overlap(my_circuit, selected_qubits)
                    print("Circuito com XOR Fuzzy ôplus aplicado:")

        elif escolha == '14':  # Opção para medir qubits e exibir histograma
            medir_qubits(my_circuit)

        elif escolha == '0':
            salvar_circuito_qasm(my_circuit)  # Salvar o circuito antes de sair
            print("Saindo do programa.")
            break

        else:
            print("Escolha inválida. Por favor, tente novamente.")

        # Adiciona a barreira após cada operação
        my_circuit.barrier()


        print("Circuito atualizado:")
        print(my_circuit.draw('text'))  # Impressão em texto (ASCII)
        mostrar_circuito(my_circuit)    # Exibição visual usando Matplotlib


if __name__ == "__main__":
    main()
