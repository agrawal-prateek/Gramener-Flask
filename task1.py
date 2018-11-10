import os


def print_dir(current_path):
    if os.path.isfile(current_path):
        print(current_path)
        return
    for dir_or_file in os.listdir(current_path):
        print_dir(os.path.join(current_path, dir_or_file))


if __name__ == '__main__':
    dir_name = input('Enter Directory path (Relative or Absolute)\n')
    print_dir(current_path=dir_name)
