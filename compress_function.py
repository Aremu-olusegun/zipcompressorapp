import os
import zipfile

def make_archive(filepaths, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    archive_name = f"{dest_dir}/archive.zip"
    with zipfile.ZipFile(archive_name, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)


if __name__ == "__main__":
    make_archive(filepaths=[r"C:\Users\Aremu\PycharmProjects\pythonProject1\mypythoncode\calculate.txt", r"C:\Users\Aremu\PycharmProjects\pythonProject1\mypythoncode\todos.txt"], dest_dir=r"C:\Users\Aremu\PycharmProjects\pythonProject1\mypythoncode\my_archive.zip")
