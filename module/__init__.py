from .main import AssetLibrary

# Return an 'AssetLibrary' object without running any methods
def new():
    new_object = AssetLibrary()
    return new_object

# If no 'AssetLibrary' is given, instatiate one, then run its 'main' method
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
        main_obj.start()
    # Start with AssetLibrary's default attributes
    elif start_setting == 'default':
        main_obj.set_default()
        main_obj.start()
    # Start without checking for readiness
    elif start_setting == 'force':
        main_obj.main()

    print(f'End: {main_obj.class_name}.main()')
