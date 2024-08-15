import sys

if len(sys.argv) < 3 or sys.argv != float or sys.argv != int:
    print("Dois numeros caralho!")
    sys.exit()

def soma():

    n1 = float(sys.argv[1])
    n2 = float(sys.argv[2])
    print(f"Soma: {n1+n2}")

if __name__ == "__main__":
    print(soma())