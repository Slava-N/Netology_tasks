import os
import glob
import os.path
import subprocess

program_to_use = 'convert.exe'
operation = '-resize'
operation_argument = '200'
input_photo_folder = "Source"
output_photo_folder = "Result"

def create_file_list(folder_name):
    files = glob.glob(os.path.join(folder_name, '*.jpg'))
    return(files)

def create_result_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def narrow_photo(program_to_use, input_photo, operation, operation_argument, output_photo):
    subprocess.run(['convert.exe', input_photo, '-resize', '200', output_photo])


def execute_multiple_corrections(program_to_use, operation, operation_argument, files, output_photo_folder):
    for input_photo in files:
        photo_name = input_photo.split('\\')[1]
        output_photo = os.path.join(output_photo_folder, photo_name)
        narrow_photo(program_to_use, input_photo, operation, operation_argument, output_photo)

create_result_folder(output_photo_folder)

execute_multiple_corrections(program_to_use,
                operation,
                operation_argument,
                create_file_list(input_photo_folder),
                output_photo_folder
                )
