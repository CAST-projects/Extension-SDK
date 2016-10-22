All J2EE events
===============

Description
-----------

Allow to visualize the event sequence order.

See also documentation http://cast-projects.github.io/Extension-SDK/doc/analysers_specif.html#jee-analyser-specificities


Demo
----

Open tests/integration_test and press F9.

It should prints : 

  Info   : [param] Method CallDatabase.call is calling java.sql.Statement.executeQuery at line 19 with the following possible values for parameter 1
  Info   : [param]   select * from Client
  Info   : [param]   select * from Customer
  Info   : [param] Method CallDatabase.call is calling java.sql.Statement.executeQuery at line 22 with the following possible values for parameter 1
  Info   : [param]   select * from Client
  Info   : [param]   select * from Customer
  Info   : [param] Method CallDatabase.f2 is calling java.sql.Statement.executeQuery at line 27 with the following possible values for parameter 1
  Info   : [param]   DELETE FROM Client

