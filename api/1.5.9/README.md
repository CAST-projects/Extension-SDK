# Application level API 1.5.9

## Installation instructions


1. unzip 1.5.9.7z to your plugin folder
2. put the following code line as first line in your application level python code

`import cast_upgrade_1_5_9 # @UnusedImport`


## What's new

### Features

* load_violations on objects by sub-query loading
* postgresql get_size on schema
* faster table reflection (by embedding statically the schema)
* managment : lazy loading
* ObjectQuery : 
  * in_projects() : restrict the projects to search into
  * in_set(<setid>/<set name>)
  * not_in_set()
  * is_web_service_call()
  * not_has_type(..)
  * not_in(query)
  * count() : return the number of objects
* Project.objects()
* Application.get_analyzer_technologies()
* LinkQuery : finer grain on DLM links queries
  * is_to_be_reviewed()
  * is_ignored()
  * is_not_ignored()
  * is_validated()
  * count() : return the number of links

### Bug corrections

* corrects issue on save_violation
* better ms connection support
* save_property : also clean external objects (caused bug on html5, ...)
* several calls to update csv on sql server crash
* sqlserver issue on raw saving
* log level based on CMS option : corrects a bug on take a snapshot
* exception during CastSchem.get_events()
* ObjectQuery.is_external() was giving objects external to one project but internal for others
* postgresql cache too cachy




See full doc http://cast-projects.github.io/Extension-SDK/doc/application_level.html
