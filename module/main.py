# Import Required Packages
import os
from .utils import FileManager, ModelManager


# 'AssetManager' is the main object of this file.
# All code in this file relates directly to the 'AssetManager' object.
class AssetManager:
    # Sections:
        # 1. Class Variables
        # 2. Special Methods
        # 3. Getters and Setters
        # 4. Attribute Methods
        # 5. Directory Methods
        # 6. Image Methods
        # 7. Audio Methods

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
    class_name = 'AssetManager'

    ##### Special Methods #####
    def __init__(self):
        self.attribute_list = ["name", "ready", "assets"]
        self.name = None
        self.ready = False
        self.paths = None
        self.root = os.path.dirname(os.path.abspath(__file__))
        self.model_manager = None
        self.file_manager = FileManager(self.root)

    
    def __repr__(self):
        return f'< AssetManager | Name: {self.name} >'

    ##### Getters and Setters #####
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_ready(self, ready_bool):
        self.ready = ready_bool

    def get_ready(self):
        return self.ready

    def set_paths(self, paths_dict):
        self.paths = paths_dict

    def get_paths(self):
        return self.paths

    def set_root(self, root_path):
        self.root = root_path

    def get_root(self):
        return self.root

    def set_model_manager(self, model_manager_obj):
        self.models = model_manager_obj

    def get_model_manager(self):
        return self.models

    def set_file_manager(self, file_manager_obj):
        self.files = file_manager_obj

    def get_file_manager(self):
        return self.file_manager

    ##### Attribute Methods #####

    # Return the attributes of this object as a dictionary
    def to_dict(self):
        # The keys of the following dictionary are the names of this object's properties
        # The values of the following dictionary are the values of this object's properties
        attribute_dict = {
            "attribute_list":self.attribute_list,
            "name": self.name,
            "ready": self.ready,
            "paths": self.paths
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

    def default_name(self):
        self.name = "Default"

    def default_ready(self):
        self.ready = False

    def default_paths(self):
        self.file_manager.default_paths()

    ##### Directory Methods #####

    def start_directories(self):
        # Check the current asset location.
        # If it is incorrect, create a usable path
        if self.paths == None:
            print("Creating Default Paths")
            self.default_paths()
        elif not os.path.isdir(self.paths["assets"]):
            # Create the 'assets' directory
            current_parent = os.path.dirname(self.paths["assets"])
            self.paths["assets"] = os.path.join(current_parent, "assets")
            os.mkdir(self.paths["assets"])

            # Create Required Subdirectories
            subdirectory_list = ["images", "audio", "data", "models", "other"]
            for subdirectory in subdirectory_list:
                self.paths[subdirectory] = os.path.join(self.paths["assets"], subdirectory)
                os.mkdir(self.paths[subdirectory])

    def check_directories(self):
        required_directories = ["assets", "images", "audio", "data", "models", "other"]
        try:
            # Check if the asset directories exist
            for directory in required_directories:
                if directory not in self.paths.keys():
                    print(f"{directory} not in asset path dictionary")
                    return False
                elif os.path.exists(self.paths[directory]) == False:
                    print(f"{directory} is missing from path")
                    return False
                else:
                    print(f"{directory} - OK | {self.paths[directory]}")
        
            print("Directories Ready")
            return True
        except:
            print("Path Error: Try using the 'start_directories', 'default_paths', or 'set_default' methods.")
            return False

    ##### Image File Methods #####

    ##### Audio File Methods #####

    ##### Model File Methods #####
    # Return the attributes of an object
    def get_object_state(self, some_obj):
        pass

    # Write an object's current state to a file
    def save_object(self, some_obj):

        pass
    
    # Load Classes from files in the 'models' directory for use as blueprints:
    def load_blueprints(self):
        pass

    ##### 'Other' File Methods #####

    ##### Primary Methods #####
    def main(self):
        print(f"Running {self.name}'s main method")

    # Run all ready checks.
    # If all pass, set the ready flag to True
    def check_ready(self):
        checks = [
            ("Directories", self.check_directories())
            ]
        for check in checks:
            if check[1] == False:
                print(f"{check[0]} not ready")
        self.ready = all(flag == True for (_, flag) in checks)
        return self.ready
    
    # Check for readiness.
    # If ready, run the 'main' method.
    def start(self):
        # Check object readiness
        if self.check_ready():
            self.main()
        else:
            print(f'{self.name} is not ready to start.')

    # Set all default attributes
    def set_default(self):
        self.default_name()
        self.default_ready()
        self.default_paths()
        self.start_directories()

        # Set 'self.ready' to 'True'
        self.set_ready(True)



