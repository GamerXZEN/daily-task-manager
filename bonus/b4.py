import PySimpleGUI as PSG
from file_extractor import extract_file as ext

PSG.theme("DarkPurple4")

extract_label = PSG.Text("Select files to extract: ")
extract_input = PSG.Input(tooltip="Enter in the path of the files here")
extract_choose_button = PSG.FilesBrowse("Choose", key="files")

destination_label = PSG.Text("Select destination folder: ")
destination_input = PSG.Input(tooltip="Enter in the path of the destination folder")
destination_choose_button = PSG.FolderBrowse("Choose", key="folder")

extract_button = PSG.Button("Extract", key="extract")
output = PSG.Text(key="output", text_color="green")

desktop_window = PSG.Window("File Compressor",
                            layout=[[extract_label, extract_input, extract_choose_button],
                                    [destination_label, destination_input, destination_choose_button],
                                    [extract_button, output]])

while True:
    event, values = desktop_window.read()
    filepath = values["files"]
    dest_dir = values["folder"]
    ext(filepath, dest_dir)
    desktop_window["output"].update(value="Extraction successful")

    match event:
        case PSG.WIN_CLOSED:
            break

desktop_window.close()
