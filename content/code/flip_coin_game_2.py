from qiskit import QuantumCircuit
from qiskit import IBMQ
from qiskit.compiler import transpile, assemble

tosses = 75
qc_list = []


def input_guess():
    guess = str(input("What's your guess heads/tails? [h/t]: ")).lower().strip()
    try:
        if guess[0] in ('h', 't'):
            return guess[0]
        else:
            print('Invalid Input')
            return input_guess()
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return input_guess()


def main():
    # Authenticate an account and add for use during this session. Replace string
    # argument with your private token.
    IBMQ.load_account()

    """Asks for guess"""
    guess = input_guess()
    heads = 0
    tails = 0

    qc = QuantumCircuit(1)  # quantum circuit with one qubit
    qc.h(0)  # applying Hadamard gate
    qc.measure_all()

    # After creating qc_list
    provider = IBMQ.get_provider(group='open')
    backend = provider.get_backend('ibmq_essex')
    transpiled_circs = transpile(qc, backend=backend)
    qobjs = assemble(transpiled_circs, backend=backend, shots=tosses)
    job_info = backend.run(qobjs)

    # To get the results
    result = job_info.result().get_counts()
    heads = result['0']
    tails = result['1']

    if (guess == 'h' and heads > tails) or (guess == 't' and tails > heads):
        msg = 'You WON!'
    else:
        msg = 'You LOST!'

    print('{}\nThe experiment resulted in: {} heads and {} tails.'
          .format(msg, heads, tails))


main()
