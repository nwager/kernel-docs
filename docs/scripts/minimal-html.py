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
    try:
        # Open and parse the HTML file
        with open(html_file_path, 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')
        
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

