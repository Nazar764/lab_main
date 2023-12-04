class Video_card:
    def __init__(self, year, cooler, power, name):
        self.year = year
        self.cooler = cooler
        self.power = power
        self.name = name

    def get_attribute(self, attribute):
        return getattr(self, attribute, "Attribute not found")

class Nvidia(Video_card):
    pass

class AMD(Video_card):
    pass

NVIDIA1 = Nvidia(year="2022", cooler="ML_120", power="500fps", name="4090")
AMD2 = AMD(year="2021", cooler="ML_150", power="421fps", name="6600")

v1 = {"NVIDIA": NVIDIA1, "AMD2": AMD2}

while True:
    i = input("Така як [year/...]")
    if i == "exit":
        print("OK")
        exit()
    else:
        for key, v in v1.items():
            print(f"{key}'s {i}: {v.get_attribute(i)}")
