import xml.etree.ElementTree as ET
import json
import pathlib
import argparse

def parse_talent_tree(specialization_file, talents_file, output_file):
    # Parse the XML files
    spec_tree = ET.parse(specialization_file)
    talents_tree = ET.parse(talents_file)

    # Extract root elements
    spec_root = spec_tree.getroot()
    talents_root = talents_tree.getroot()

    # Create a lookup dictionary for talents
    talent_lookup = {}
    for talent in talents_root.findall('Talent'):
        key = talent.find('Key').text
        name = talent.find('Name').text
        description = talent.find('Description').text
        talent_lookup[key] = {
            'name': name,
            'description': description
        }

    # Parse the specialization tree

    sources_node = spec_root.find('Sources')

    if sources_node is not None:
        sources = [{'page': source_node.attrib['Page'], 'title': source_node.text} for source_node in sources_node]
    else:
        source_node = spec_root.find('Source')
        sources = [{'page': source_node.attrib['Page'], 'title': source_node.text}]

    universal_node = spec_root.find('Universal')

    career_skills_node = spec_root.find('CareerSkills')


    specialization = {
        'key': spec_root.find('Key').text,
        'name': spec_root.find('Name').text,
        'description': spec_root.find('Description').text,
        'sources': sources,
        'career_skills': [skill.text for skill in career_skills_node.findall('Key')] if career_skills_node is not None else [],
        'universal': universal_node is not None and universal_node.text.lower() == 'true',
        'talent_rows': []
    }

    # Process talent rows
    for row in spec_root.find('TalentRows').findall('TalentRow'):
        row_data = {
            'cost': row.find('Cost').text,
            'talents': []
        }
        for index, talent_key in enumerate(row.find('Talents').findall('Key')):
            talent = talent_lookup.get(talent_key.text, None)

            if talent is None:
                print(f'Talent {talent_key.text} is missing (Spec {output_file.stem})')
                talent = {'name': 'Unknown', 'description': 'No description available.'}
            connections = []
            directions = row.find('Directions').findall('Direction')
            if index < len(directions):
                direction = directions[index]
                connections = {
                    'left': direction.find('Left') is not None and direction.find('Left').text.lower() == 'true',
                    'right': direction.find('Right') is not None and direction.find('Right').text.lower() == 'true',
                    'up': direction.find('Up') is not None and direction.find('Up').text.lower() == 'true',
                    'down': direction.find('Down') is not None and direction.find('Down').text.lower() == 'true',
                }
            row_data['talents'].append({
                'key': talent_key.text,
                'name': talent['name'],
                'description': talent['description'],
                'connections': connections
            })
        specialization['talent_rows'].append(row_data)

    # Save the result as JSON
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(specialization, json_file, ensure_ascii=False, indent=4)


def main(specialization_dirpath):
    # File paths
    talents_file = 'DataCustom/Talents.xml'
    for specialization_filepath in specialization_dirpath.glob('*.xml'):
        output_file = pathlib.Path('output') / f'{specialization_filepath.stem.lower().replace(' ', '_')}.json' 

        # Run the script
        try:
            parse_talent_tree(specialization_filepath, talents_file, output_file)
        except Exception as err:
            print(f'Exception {err} occured during parsing of {specialization_filepath}')
            raise 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('specialization_dirpath', type=pathlib.Path)

    args = parser.parse_args()
    main(args.specialization_dirpath)