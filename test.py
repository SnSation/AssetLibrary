import module as assetlib

# assetlib.start('default')

testlib = assetlib.new()

# testlib.default_start()

# testlib.create_directory()
testlib.start_directories()
# testlib.default_asset_location()
# print(testlib.get_asset_location())
testlib.default_asset_paths()
print(testlib.check_ready())
for k,v in testlib.asset_paths.items():
    print(f"{k} --- {v}")