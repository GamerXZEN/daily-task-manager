import zipfile
import pathlib


def extract_file(filepath, dest_dir):
	with zipfile.ZipFile(filepath, 'r') as file:
		file.extractall(dest_dir)


if __name__ == '__main__':
	extract_file(filepath=["feet_to_meters.py", "b1.py"], dest_dir="test_dir")
