import numpy as np

def create_Uf():
    # Step 1: Get number of input bits
    n = int(input("Enter number of input bits (e.g. 2, 3, 4): "))
    m = int(input("Enter number of output bits: "))

    # Step 2: Matrix size
    total_qubits = n + m
    dim = 2 ** total_qubits
    Uf = np.zeros((dim, dim), dtype=int)

    # Step 3: Ask for mapping
    mapping = {}
    for i in range(2**n):
        x = format(i, f'0{n}b')  
        fx = input(f"Enter output for input {x} (as {m}-bit string): ")
        mapping[x] = fx

    # Step 4: Construct Uf
    for x_int in range(2**n):
        x_bits = format(x_int, f'0{n}b')

        for y_int in range(2**m):
            y_bits = format(y_int, f'0{m}b')

            fx_bits = mapping[x_bits]
            new_y = int(y_bits, 2) ^ int(fx_bits, 2)


            in_state = (x_int << m) | y_int
            out_state = (x_int << m) | new_y

            Uf[out_state, in_state] = 1

    return Uf




def main():
    matrix = create_Uf()
    print("Transformation Matrix:")
    print(matrix)

if __name__ == "__main__":
    main()