import cast.analysers.jee
from cast.analysers import log


class J2EEParam(cast.analysers.jee.Extension):
    
    def start_analysis(self, options):
        
        """ 
        add param on java.sql.Statement.executeQuery
        
        We are saying that we are interested in all call to java.sql.Statement.executeQuery and for those call 
        we want to have the possible values of the 1 parameter 
        When this value is computed, my_callback(..) will be called back with all necessary informations
        
        """ 
        options.add_parameterization("java.sql.Statement.executeQuery(java.lang.String)", [1], self.my_callback)
        options.add_parameterization("Template.execute(java.lang.String)", [1], self.my_callback2)
        

    def my_callback(self, values, caller, line, column):
        
        log.debug("Method %s is calling java.sql.Statement.executeQuery at line %s with the following possible values for parameter 1" % (str(caller.get_fullname()), str(line)))
        for value in values[1]:
            log.debug("  %s" % str(value))
        
    def my_callback2(self, values, caller, line, column):
        
        log.debug("Method %s is calling ... at line %s with the following possible values for parameter 1" % (str(caller.get_fullname()), str(line)))
        for value in values[1]:
            log.debug("  %s" % str(value))
        
        
