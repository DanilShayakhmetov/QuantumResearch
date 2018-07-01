from qiskit import QuantumProgram

# Checking the version of PYTHON;

import sys


def Grover():
    if sys.version_info < (3,5):
        raise Exception('Please use Python version 3.5 or greater.')

    #Create an object
    qp = QuantumProgram()
    backend = 'local_qasm_simulator'
    # backend = 'ibmqx4'
    max_credits = 15

    QX_TOKEN = "ee6100e19629678494bd4c9f4f0f3dc3038fe389b08eee456b8a8be280e08884f6b6228825afa60dda60bf7ee5995ce9e5ae6473f31137a0e94780669bce9707"
    QX_URL = "https://quantumexperience.ng.bluemix.net/api"

    # Set up the API and execute the program.

    # qp.set_api(QX_TOKEN, QX_URL)

    # quantum register for the circuit(3->5)
    q1 = qp.create_quantum_register('q1', 5)
    c1 = qp.create_classical_register('c1', 5)

    # making the circuit
    qc1 = qp.create_circuit('Grover', [q1], [c1])

    # line one
    qc1.x(q1[0])


    # line two
    qc1.h(q1[0])
    qc1.h(q1[1])
    qc1.h(q1[2])

    # line three
    qc1.x(q1[0])
    qc1.x(q1[1])

    # line four
    qc1.ccx(q1[2],q1[1],q1[0])

    qc1.x(q1[2])
    # qc1.x(q1[1])

    # line five
    qc1.h(q1[2])
    qc1.h(q1[1])

    # line six
    qc1.x(q1[2])
    qc1.x(q1[1])

    # line seven
    qc1.h(q1[1])

    # line eight
    qc1.cx(q1[2],q1[1])

    # line nine
    qc1.h(q1[1])

    # line ten
    qc1.x(q1[2])
    qc1.x(q1[1])

    # line eleven
    qc1.h(q1[0])
    qc1.h(q1[1])
    qc1.h(q1[2])

    # Measure
    for i in range(5):
        qc1.measure(q1[i], c1[i])

    # printing the circuits
    print(qp.get_qasm('Grover'))
    qobj = qp.compile('Grover', backend=backend, shots = 1000, max_credits = 15)
    qp.get_execution_list(qobj)
    qp.get_execution_list(qobj, verbose = True)
    qp.get_compiled_configuration(qobj, 'Grover')

    #new
    result = qp.execute('Grover', backend=backend, shots = 1000, max_credits = 15)


    #print result:
    print(qp.get_compiled_qasm(qobj, 'Grover'))

    #print info:
    #print(api.backend_status(backend))
    #print(api.backend_parameters(backend))

    #new
    # print(result)
    # print(result.get_data("Grover"))

    #Record information in text.txt(Create text.txt file in your repository)

    res = result.get_data("Grover")
    quasm = qp.get_qasm('Grover')
    b = ascii(res)
    c = ascii(quasm)
    with open('Fourth(111).txt', 'w') as ouf:
        ouf.write('\n'+b)

Grover()