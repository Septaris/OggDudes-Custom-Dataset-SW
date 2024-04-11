import os
import argparse
import glob
import xml.etree.ElementTree as ET
from pathlib import Path
import sys
import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Initialize logger
    logger = logging.getLogger(__name__)

    return logger

def sort_by_key(element):
    if element.find('Key') is not None:
        return element.find('Key').text
    else:
        raise ValueError("Element does not contain a 'Key' child.")

def process_xml_file(file_path, logger):
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Extract elements to be sorted
        elements = root.findall('./*')
        
        # Sort elements by key child
        elements.sort(key=sort_by_key)

        
        # Standardize formatting
        for element in elements:
            # Normalize whitespace in child elements
            for child in element:
                if child.text:
                    child.text = child.text.strip()
            
            # Sort attributes alphabetically within each element
            element.attrib = dict(sorted(element.attrib.items()))

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
        sorted_tree.write(file_path, encoding='utf-8')
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
    sys.exit(0)

if __name__ == "__main__":
    main()
