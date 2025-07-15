# Utils Repository

This repository contains a collection of utility scripts designed for common automation and data-processing tasks. It is divided into various main components:

- A set of general-purpose **Python utility scripts** for various use cases such as text processing, user management, and educational games.

---

## 📁 Directory Overview

### 1. `scripts/`
A miscellaneous collection of lightweight scripts, useful for quick automation, testing, and learning.

#### 📊 Script Overview

| Script                             | Description                                         |
|------------------------------------|-----------------------------------------------------|
| `ari_app_multiplication_trainer.py`| Interactive multiplication practice game            |
| `clean_transcription_file.py`      | Cleans and formats transcription text files         |
| `manage_users.py`                  | Adds, removes, and displays users in a list         |
| `search_keywords.py`               | Finds keywords within a text input or file          |
| `space_counter.py`                 | Counts spaces and characters in a text block        |

## 📄 Requirements

- Python 3.x
- Libraries:
  - pandas
  - openpyxl
  - numpy
  - (other libraries based on the scripts)

## 🛠️ Installation

1. Clone this repository:
	```bash
	git clone https://github.com/CFOnatraY/utils.git
	git clone git@github.com:CFOnatraY/utils.git
	```

2. Create a virtual environment (optional but recommended):
	```bash
	python -m venv venv
	```

3. Activate the virtual environment:
	- On Windows:
	```bash
	venv\scripts\activate
	```
	- On macOS/Linux:
	```bash
	source venv/bin/activate
	```

4. Install the required libraries:
	 ```bash
	pip install -r requirements.txt
	```

## 🚀 How to Run

1. For `scripts/` folder:

Navigate to the Other_Scripts directory and run any script independently:

	```bash
	cd scripts
	python script_name.py
	```


## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.