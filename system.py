import matplotlib.pyplot as plt
import numpy as np

# Durée de la simulation en jours
duration = 365 * 10

# Positions initiales des planètes en unités astronomiques
planet_initial_positions = [
    [0, 0],  # Soleil
    [1, 0],  # Mercure
    [5.2, 0],  # Vénus
    [10, 0],  # Terre
    [19.18, 0],  # Mars
    [30.07, 0],  # Jupiter
    [39.53, 0],  # Saturne
    [46.97, 0]  # Uranus
]

# Vitesse angulaire en degrés par jour pour chaque planète
planet_angular_speeds = [
    0,  # Soleil
    4.09,  # Mercure
    1.605,  # Vénus
    1,  # Terre
    0.532,  # Mars
    0.084,  # Jupiter
    0.034,  # Saturne
    0.012  # Uranus
]

# Conversion en radians par jour
planet_angular_speeds = [np.deg2rad(speed) for speed in planet_angular_speeds]

# Temps de la simulation
times = np.linspace(0, duration, duration)

# Calcul des positions pour chaque planète pour chaque jour de la simulation
planet_positions = []
for i, initial_position in enumerate(planet_initial_positions):
    x = initial_position[0] * np.cos(planet_angular_speeds[i] * times)
    y = initial_position[0] * np.sin(planet_angular_speeds[i] * times)
    planet_positions.append((x, y))

# Dessin des positions pour chaque planète
for i, planet_position in enumerate(planet_positions):
    plt.plot(planet_position[0], planet_position[1], label=f'Planète {i + 1}')

# Ajout d'une légende et d'un titre
plt.legend()
plt.title("Mouvement des planètes dans le système solaire")

# Affichage du graphique
plt.show()
