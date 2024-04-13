import os
import argparse
import glob
import xml.etree.ElementTree as ET
from pathlib import Path
import sys
import logging

class MissingKeyError(Exception):
    pass

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Initialize logger
    logger = logging.getLogger(__name__)

    return logger

def sort_by_key(element):
    if element.find('Key') is not None:
        return element.find('Key').text
    else:
        raise MissingKeyError("Element does not contain a 'Key' child.")

def process_xml_file(file_path, logger):
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Extract elements to be sorted
        elements = root.findall('./*')

        # Sort elements by key child
        is_sorted = False

        try:
            elements.sort(key=sort_by_key)
            is_sorted = True
        except MissingKeyError as err:
            logger.warning(f"Skipping sorting of file '{file_path}': {err}")

        # Standardize formatting
        for element in elements:
            # Normalize whitespace in child elements
            for child in element:
                if child.text:
                    child.text = child.text.strip()

            # Sort attributes alphabetically within each element
            element.attrib = dict(sorted(element.attrib.items()))

            # sort child elements alphabetically
            if len(element) > 0:
                element[:] = sorted(element, key=lambda x: x.tag)


        if is_sorted:
            # create a copy of the elements list
            elements_copy = elements.copy()

            # remove all elements from the root
            for element in elements:
                root.remove(element)

            # Add sorted elements back to the root to ensure they are in the correct order
            for element in elements_copy:
                root.append(element)

        # Save modified XML file
        sorted_tree = ET.ElementTree(root)
        sorted_tree.write(file_path, encoding='utf-8', xml_declaration=True)
        logger.info(f"Processed file: '{file_path}'")


    except Exception as e:
        logger.error(f"Error processing file '{file_path}': {e}")

def process_xml_files(directory, logger):
    # Iterate over XML files in the directory
    for filename in directory.glob('**/*.xml'):
        process_xml_file(filename, logger)

def main():
    # Initialize logger
    logger = setup_logger()

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Sort and standardize XML files')
    parser.add_argument('directory', type=str, help='Path to directory containing XML files')
    args = parser.parse_args()

    # Validate directory path
    directory_path = Path(args.directory)
    if not directory_path.is_dir():
        logger.error(f"Error: '{args.directory}' is not a valid directory.")
        sys.exit(1)

    # Process XML files in the directory
    process_xml_files(directory_path, logger)
    return 0

if __name__ == "__main__":
    sys.exit(main())
