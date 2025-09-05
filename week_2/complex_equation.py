import matplotlib.pyplot as plt

def plot_complex_numbers(c1, c2, result ):
    numbers = [c1, c2, result]
    labels = [c1, c2, result]
    colors = ['blue', 'green', 'red']

    plt.figure(figsize=(6, 6))


    for num, label, color in zip(numbers, labels, colors):
        plt.arrow(0, 0, num.real, num.imag,
                head_width=0.2, head_length=0.3, fc=color, ec=color)
        plt.text( num.real + 0.2, num.imag + 0.2, f"{label} = {num}", fontsize=10, color=color)

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel("Real part")
    plt.ylabel("Imaginary part")
    plt.title("Complex Numbers on the Complex Plane")
    plt.grid(True)
    plt.axis('equal')
    plt.show()
    
def main():
    loop_exit = True    
    while loop_exit:
        c1 = input("Enter a complex number one (e.g., 3+4i): ").replace('i', 'j')
        equation_c1 = complex(c1)

        c2 = input("Enter another complex number two (e.g., 1+2i): ").replace('i', 'j')
        equation_c2 = complex(c2)
        print("")

        user_input = input("Enter which operation to perform 1 : add, 2: subtract, 3: multiply or 4: exit): ")
        print("")


        if user_input == '1':
            result = equation_c1 + equation_c2
            print("c1 = ", equation_c1)
            print("c2 = ", equation_c2)
            print("c1 + c2 = ", result)
            print("")
            plot_complex_numbers(equation_c1, equation_c2, result)
            print("")

        elif user_input == '2':
            result = equation_c1 - equation_c2
            print("c1 = ", equation_c1)
            print("c2 = ", equation_c2)
            print("c1 - c2 = ", result)
            print("")
            plot_complex_numbers(equation_c1, equation_c2, result)
            print("")

        elif user_input == '3':
            result = equation_c1 * equation_c2
            print("c1 = ", equation_c1)
            print("c2 = ", equation_c2)
            print("c1 * c2 = ", result)
            print("")
            plot_complex_numbers(equation_c1, equation_c2, result)
            print("")

        elif user_input == '4':
            print("Exiting the program.")
            loop_exit = False

        else:
            print("Invalid operation selected. Please choose 1 : add, 2: subtract or 3: multiply")

if __name__ == "__main__":
    main()