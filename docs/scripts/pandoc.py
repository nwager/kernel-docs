import os
import subprocess

# Specify the folder path
folder_path = 'docx'

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an HTML file
    if filename.endswith('.html'):
        html_file_path = os.path.join(folder_path, filename)
        docx_file_path = os.path.join(folder_path, filename.replace('.html', '.docx'))
        
        # Run the pandoc command to convert HTML to DOCX
        try:
            subprocess.run(['pandoc', html_file_path, '-o', docx_file_path, '--reference-doc', 'scripts/pandoc-template.docx'], check=True)
            print(f"Converted {filename} to {os.path.basename(docx_file_path)}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {filename}: {e}")
        
"""         # Remove the original HTML file after conversion
        try:
            os.remove(html_file_path)
            print(f"Deleted {filename}")
        except OSError as e:
            print(f"Error deleting {filename}: {e}") """
