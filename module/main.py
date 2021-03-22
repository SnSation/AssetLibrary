# Import Required Packages
import os


# 'AssetLibrary' is the main object of this file.
# All code in this file relates directly to the 'AssetLibrary' object.
class AssetLibrary:
    # Sections:
        # 1. Class Variables
        # 2. Special Methods
        # 3. Getters and Setters
        # 4. Attribute Methods
        # 5. Directory Methods
        # 6. Image Methods
        # 7. Audio Methods
        # 8. 

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
    class_name = 'AssetLibrary'

    ##### Special Methods #####
    def __init__(self):
        self.attribute_list = ["name", "ready", "assets"]
        self.name = None
        self.ready = False
        self.asset_paths = None
    
    def __repr__(self):
        return f'< AssetLibrary | Name: {self.name} >'

    ##### Getters and Setters #####
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_ready(self, ready_bool):
        self.ready = ready_bool

    def get_ready(self):
        return self.ready

    def set_asset_paths(self, paths_dict):
        self.asset_paths = paths_dict

    def get_asset_paths(self):
        return self.asset_paths

    ##### Attribute Methods #####

    # Return the attributes of this object as a dictionary
    def to_dict(self):
        # The keys of the following dictionary are the names of this object's properties
        # The values of the following dictionary are the values of this object's properties
        attribute_dict = {
            "attribute_list":self.attribute_list,
            "name": self.name,
            "ready": self.ready,
            "asset_paths": self.asset_paths
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

    def default_asset_paths(self):
        this_file = os.path.abspath(__file__)
        this_module = os.path.dirname(this_file)
        default_asset_paths = {}
        default_asset_paths["assets"] = os.path.join(this_module, "assets")

        subdirectory_list = ["images", "audio", "data", "models", "other"]
        for directory in subdirectory_list:
            default_asset_paths[directory] = os.path.join(default_asset_paths["assets"], directory)

        self.asset_paths = default_asset_paths

        for k, v in self.asset_paths.items():
            if not os.path.isdir(v):
                os.mkdir(v)
                print(f"{k} Directory Created")

    ##### Directory Methods #####
    
    def get_module_path(self):
        return os.path.dirname(os.path.abspath(__file__))

    def start_directories(self):
        # Check the current asset location.
        # If it is incorrect, create a usable path
        if self.asset_paths == None:
            print("Creating Default Paths")
            self.default_asset_paths()
        elif not os.path.isdir(self.asset_paths["assets"]):
            # Create the 'assets' directory
            current_parent = os.path.dirname(self.asset_paths["assets"])
            self.asset_paths["assets"] = os.path.join(current_parent, "assets")
            os.mkdir(self.asset_paths["assets"])

            # Create Required Subdirectories
            subdirectory_list = ["images", "audio", "data", "models", "other"]
            for subdirectory in subdirectory_list:
                self.asset_paths[subdirectory] = os.path.join(self.asset_paths["assets"], subdirectory)
                os.mkdir(self.asset_paths[subdirectory])

    def check_directories(self):
        required_directories = ["assets", "images", "audio", "data", "models", "other"]
        try:
            # Check if the asset directories exist
            for directory in required_directories:
                if directory not in self.asset_paths.keys():
                    print(f"{directory} not in asset path dictionary")
                    return False
                elif os.path.exists(self.asset_paths[directory]) == False:
                    print(f"{directory} is missing from path")
                    return False
                else:
                    print(f"{directory} - OK | {self.asset_paths[directory]}")
        
            print("Directories Ready")
            return True
        except:
            print("Path Error: Try using the 'start_directories', 'default_asset_paths', or 'set_default' methods.")
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
        self.default_asset_paths()
        self.start_directories()

        # Set 'self.ready' to 'True'
        self.set_ready(True)



