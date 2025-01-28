import json
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def display_animal_info (animals):
    output = []
    for animal in animals:
        if 'name' in animal:
            output.append(f"Name: {animal ['name']}")
        if 'characteristics' in animal:
            characteristics = animal['characteristics']
        if 'diet' in characteristics:
            output.append(f"diet: {characteristics['diet']}")
        if'locations' in animal and animal['locations']:
            output.append(f"Location:{animal['locations'] [0]}")
        if 'type' in characteristics:
            output.append(f"type:{characteristics['type']}")
        return "\n".join(output)


def generate_animals_output(animals):
    return "\n\n".join (display_animal_info(animals) for animal in animals)


def main():
    animals_data = load_data('animals_data.json')
    animals_output = generate_animals_output(animals_data)

    with open('animals_template.html','r') as template_file:
        template_content = template_file.read()

    new_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_output)

    with open('animals.html','w')as output_file:
        output_file.write(new_html_content)

    print(animals_output)


if __name__ == "__main__":
    main()
