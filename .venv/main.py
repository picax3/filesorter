import os
import shutil

def create_folder(path: str, extension: str) -> str:
    folder_name: str = extension[1:]
    """ creates a folder after extension of the file so everything after character 0.
    [1:] slicing starts from the second charater onward
    extension = '.jpg' then extension[1:] would return 'jpg' """
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        """checks if folder with extension name doesnt exist and makes directory"""
        os.makedirs(folder_path)
        """if exists returns the folder"""
    return folder_path


def sort_files(source_path: str):
    """sort files on a given path"""

    for root_dir, sub_dir, filenames in os.walk(source_path):
        """walks thru all directories and files in that path
        open up each folder and slowly walk thru it
        return to us a tuple of file dir, sub dir and filenames
        for each of the paths
        recursivelly walking thru each files"""
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extension: str = os.path.splitext(filename)[1]
            """split file name and grab whatever after index 1
            returning safe operation
            return no name if no extension
            check first if there is an extension"""

            if extension:
                """if there is an extension
                create our target folder"""
                target_folder: str = create_folder(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)

            """shutil moves files around
            """
            shutil.move(file_path, target_path)
            """make sure we dont have any folders
            after files are moved
            create a function that removes them"""

def remove_empty_folders(source_path: str):
    """removes all empty folders"""
    """perform same walking operation
    we used to sort files
    copy paste line 21 and specify new parameter topdown
    set it to false meaning starting with subfolders
    making way back to root
    by default start with root"""
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        """loop thru all sub-directories"""
        for current_dir in sub_dir:
            folder_path: str = os.path.join(root_dir, current_dir)
            """now that we have current path
            check for any elements inside it"""
            if not os.listdir(folder_path):
                os.rmdir(folder_path)

def main():
    user_input: str = input("Please provide a file path to sort:")

    if os.path.exists(path=user_input):
        """if path provided by user exists perform operation"""
        sort_files(user_input)
        """sort files provided by user input"""
        remove_empty_folders(user_input)
        print('Files sorted succesfully')
    else:
        print('Invalid path, pls provide a valid path.')

if __name__ == "__main__":
    main()
