# Requirements:

- [apt-get | apk | brew | ...] install tesseract
- pip install -r requirements.txt

# Usage:
### text to dwemer:
````
python dwemer.py --write='path_to_file.txt' [--output=png_file_name] [--font-size=size] [--font-type=type]
````
### dwemer to text:
````
python dwemer.py --read=path_to_file.png [--output=text_file_name]
````
### help:
````
python dwemer.py --help
````

# Exemple:
### text to dwemer:
````
python dwemer.py --write=dwemer.py --output=exemple/dwemer
````
### dwemer to text:
````
python dwemer.py --read=exemple/dwemer.png --output=exemple/dwemer
````

