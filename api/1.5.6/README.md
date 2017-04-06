# Application level API 1.5.6

## Installation instructions


1. unzip 1.5.6.7z to your plugin folder
2. put the following code line as first line in your application level python code

`import cast_upgrade_1_5_6 # @UnusedImport`


## What's new

* saving several times the same property on teh same object triggers an exception earlier
* more resistance to bad sql queries
* log level (debug or not) is now aligned on CMS option
* correction of log issue with cast.application.test.run


See full doc ...
