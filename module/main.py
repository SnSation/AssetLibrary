# Import Required Packages


# 'AssetLibrary' is the main object of this file.
# All code in this file relates directly to the 'AssetLibrary' object.
class AssetLibrary:
    # Sections:
        # 1. Class Variables
        # 2. Special Methods
        # 3. Getters and Setters
        # 4. Attribute Methods
        # 5. Utility Methods
        # 6. Main Method
        # 7. Primary Methods

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
        self.name = None
        self.ready = False
    
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

    ##### Attribute Methods #####

    # Return the attributes of this object as a dictionary
    def to_dict(self):
        # The keys of the following dictionary are the names of this object's properties
        # The values of the following dictionary are the values of this object's properties
        attribute_dict = {
            "name": self.name,
        }

        return attribute_dict

    # Set the value of a single attribute of this object
    def set_attribute(self, attribute_name, attribute_value):
        # The list in the following loop contains the names of all attributes of this object
        for attribute in ["name"]:
            if attribute == attribute_name:
                setattr(self, attribute, attribute_value)
                break

    # Set the value of one or more attributes of this object
    def set_attributes(self, attribute_data_dict):
        for attribute in ["name"]:
            if attribute in attribute_data_dict:
                setattr(self, attribute, attribute_data_dict[attribute])

    # Set up default attributes for this object and set the 'ready' attribute
    def set_default(self):
        # Create a dictionary with this object's attributes as keys
        default_attributes = {
            'name': 'Default'
        }
        self.set_attributes(default_attributes)

        # Set 'self.ready' to 'True'
        self.set_ready(True)

    ##### Utility Methods #####


    ##### Main Method #####
    def main(self):
        print(f"Running {self.name}'s main method")
    
    ##### Primary Methods #####

    # Check for readiness.
    # If ready, run the 'main' method.
    def start(self):
        # Check object readiness
        if self.get_ready():
            self.main()
        else:
            print(f'{self.name} is not ready to start.')

    # Set default attributes and run the 'main' method
    def default_start(self):
        self.set_default()
        self.main()



