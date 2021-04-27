from course_contents.c06_files.imports_project.utils  import utils

from course_contents.c06_files.imports_project.utils.common.file_operations import save_to_file, read_file

save_to_file('Hello, world!', 'test.txt')

print(read_file('test.txt'))

print(f'app is {__name__}')
