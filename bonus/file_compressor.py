import zipfile
import pathlib

def zip_file(filepaths, dest_dir):
	dest_path = pathlib.Path(dest_dir, "compressed_zip")
	with zipfile.ZipFile(dest_path, 'w') as file:
		for filepath in filepaths:
			filepath = pathlib.Path(filepath)
			file.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
	zip_file(filepaths=["feet_to_meters.py", "b1.py"], dest_dir="sheesh")
