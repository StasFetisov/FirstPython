print('Hello world')



from os.path import exists
path_to_file = r'..\requirements.txt'
file_name = '..\requirements.txt'
file_exists = exists (path_to_file)
if file_exists:

    file_descriptor = open(path_to_file, 'r', encoding='utf-16')
    file_text = file_descriptor.read()
    print(file_name)
    print(file_text)

else:
    print(f'Файл не найден {path_to_file}')