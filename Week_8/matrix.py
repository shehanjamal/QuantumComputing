import numpy as np

def create_matrix(num_inputs, num_outputs, out_for_0, out_for_1):
    """
    Build a transformation matrix for a custom logic gate.
    
    Args:
        num_inputs (int): number of input qubits
        num_outputs (int): number of output qubits
        out_for_0 (int): output when input is 0
        out_for_1 (int): output when input is 1
    """
    # Total possible states
    input_states = 2 ** num_inputs
    output_states = 2 ** num_outputs
    
    # Initialize matrix with zeros
    matrix = np.zeros((output_states, input_states), dtype=int)
    
    # For each input state, assign the mapping
    for i in range(input_states):
        # Decide what the output is based on the "last bit"
        last_bit = i % 2
        if last_bit == 0:
            out = out_for_0
        else:
            out = out_for_1
        
        # Place 1 at the appropriate location in the matrix
        if out < output_states:
            matrix[out, i] = 1
    
    return matrix


def main():
    num_inputs = int(input("Enter number of inputs: "))
    num_outputs = int(input("Enter number of outputs: "))
    out_for_0 = int(input("When input is 0, what should the output be? "))
    out_for_1 = int(input("When input is 1, what should the output be? "))

    matrix = create_matrix(num_inputs, num_outputs, out_for_0, out_for_1)
    print("Transformation Matrix:")
    print(matrix)

if __name__ == "__main__":
    main()