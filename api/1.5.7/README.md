# Application level API 1.5.7

## Installation instructions


1. unzip 1.5.7.7z to your plugin folder
2. put the following code line as first line in your application level python code

`import cast_upgrade_1_5_7 # @UnusedImport`


## What's new

### Features

- load_violations on objects by sub-query loading
- postgresql get_size on schema
- faster table reflection (by embedding statically the schema)
- managment : lazy loading

### Bug corrections

- corrects issue on save_violation
- better ms connection support
- save_property : also clean external objects (caused bug on html5, ...)
- several calls to update csv on sql server crash
- sqlserver issue on raw saving
- log level based on CMS option : corrects a bug on take a snapshot

See full doc ...
