# Import Required Packages
import os

# 'FMDirectory' is the main object of this file.
# All code in this file relates directly to the 'FMDirectory' object.
class FMDirectory:
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
    class_name = 'FMDirectory'

    ##### Special Methods #####
    def __init__(self, name, path, hidden=[]):
        self.attribute_list = ["ready", "name", "path", "content", "directories", "files"]
        self.ready = False
        self.name = name
        self.path = path
        self.hidden = hidden
        self.content = os.listdir(self.path)
        self.directories = {}
        self.files = {}

    
    def __repr__(self):
        return f"< FMDirectory | Name: {self.name} >"

    ##### Getters and Setters #####
    def set_ready(self, ready_bool):
        self.ready = ready_bool

    def get_ready(self):
        return self.ready

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path
    
    def set_hidden(self, name_list):
        self.hidden = name_list

    def get_hidden(self):
        return self.hidden

    def set_content(self):
        all_content = os.listdir(self.path)
        visible_content = [element for element in all_content if element not in self.hidden]
        self.content = visible_content

    def get_content(self):
        return self.content

    def set_directories(self, directory_dict):
        self.directories = directory_dict

    def get_directories(self):
        return self.directories

    def set_files(self, files_list):
        self.files = files_list

    def get_files(self):
        return self.files

    ##### Attribute Methods #####

    # Return the attributes of this object as a dictionary
    def to_dict(self):
        # The keys of the following dictionary are the names of this object's properties
        # The values of the following dictionary are the values of this object's properties
        attribute_dict = {
            "attribute_list":self.attribute_list,
            "ready": self.ready,
            "name": self.name,
            "path": self.path,
            "directories":self.directories,
            "files":self.files
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

    ##### Utility Methods #####
    # Create a dictionary of information about a directory
    def get_info(self, directory_path):
        info_dict = {}
        content = os.listdir(directory_path)
        directories = [directory for directory in content if os.path.isdir(os.path.join(directory_path, directory))]
        files = [filename for filename in content if os.path.isfile(os.path.join(directory_path, filename))]

        info_dict["path"] = directory_path
        info_dict["directories"] = directories
        info_dict["files"] = files

        return info_dict

    def add_item(self, item_name, hide=False):
        new_item_path = os.path.join(self.path, item_name)
        if not os.path.exists(new_item_path):
            os.mkdir(new_item_path)
        else:
            print(f"{item_name} already exists")
        if hide:
            self.hidden.append(item_name)
        self.set_content()
        

    ##### Primary Methods #####