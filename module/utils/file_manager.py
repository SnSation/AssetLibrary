# Import Required Packages
import os
from .directory import FMDirectory

# 'FileManager' is the main object of this file.
# All code in this file relates directly to the 'FileManager' object.
class FileManager:
    # Sections:
        # 1. Class Variables
        # 2. Special Methods
        # 3. Getters and Setters
        # 4. Attribute Methods
        # 5. Utility Methods
        # 6. Primary Methods

    ##### Key #####
        # Name as a string = 'name' OR 'target_name'
        # Text as a string = 'text'
        # Object = 'class_name_obj'
        # Dictionary = 'expected_content_dict'
        # List = 'expected_element_type_list'
        # Tuple = 'target_variable_tup'
        # String = 'target_variable_str'
        # Integer = 'target_variable_int'
        # Boolean = 'target_variable_bool'
        # Argument Value = 'argument_name_value'
        # Other = 'targetvariable_expectation'

    ##### Class Variables #####
    class_name = 'FileManager'

    ##### Special Methods #####
    def __init__(self, root_path):
        self.attribute_list = ["ready", "name", "root", "directory", "parsers"]
        self.ready = False
        self.name = None
        self.root = os.path.join(root_path, "assets")
        self.directory = None
        self.parsers = None

    
    def __repr__(self):
        return f"< FileManager | Name: {self.name} >"

    ##### Getters and Setters #####
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_root(self, path):
        self.root = path

    def get_root(self):
        return self.root

    def set_directory(self, directory_obj):
        self.directory = directory_obj       

    def get_directory(self):
        return self.directory

    def set_parsers(self, parser_dict):
        self.parsers = parser_dict

    def get_parsers(self):
        return self.parsers

    ##### Attribute Methods #####

    # Return the attributes of this object as a dictionary
    def to_dict(self):
        # The keys of the following dictionary are the names of this object's properties
        # The values of the following dictionary are the values of this object's properties
        attribute_dict = {
            "attribute_list":self.attribute_list,
            "name": self.name,
            "ready": self.ready,
            "root": self.root,
            "directory":self.directory,
            "parsers": self.parsers
        }

        return attribute_dict

    # Set the value of a single attribute of this object
    def set_attribute(self, attribute_name, attribute_value):
        # The list in the following loop contains the names of all attributes of this object
        for attribute in self.attribute_list:
            if attribute == attribute_name:
                setattr(self, attribute, attribute_value)
                break

    # Set the value of one or more attributes of this object
    def set_attributes(self, attribute_data_dict):
        for attribute in self.attribute_list:
            if attribute in attribute_data_dict:
                setattr(self, attribute, attribute_data_dict[attribute])

    def change_root(self, path):
        self.set_root(path)
        self.start_directory()

    def add_parser(self, parser_obj):
        self.parsers[parser_obj.get_name()] = parser_obj

    def remove_parser(self, parser_name):
        del self.parsers[parser_name]

    def get_parser(self, parser_name):
        return self.get_parsers()[parser_name]

    ##### Utility Methods #####
    def structure_directory(self, directory_obj):
        directory_dict = {}
        file_dict = {}
        for item in directory_obj.get_content():
            item_path = os.path.join(directory_obj.get_path(), item)
            if os.path.isfile(item_path):
                file_dict[item] = item_path
            
            if os.path.isdir(item_path):
                new_directory_obj = FMDirectory(item, item_path)
                directory_dict[new_directory_obj.get_name()] = new_directory_obj

        directory_obj.set_files(file_dict)
        directory_obj.set_directories(directory_dict)

        for dir_obj in directory_obj.get_directories().values():
            self.structure_directory(dir_obj)

    def start_directory(self):
        # Check for an assets directory.
        # If one does not exist, create one
        if not os.path.isdir(self.root):
            os.mkdir(self.root)
        # Check directory property for a FMDirectory object.
        if type(self.directory) is not FMDirectory:
            directory_path = self.root
            self.directory = FMDirectory("assets", directory_path)

        self.structure_directory(self.directory)

    def default_directory(self):
        assets_directory = FMDirectory("assets", self.root)
        self.set_directory(assets_directory)

        subdir_names = ["images", "audio", "data", "models", "other"]
        for subdir_name in subdir_names:
            self.directory.add_item(subdir_name)

        self.start_directory()

    def clear_directory(self, directory_obj):
        directory_clear = False
        while not directory_clear:
            # Check the contents of the directory
            directory_content = os.listdir(directory_obj.path)
            if not directory_content:
                directory_clear = True
                print("Directory Emptied")
                break
            else:
                for root, directories, files in os.walk(directory_obj.path):
                    print(f"Scanning Directory: {root}\n")
                    for item_name in files:
                        print(f"File Name: {item_name}")
                        item_path = os.path.join(directory_obj.path, item_name)
                        print(f"File Path: {item_path}")
                        try:
                            os.remove(item_path)
                            print(f"Deleted: {item_name}")
                        except OSError as e:
                            print("Error: %s : %s" % (item_path, e.strerror))
                    for item_name in directories:
                        print(f"Directory Name: {item_name}")
                        item_path = os.path.join(directory_obj.path, item_name)
                        print(f"Directory Path: {item_path}")
                        if os.listdir(item_path):
                            print("Directory Not Empty ... Clearing Directory")
                            self.clear_directory(item_path)
                        else:
                            try:
                                os.rmdir(item_path)
                                print(f"Deleted: {item_name}")
                            except OSError as e:
                                print("Error: %s : %s" % (item_path, e.strerror))

        self.structure_directory(self.directory)

    def remove_directory(self, directory_obj):
        self.clear_directory(directory_obj)
        os.rmdir(directory_obj.path)
        self.structure_directory(self.directory)

    ##### Primary Methods #####

    def create_package(self):
        pass

    def start(self):
        if self.directory == None:
            self.default_directory()
