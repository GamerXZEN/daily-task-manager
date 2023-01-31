import PySimpleGUI as sg

compress_label = sg.Text("Select files to compress: ")
compress_input = sg.Input(tooltip="Enter in the path of the files here")
compress_choose_button = sg.FilesBrowse("Choose")

destination_label = sg.Text("Select destination folder: ")
destination_input = sg.Input(tooltip="Enter in the path of the destination folder")
destination_choose_button = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

desktop_window = sg.Window("File Compressor",
                           layout=[[compress_label, compress_input, compress_choose_button],
                                   [destination_label, destination_input, destination_choose_button],
                                   [compress_button]])
desktop_window.read()
desktop_window.close()