import re
import fnmatch
import os


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None


def find_items_by_name(item_name_pattern, search_type='file', start_directory=None):
        """
    Search for files or folders by name in the specified directory.

    :param item_name_pattern: The pattern to search for (e.g., 'MyFolder*', '*.txt')
    :param search_type: 'file' to search for files, 'folder' to search for folders
    :param start_directory: The directory to start the search from. Defaults to the root directory.
    :return: List of paths matching the search criteria
        """
    # Use the start directory or the root directory if none is provided
        root_directory = start_directory if start_directory else os.path.abspath(os.sep)
        matching_items = []

    # Walk through the directory tree, without following symbolic links
        for dirpath, dirnames, filenames in os.walk(root_directory, followlinks=False):
            try:
                if search_type == 'file':
                    # Search for files
                    for filename in filenames:
                        if fnmatch.fnmatch(filename, item_name_pattern):
                            matching_items.append(os.path.join(dirpath, filename))
                elif search_type == 'folder':
                    # Search for folders
                    for dirname in dirnames:
                        if fnmatch.fnmatch(dirname, item_name_pattern):
                            matching_items.append(os.path.join(dirpath, dirname))
            except PermissionError:
                print(f"Permission denied: {dirpath}")
                continue
            except Exception as e:
                print(f"Error: {e}")
                continue

        return matching_items



