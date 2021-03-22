# Import Required Packages


# 'ModelManager' is the main object of this file.
# All code in this file relates directly to the 'ModelManager' object.
class ModelManager:
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
    class_name = 'ModelManager'

    ##### Special Methods #####
    def __init__(self):
        self.attribute_list = ["name", "ready"]
        self.ready = False
        self.name = None

    
    def __repr__(self):
        return "< ModelManager | Name: {self.name} >"

    ##### Getters and Setters #####
    def set_ready(self, ready_bool):
        self.ready = ready_bool

    def get_ready(self):
        return self.ready

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    ##### Attribute Methods #####

    # Return the attributes of this object as a dictionary
    def to_dict(self):
        # The keys of the following dictionary are the names of this object's properties
        # The values of the following dictionary are the values of this object's properties
        attribute_dict = {
            "attribute_list":self.attribute_list,
            "name": self.name,
            "ready": self.ready,
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

    ##### Primary Methods #####
