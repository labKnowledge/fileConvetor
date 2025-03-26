import subprocess
import argparse
import os

def convert_to_markdown(input_path):
    """
    Converts a document to Markdown using MarkItDown.

    Args:
        input_path (str): The path to the input document.
    Returns:
        str: The converted Markdown content if output_path is not specified.
    """

    # Determine the input file extension
    extension = input_path.split('.')[-1]

    output_path = input_path.replace('.' + extension, '.md')
    # Construct the command to convert the document to Markdown
    command = f"markitdown '{input_path}' > '{output_path}'"

    # Print the command to see what is being executed
    print(f"Executing command: {command}")

    # Run the command and capture the output or check for errors
    result = subprocess.run(command, check=True, capture_output=True, text=True, shell=True)
    
    return result.stdout

if __name__ == "__main__":
    # Check if the specified folder exists
    input_folder = 'documents'  # Specify the folder containing documents
    if os.path.exists(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(('.doc', '.docx', '.pdf')):  # Add other formats as needed
                input_path = os.path.join(input_folder, filename)
                markdown_content = convert_to_markdown(input_path)
                print(markdown_content)
    else:
        print(f"The folder '{input_folder}' does not exist.")