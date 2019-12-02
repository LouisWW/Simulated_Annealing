# calculate the energy level of one particle
def calc_energy_1p(coordinates, particlenumber, list_particles):
    E = 0
    for i in range(len(list_particles)):
        distance = np.sqrt((coordinates[0] - list_particles[i].x) ** 2 + (coordinates[1] - list_particles[i].y) ** 2)
        if distance != 0:
            E += 1 / distance

    return E