import module as assetlib

# assetlib.start('default')

testlib = assetlib.new()
testlib.file_manager.default_directory()
print(testlib.file_manager)
print(testlib.file_manager.directory)
print(testlib.file_manager.directory.path)
print(testlib.file_manager.directory.directories)
testlib.file_manager.clear_directory(testlib.file_manager.directory.directories["testdir"])
print(testlib.file_manager.directory.directories)
testlib.file_manager.remove_directory(testlib.file_manager.directory.directories["testdir"])
print(testlib.file_manager.directory.directories)


# testlib.default_start()

# testlib.create_directory()
# testlib.start_directories()
# # testlib.default_asset_location()
# # print(testlib.get_asset_location())
# testlib.default_asset_paths()
# print(testlib.check_ready())
# for k,v in testlib.asset_paths.items():
#     print(f"{k} --- {v}")