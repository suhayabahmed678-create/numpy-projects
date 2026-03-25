import numpy as np
from pathlib import Path
from datetime import datetime


class SmartSyntheticLap:
    def __init__(self , rows=100 , cols=3 , dist="normal"):
        self.rows = rows
        self.cols = cols
        self.dist = dist.lower()
        self.data = None


# Distribution Generator
    def _make_data(self):
        distributions =({
            "normal": lambda: np.random.normal(0, 1, (self.rows, self.cols)),
            "uniform": lambda: np.random.uniform(0, 1, (self.rows, self.cols)),
            "integers": lambda: np.random.randint(0, 100, (self.rows, self.cols)),
        })
        if self.dist not in distributions:
            raise ValueError("Invalid distribution type")
        return distributions[self.dist]()


    def scale(self):
        mn = self.data.min(axis=0)
        mx = self.data.max(axis=0)
        self.data = (self.data - mn) / (mx - mn + 1e-9)

    def generate(self, scale=False):
        print("⚙ Generating data...")
        self.data = self._make_data()

        if scale:
            self.scale()

        return self.data

    # Quick Summary
    def summary(self):
        print("\n dataset summary")
        print("shape:" , self.data.shape)
        print("min  :" , np.mean(self.data, axis=0))
        print("std  :" , np.std(self.data, axis=0))

    # Save
    def save(self):
        filename = f"synthetic_{self.dist}_{datetime.now().strftime('%H%M%S')}.csv"
        path = Path(filename)
        np.savetxt(path, self.data, delimiter=",", fmt="%.4f")
        print("saved as:", filename)

# Runner
def run ():
    print("🧪 Smart Synthetic Lab\n")
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))
    dist = input("Distribution (normal, uniform, integers): ").lower()

    lab = SmartSyntheticLap(rows, cols, dist)

    try:
        lab.generate(scale=input("scale 0-1?(y/n):").lower()=="y")
        print("\nPreview:\n", lab.data[:5])
        lab.summary()

        if input("\nSave file? (y/n): ").lower() == "y":
            lab.save()

    except Exception as e:
        print("Error " ,e)


if __name__ == "__main__":
    run()

