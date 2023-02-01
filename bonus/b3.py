import PySimpleGUI as PSG
from file_compressor import zip_file as comp

compress_label = PSG.Text("Select files to compress: ")
compress_input = PSG.Input(tooltip="Enter in the path of the files here")
compress_choose_button = PSG.FilesBrowse("Choose", key="files")

destination_label = PSG.Text("Select destination folder: ")
destination_input = PSG.Input(tooltip="Enter in the path of the destination folder")
destination_choose_button = PSG.FolderBrowse("Choose", key="folder")

compress_button = PSG.Button("Compress", key="compress")
output = PSG.Text(key="executable files", text_color="green")

desktop_window = PSG.Window("File Compressor",
                            layout=[[compress_label, compress_input, compress_choose_button],
                                   [destination_label, destination_input, destination_choose_button],
                                   [compress_button]])

while True:
    event, values = desktop_window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    comp(filepaths, folder)
    desktop_window["executable files"].update(value="Compression successful")

    match event:
        case PSG.WIN_CLOSED:
            break

desktop_window.close()
