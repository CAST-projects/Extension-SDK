Handle a new type of XML file for J2EE
======================================

Description
-----------

J2EE analyzer does not create object for XML file not explicitly declared as handled.
This sample demonstrate usage of API to register some XML files to be 'handled'.

Basically here we inform J2EE analyzer to consider any XML file that satisfy an xpath pattern.
Then we can receive that file, plus all others during callback start_xml_file. 

See : http://cast-projects.github.io/Extension-SDK/doc/analysers_specif.html#manipulating-options

Demo
----

Open tests/test and press F9.
