C = 300000000  # velocità della luce in m/s


def main():
    mass = int(input("m: "))
    print(energy(mass))


def energy(mass):
    return mass * C ** 2