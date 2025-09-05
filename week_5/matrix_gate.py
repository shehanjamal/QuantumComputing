def main():
    menu = True
    while menu:
        input_matrix = input("Enter 1 for hardamands matrix, enter 2 for swap gate matrix and 3 for exit: ")
        if input_matrix == '1':
            import numpy as np
            H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])
            print("Hardamard's Matrix:")
            print(H)

        elif input_matrix == '2':
            import numpy as np
            S = np.array([
                    [1, 0, 0, 0],
                    [0, 0, 1, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 1]
                ])       
            print("Swap Gate Matrix:")
            print(S)

        elif input_matrix == '3':
            print("Exiting the program.")
            menu = False

        else:
            print("Invalid input. Please enter 1 or 2.")

        print("")
if __name__ == "__main__":
    main()