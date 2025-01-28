import json
def load_data(animal_data):
  """ Loads a JSON file """
  with open(animal_data, "r") as handle:
    return json.load(handle)


def display_animal_info (animals):
    for animal in animals:
        if 'name' in animal:
            print(f"Name: {animal ['name']}")
        if 'characteristics' in animal:
            characteristics = animal['characteristics']
        if 'diet' in characteristics:
            print(f"diet: {characteristics['diet']}")
        if'locations' in animal and animal['locations']:
            print(f"Location:{animal['locations'] [0]}")
        if 'type' in characteristics:
            print(f"type:{characteristics['type']}")
        print()

animals_data = load_data('animals_data.json')
display_animal_info(animals_data)