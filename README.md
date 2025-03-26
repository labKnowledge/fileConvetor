# GitHub Action Markdown Converter

This project provides a GitHub Action that automatically converts uploaded documents in a specified folder to Markdown format using a Python script.

## Overview

The GitHub Action is triggered when files are uploaded to a designated folder in your repository. It utilizes the `toMarkdown.py` script to convert various document formats into Markdown files.

## Project Structure

```
github-action-markdown-converter
├── .github
│   └── workflows
│       └── convert-to-markdown.yml
├── toMarkdown.py
├── requirements.txt
└── README.md
```

## Setup

1. **Clone the Repository**: Start by cloning this repository to your local machine.

   ```bash
   git clone <repository-url>
   cd github-action-markdown-converter
   ```

2. **Install Dependencies**: Ensure you have the required Python packages. You can install them using pip.

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure GitHub Action**: The action is defined in the `.github/workflows/convert-to-markdown.yml` file. You can customize the trigger and other parameters as needed.

## Usage

1. **Upload Documents**: Place the documents you want to convert in the specified folder in your repository.

2. **Trigger the Action**: The GitHub Action will automatically run when files are uploaded, converting them to Markdown format.

3. **Check Output**: The converted Markdown files will be saved in the same directory as the original documents, with a `.md` extension.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.