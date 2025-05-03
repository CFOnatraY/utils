﻿# Migration Data Cleaning Tool

This project aims to clean and update site numbers in a dataset. It handles migration issues where `CUST_SITE_NUMBER` from an old system (EBS Oracle) has extra digits appended to the end (e.g., `110098739` → `1100987391`). The tool compares data in two Excel files, cleans the `CUST_SITE_NUMBER` field, and updates it based on a reference report.

## Description

The project consists of several Python scripts:

- **`clean_data.py`**: Cleans the input Excel file by removing unwanted characters (e.g., tabs, spaces) and ensuring empty fields are treated correctly.
- **`update_data.py`**: Updates the `CUST_SITE_NUMBER` based on a comparison with the `SITE_NUMBER` from a reference report. It handles exact matches and migration issues with added digits.
- **`main.py`**: The main script that runs the cleaning and updating processes in sequence.

Additional details:
- **`SUFFIX_ADDED`**: A column that tracks any extra digits appended to `CUST_SITE_NUMBER` (e.g., `1`, `00`, etc.).
- **`CHANGE_STATUS`**: Indicates whether a site number was changed or if there was no match.
- **`NEW_PARTY_NUMBER`**: A new column that brings the `PARTY_NUMBER` from the reference report.
- **`NEW_USO`**: A new column indicating whether the site is associated with "Bill to" or "Ship to" (or both).
- **`NEW_CXC`**: A new column that brings the `CXC` account number from the reference report. If no account exists, it shows "DON'T_HAVE".
- **`NEW_CXI`**: A new column that brings the `CXI` account number from the reference report. If no account exists, it shows "DON'T_HAVE".
- **`NEW_FECHAFIN`**: A new column indicating when the `NEW_SITE_NUMBER` is/was active.
- **`NEW_ACCOUNT_NUMBER`**: A new column that tracks the `ACCOUNT_NUMBER` associated with the site number. If no account exists, it shows "DON'T_HAVE".

## Requirements

- Python 3.x
- Libraries:
  - pandas
  - openpyxl
  - numpy
  - re

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

1. Place your input Excel files (`input_file.xlsx` and `reference_report.xlsx`) in the same directory as the scripts.

2. Edit the `input_file.xlsx` and `reference_report.xlsx` files to include your data. Ensure that the columns are named correctly:
   - `input_file.xlsx` should contain a column named `CUST_SITE_NUMBER`.
   - `reference_report.xlsx` should contain a column named `SITE_NUMBER`, `PARTY_NUMBER`, `USO`, `CXC`, `CXI`, `FECHAFIN`, and `ACCOUNT_NUMBER`.

3. Run the main script to clean and update the data:
	```bash
	python main.py
	```

4. The cleaned and updated data will be saved in a new Excel file named `updated_clean_file.xlsx` in the same directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
