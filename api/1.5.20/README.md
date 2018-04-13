# Application level API 1.5.20

## Installation instructions


1. unzip 1.5.20.7z to your plugin folder
2. put the following code line as first line in your application level python code and in your tests code

`import cast_upgrade_1_5_20 # @UnusedImport`

See full doc http://cast-projects.github.io/Extension-SDK/doc/application_level.html

## What's new

* corrects an issue on save_property for integer out of 32 bits integer range
* adds
  * AnalysisUnit.get_technologies()
  * AnalysisUnit.get_included_selection()
  * AnalysisUnit.get_excluded_selection()
