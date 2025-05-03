# Utils Repository

This repository contains various utility scripts for different tasks. It includes a **Migration Data Cleaning Tool** for cleaning and updating site numbers, as well as other utility scripts for different development needs.

## Directories:

### 1. **MigrationDataCleaningTool**:
This folder contains the code related to the migration data cleaning tool. It focuses on handling migration issues in `CUST_SITE_NUMBER` (EBS Oracle to Oracle Fusion Cloud Applications migration), cleaning the data, and updating site numbers based on a reference report.

Scripts inside this folder:
- **`clean_data.py`**: Cleans the input Excel file by removing unwanted characters (e.g., tabs, spaces) and ensuring empty fields are treated correctly.
- **`update_data.py`**: Updates the `CUST_SITE_NUMBER` based on a comparison with the `SITE_NUMBER` from a reference report. It handles exact matches and migration issues with added digits.
- **`main.py`**: The main script that runs the cleaning and updating processes in sequence.
- **`requirements.txt`**: The dependencies needed for the data cleaning tool.
- **`README.md`**: Documentation specific to the Migration Data Cleaning Tool.

### 2. **Other_Scripts**:
This folder contains various other utility scripts for different development tasks.

Scripts inside this folder:
- **`clean_transcription_file.py`**: (description of this script)
- **`manage_users.py`**: (description of this script)
- **`search_keywords.py`**: (description of this script)
- **`space_counter.py`**: (description of this script)

### Requirements

- Python 3.x
- Libraries:
  - pandas
  - openpyxl
  - numpy
  - re
  - (other libraries based on the scripts)

## Installation

1. Clone this repository:
	```bash
	git clone https://github.com/CFOnatraY/utils.git
	```

2. Create a virtual environment (optional but recommended):
	```bash
	python -m venv venv
	```

3. Activate the virtual environment:
	- On Windows:
	```bash
	venv\Scripts\activate
	```
	- On macOS/Linux:
	```bash
	source venv/bin/activate
	```

4. Install the required libraries:
	 ```bash
	pip install -r requirements.txt
	```

## Usage

1. For Migration Data Cleaning Tool:

	- Navigate to MigrationDataCleaningTool/.
	- Run the main script:
	```bash
	python main.py
	```

2. For Other_Scripts, each script has its own functionality. You can run them individually depending on your needs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.