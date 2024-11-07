import os
from docx import Document
from docx.shared import Pt
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# Define folder path and list of search strings
folder_path = "docx"
search_strings = [
    "sudo dpkg -i linux-image-unsigned-<kernel version>-<generic or derivative>*.deb",
    "sudo dpkg -i linux-headers-<kernel version>-<generic or derivative>*.deb",
    "sudo dpkg -i linux-modules-<kernel version>-<generic or derivative>*.deb",
    "deb [arch=amd64] http://archive.ubuntu.com/ubuntu focal main restricted",
    "<kernel_source_working_directory>/debian.<derivative>/changelog",
    "linux-image-unsigned-6.8.0-999-generic_6.8.0-999.48_amd64.deb",
    "sudo apt build-dep -y linux linux-image-unsigned-$(uname -r)",
    "deb-src http://archive.ubuntu.com/ubuntu jammy-updates main",
    "Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg",
    "<kernel_source_working_directory>/debian.master/changelog",
    "sudo apt install -y fakeroot llvm libncurses-dev dwarves",
    "linux-headers-6.8.0-999-generic_6.8.0-999.48_amd64.deb",
    "linux-modules-6.8.0-999-generic_6.8.0-999.48_amd64.deb",
    "sudo dpkg -i linux-headers-<kernel version>*_all.deb",
    "deb-src http://archive.ubuntu.com/ubuntu jammy main",
    "Components: main universe restricted multiverse",
    "linux-headers-6.8.0-999_6.8.0-999.48_all.deb",
    "Suites: noble noble-updates noble-backports",
    "apt source linux-image-unsigned-$(uname -r)",
    "linux (6.8.0-999.48) noble; urgency=medium",
    "/etc/apt/sources.list.d/ubuntu.sources",
    "URIs: http://archive.ubuntu.com/ubuntu",
    "sudo snap install snapcraft --classic",
    "cd <kernel_source_working_directory>",
    "dpkg --print-foreign-architectures",
    "dpkg --print-foreign-architectures",
    "fakeroot debian/rules editconfigs",
    "chmod a+x debian/scripts/misc/*",
    "fakeroot debian/rules binary",
    "└── linux_X.Y.Z.orig.tar.gz",
    "fakeroot debian/rules clean",
    "sudo apt purge -y snapcraft",
    "chmod a+x debian/scripts/*",
    "├── linux_X.Y.Z-*.diff.gz",
    "sudo apt-get -y upgrade",
    "chmod a+x debian/rules",
    "Types: deb deb-src",    
    "├── linux_X.Y.Z-*.dsc",
    "/etc/apt/sources.list",
    "Architectures: amd64",
    "<working_directory>",
    "sudo apt-get update",
    "├── linux-X.Y.Z/",
    "sudo apt update",
    "ubuntu.sources",
    "sources.list",
    "sudo reboot",
    "menuconfig",
    "│   └── *",
    "uname -r",
    "Types:",
    "[...]",
    "dpkg",
]

# Step 1: List all .docx files in the folder
docx_files = [f for f in os.listdir(folder_path) if f.endswith('.docx')]

for filename in docx_files:
    file_path = os.path.join(folder_path, filename)

    # Open the original .docx file for in-place modification
    doc = Document(file_path)

    # Step 2: Process each paragraph in the document
    for para in doc.paragraphs:
        for run in para.runs:
            # Check if any of the search strings are in the current run's text
            if any(search_string in run.text for search_string in search_strings):
                # Format matching text
                run.font.name = 'Ubuntu Mono'
                run.font.size = Pt(11)

                # Apply background color #EEEDEB
                rPr = run._r.get_or_add_rPr()  # Access the run properties
                shading_elm = parse_xml(r'<w:shd {} w:fill="EEEDEB"/>'.format(nsdecls('w')))
                rPr.append(shading_elm)

                # Print each updated line to the console
                print(run.text)

    # Step 3: Save changes directly to the original file
    doc.save(file_path)
    print(f"Formatted file: {file_path}")
