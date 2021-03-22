from .main import AssetLibrary

def new():
    new_object = AssetLibrary()
    return new_object

def new_default():
    new_object = AssetLibrary()
    new_object.set_default()
    return new_object

# Check object readiness, then run the 'main' method
# Start Settings:
    # 'standard' = check object readiness -> run the main method
    # 'default' = set the object's default attributes -> run the 'main' method
    # 'force' = run the main method (does NOT check for readiness)
def start(start_setting='standard', target_obj=None):
    main_obj = target_obj
    # If no target object is given, create an instance of 'AssetLibrary' to target
    if main_obj == None:
        main_obj = AssetLibrary()

    print(f'Start: {main_obj.class_name}.main()')

    # Standard Start
    if start_setting == 'standard':
        if main_obj.get_ready() == True:
            main_obj.main()
        else:
            print(f'{main_obj.name} is not ready to start.')
    # Start with AssetLibrary's default attributes
    elif start_setting == 'default':
        main_obj.default_start()
    # Start without checking for readiness
    elif start_setting == 'force':
        main_obj.main()

    print(f'End: {main_obj.class_name}.main()')
