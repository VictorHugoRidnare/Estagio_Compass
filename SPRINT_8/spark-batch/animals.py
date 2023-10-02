import csv

with open("SPRINT_8\ordered_animals.csv", mode='w', newline='') as file:
    writer = csv.writer(file)

    animals = [
        "Cachorro",
        "Gato",
        "Elefante",
        "Leão",
        "Tigre",
        "Girafa",
        "Rinoceronte",
        "Zebra",
        "Cavalo",
        "Panda",
        "Kanguru",
        "Coelho",
        "Pássaro",
        "Peixe",
        "Tartaruga",
        "Serpente",
        "Crocodilo",
        "Macaco",
        "Hipopótamo",
        "Pinguim"
    ]

    ordered_list = sorted(animals)
    for item in ordered_list:
        writer.writerow([item])

file.close()