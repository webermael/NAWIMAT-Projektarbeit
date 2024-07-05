# Installation Guide

## Prequisites
- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer) 

## Steps
1. Clone the repository:

```sh 
git clone https://github.com/webermael/NAWIMAT-Projektarbeit.git
cd NAWIMAT-Projektarbeit
```

2. Create and activate a virtual environment:

macOS / Linux:

```sh
python -m venv venv
source venv/bin/activate
```

Windows:
```sh
python -m venv venv
source venv\Scripts\activate
```

3. Install the required dependencies:

```sh 
pip install -r requirements.txt
```

4. Run the simulation:

```sh 
python src/main.py
```
