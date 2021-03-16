from cast import Event
from cast.analysers import ua
from interpreter import Interpreter

        
class Html5Diag(ua.Extension):

    def __init__(self):
        pass
        
    def start_analysis(self):
        pass

    @Event('com.castsoftware.html5', 'add_quality_rules')
    def add_quality_rules(self, externalQualityRules):

        interpreter = Interpreter()
        externalQualityRules.add_interpreter(interpreter, self.get_plugin())
