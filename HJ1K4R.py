from abc import ABC, abstractmethod

# --- Absztrakt Járat osztály ---
class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self):
        pass

# --- BelföldiJarat ---
class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_tipus(self):
        return "Belföldi"

# --- NemzetkoziJarat ---
class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_tipus(self):
        return "Nemzetközi"

# --- JegyFoglalas ---
class JegyFoglalas:
    def __init__(self, utas_nev, jarat):
        self.utas_nev = utas_nev
        self.jarat = jarat

    def __str__(self):
        return f"{self.utas_nev} - {self.jarat.jaratszam} ({self.jarat.jarat_tipus()}, {self.jarat.celallomas}, {self.jarat.jegyar} Ft)"

# --- LégiTársaság ---
class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def jarat_hozzaadas(self, jarat):
        self.jaratok.append(jarat)

    def foglalas(self, utas_nev, jaratszam):
        jarat = next((j for j in self.jaratok if j.jaratszam == jaratszam), None)
        if jarat:
            foglalas = JegyFoglalas(utas_nev, jarat)
            self.foglalasok.append(foglalas)
            return foglalas
        else:
            raise ValueError("Nem létező járatszám!")

    def lemondas(self, utas_nev, jaratszam):
        for f in self.foglalasok:
            if f.utas_nev == utas_nev and f.jarat.jaratszam == jaratszam:
                self.foglalasok.remove(f)
                return True
        raise ValueError("Foglalás nem található!")

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincs aktív foglalás.")
        for f in self.foglalasok:
            print(f)

# --- Példányosítás és előkészítés ---
def elokeszites():
    lt = LegiTarsasag("SkyFly")
    # Járatok
    lt.jarat_hozzaadas(BelfoldiJarat("B101", "Debrecen", 12000))
    lt.jarat_hozzaadas(NemzetkoziJarat("N202", "London", 45000))
    lt.jarat_hozzaadas(NemzetkoziJarat("N303", "Párizs", 42000))
    # Foglalások
    lt.foglalas("Kovács Anna", "B101")
    lt.foglalas("Nagy Péter", "N202")
    lt.foglalas("Kiss Judit", "N303")
    lt.foglalas("Szabó László", "B101")
    lt.foglalas("Tóth Gábor", "N202")
    lt.foglalas("Varga Eszter", "N303")
    return lt

# --- Egyszerű CLI ---
def main():
    lt = elokeszites()
    while True:
        print("\n1. Foglalás\n2. Lemondás\n3. Foglalások listázása\n4. Kilépés")
        valasztas = input("Válassz műveletet: ")
        if valasztas == "1":
            nev = input("Utas neve: ")
            jaratszam = input("Járatszám: ")
            try:
                foglalas = lt.foglalas(nev, jaratszam)
                print(f"Sikeres foglalás: {foglalas}")
            except ValueError as e:
                print(e)
        elif valasztas == "2":
            nev = input("Utas neve: ")
            jaratszam = input("Járatszám: ")
            try:
                lt.lemondas(nev, jaratszam)
                print("Foglalás lemondva.")
            except ValueError as e:
                print(e)
        elif valasztas == "3":
            lt.foglalasok_listazasa()
        elif valasztas == "4":
            break
        else:
            print("Érvénytelen opció!")

if __name__ == "__main__":
    main()
