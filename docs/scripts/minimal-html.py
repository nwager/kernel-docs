import os
import subprocess
from bs4 import BeautifulSoup

# Function to clean HTML by removing ¶ characters
def clean_html(file_path):
    try:
        subprocess.run(['sed', '-i', 's/¶//g', file_path], check=True)
        print(f"Cleaned file: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error cleaning file {file_path}: {e}")

# Read input from the provided text file
def process_input_file(input_file_path):
    output_files = []  # Store output files for cleanup
    
    with open(input_file_path, 'r') as file:
        for line in file:
            # Strip any extraneous whitespace or newline characters
            line = line.strip()
            
            if line:
                # Split the line into fields based on commas
                fields = line.split(',')
                
                # Extract the values
                html_file_path = fields[0].strip()
                target_element = fields[1].strip()
                selector_type = fields[2].strip()
                selector_value = fields[3].strip()
                output_file_path = fields[4].strip()

                # Process each HTML file
                process_html(html_file_path, target_element, selector_type, selector_value, output_file_path)
                
                # Add the output file to the list for cleaning later
                output_files.append(output_file_path)

    # Clean up all the output files after processing is done
    for output_file in output_files:
        clean_html(output_file)

# Function to process the HTML file
def process_html(html_file_path, target_element, selector_type, selector_value, output_file_path):

    # Define the base domain as a variable
    base_domain = "https://canonical-kernel-docs.readthedocs-hosted.com/en/latest/"

    # Define list of internal refs to replace
    internal_refs = [
        ["#how-to-build-kernel-setup", "#set-up-build-environment"],
        ["#how-to-build-kernel-install-packages", "#install-required-packages"],
        ["#how-to-build-kernel-obtain-source", "#obtain-the-source-for-an-ubuntu-release"],
        ["../../prepare/obtain-kernel-source-git/", f"{base_domain}how-to/prepare/obtain-kernel-source-git/"]
    ]

    try:
        # Open and parse the HTML file
        with open(html_file_path, 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')

        # Find all <span> elements with an "id" attribute and remove them
        for span in soup.find_all('span', id=True):
            span.decompose()  # Removes the element from the DOM

        # Loop through each replacement in internal_refs
        for old_href, new_href in internal_refs:
            # Find all <a> tags with class 'reference internal' and the matching href
            for link in soup.find_all('a', class_='reference internal', href=old_href):
                link['href'] = new_href

        # Find the target element based on the selector type and value
        if selector_type == 'id':
            target_element = soup.find(target_element, {'id': selector_value})
        elif selector_type == 'class':
            target_element = soup.find(target_element, {'class': selector_value})
        else:
            print(f"Unsupported selector type: {selector_type}")
            return
        
        # If the target element is found, save it to the output file
        if target_element:
            with open(output_file_path, 'w') as target_file:
                target_file.write(str(target_element))
            print(f"Saved target element to: {output_file_path}")
        else:
            print(f"Element not found with {selector_type}='{selector_value}' in {html_file_path}")
    
    except Exception as e:
        print(f"Error processing {html_file_path}: {e}")

# Main entry point
if __name__ == "__main__":
    # Path to docx list
    input_file = './scripts/docx-file-list'

    # Process the input file
    process_input_file(input_file)

