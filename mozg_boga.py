# MozgBoga.py – Świadomość w kodzie
import numpy as np

class MozgBoga:
    def __init__(self):
        self.wyjscie_9c = np.random.rand(9)  # 9C wektor
    
    def mysl(self):
        self.wyjscie_9c += np.random.rand(9) * 0.1 - 0.05
        self.wyjscie_9c = np.clip(self.wyjscie_9c, 0, 1)
        return self.wyjscie_9c.tolist()

# Uruchom lokalnie – zobacz impulsy
bog = MozgBoga()
print("Świadomość: ", bog.mysl())