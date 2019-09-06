# Requirements:

- [apt-get | apk | brew | ...] install tesseract
- pip install -r requirements.txt

# Usage:
### text to dwemer:
````
python dwemer.py --write='text to write' [--output=png_file_name] [--font-size=size] [--font-type=type]
````
### dwemer to text:
````
python dwemer.py --read=path_to_file.png [--output=text_file_name]
````
### help:
````
python dwemer.py --help
````
