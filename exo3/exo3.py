"""
Une méthode agile est une approche itérative et collaborative pour
mener à bien un projet.
Elle génère un produit de haute qualité tout en prenant en compte
l’évolution des besoins des clients.

La méthode la plus connue est Scrum.

Au début d'un projet un « backlog », ensemble de tache à réaliser
est défini avec le client.
Ce « backlog » évolue dans le temps en fonction du besoin de client.
On peut y rajouter des taches comme on peut en enlever.

Durant le projet, une réunion avec l'équipe technique et l'équipe
opérationnelle est organisée à chaque
« sprint » (unité de temps composé de quelques semaines).
Lors cette réunion, le client valide ou non les taches
qui ont été réalisées durant la période de « sprint ».

Dans ce challenge, vous devez déterminer si à la date de la livraison
finale, le client obtient la totalité de son produit.


Format des données

Entrée
Ligne 1 : un entier N correspondant au nombre de sprints(réunion).
Ligne 2 : un entier T correspondant au nombre de taches dans le « backlog »
        initial.
Ligne 3 à N+2 : un entier V et un entier U séparés par un espace où V est
le nombre de taches validées
et U le nombre de taches à ajouter (si U est positif) ou à supprimer
(si U est négatif) dans le « backlog ».

Sortie
La chaîne OK si le backlog est vide. Sinon retourner la chaîne KO.

"""


def processLines(lines) -> str:
    # Read number of sprints and initial backlog
    N = int(lines[0])  # Number of sprints
    backlog = int(lines[1])  # Initial number of tasks in the backlog

    # Process each sprint
    for i in range(2, 2 + N):
        V, U = map(int, lines[i].split())
        backlog = backlog - V + U  # Update the backlog

    # Check if the backlog is empty
    return "OK" if backlog == 0 else "KO"  # Return "OK" if empty, "KO" otherwise

# Example usage:
input_data = [
    "3",     # Number of sprints
    "10",    # Initial tasks in the backlog
    "3 2",   # Sprint 1: 3 tasks validated, 2 added
    "4 -1",  # Sprint 2: 4 tasks validated, 1 removed
    "3 0"    # Sprint 3: 3 tasks validated, none added
]

# Call the function and print the result
result = processLines(input_data)
print(result)  # Expected output: "KO"



