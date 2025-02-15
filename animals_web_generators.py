import json
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def display_animal_info(animal):
    output = []

    if 'name' in animal:
        output.append(f'<div class="card__title">{animal["name"]}</div>')
    if 'characteristics' in animal:
        characteristics = animal['characteristics']
        if 'diet' in characteristics:
            output.append(f'<p class="card__text"><strong>Diet:</strong> {characteristics["diet"]}<br/>')
        if 'type' in characteristics:
            output.append(f'<strong>Type:</strong> {characteristics["type"]}<br/>')
    if 'locations' in animal and animal['locations']:
        output.append(f'<strong>Location:</strong> {", ".join(animal["locations"])}<br/></p>')

    return "<br/>\n".join(output)

def generate_animals_output(animals):
    items = []
    for animal in animals:
        animal_info = display_animal_info(animal)
        item_html = f'<li class="cards__item">\n{animal_info}\n</li>'
        items.append(item_html)
    return "\n".join(items)

def main():
    animals_data = load_data('animals_data.json')
    animals_output = generate_animals_output(animals_data)

    with open('animals_template.html', 'r') as template_file:
        template_content = template_file.read()

    new_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_output)

    with open('animals.html', 'w') as output_file:
        output_file.write(new_html_content)

    print(animals_output)

if __name__ == "__main__":
        main()


