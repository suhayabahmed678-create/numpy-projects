#smart Matrix Toolkit
import numpy as np

class MatrixBuilder:
    @staticmethod
    def from_input(name="Matrix"):
        r = int (input(f"{name}: rows"))
        c = int (input(f"{name}: cols"))
        print(f"Enter {r*c} values (space separated):")
        values = list(map(float , input("> ").split()))
        return np.array(values).reshape(r, c)



class MatrixBrain:
    def __init__(self, mat: np.ndarray ):
        self.m = mat

    def show(self, title="Matrix"):
        print(f"\n 📦{title}\n {self.m}")

    def Transpose(self):
        return self.m.T

    def determinant(self):
        if self.m.shape[0] != self.m.shape[1]:
            return None
        return float(np.linalg.det(self.m))

    def inverse(self):
        if self.m.shape[0] != self.m.shape[1]:
            return None
        try :
            return np.linalg.inv(self.m)
        except np.linalg.LinAlgError:
            return None

    def rank(self):
        return int(np.linalg.matrix_rank(self.m))


class MatrixOps:
    @staticmethod
    def add(a, b):
        if a.shape != b.shape:
            return None
        return a + b

    @staticmethod
    def multiply(a, b):
        if a.shape[1] != b.shape[0]:
            return None
        return a @ b


def menu():
    print("""
🧠 Smart Matrix Toolkit
1 → Add matrices
2 → Multiply matrices
3 → Transpose
4 → Determinant
5 → Inverse
6 → Rank
0 → Exit
""")

def run():
    while True:
        menu()
        choice = input("choose: ")

        if choice == "0":
            print("bye")
            break

        if choice in {"1","2"}:
            A = MatrixBuilder.from_input("Matrix A")
            B = MatrixBuilder.from_input("Matrix B")

            if choice == "1":
                res = MatrixOps.add(A, B)
                print("\n Result:\n ", res if res is not None else "shape mismatch")

            else:
                res = MatrixOps.multiply(A, B)
                print("\n Result:\n ", res if res is not None else "shape mismatch")

        else:
            A = MatrixBuilder.from_input("Matrix A")
            brain = MatrixBrain(A)
            brain.show()

            if choice == "3":
                print("\nTranspose:\n",brain.Transpose())

            elif choice == "4":
                d = brain.determinant()
                print("\nDeterminant:\n",d if d is not None else "shape mismatch")

            elif choice == "5":
                inv = brain.inverse()
                print("\nInverse:\n",inv if inv is not None else "shape mismatch")

            elif choice == "6":
                print("\nRank",brain.rank())

if __name__ == "__main__":
    run()

