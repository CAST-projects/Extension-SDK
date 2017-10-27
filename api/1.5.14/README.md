# Application level API 1.5.14

## Installation instructions


1. unzip 1.5.14.7z to your plugin folder
2. put the following code line as first line in your application level python code

`import cast_upgrade_1_5_14 # @UnusedImport`

See full doc http://cast-projects.github.io/Extension-SDK/doc/application_level.html

## What's new

* test api for application level : allow some test metamodel inside the test dubsolder : name them xxxMetaModelTest.xml

### Bug corrections

* cast.application.test.run did not launch anymore
* links created during end_application and marked as not sure where not visible in DLM 
