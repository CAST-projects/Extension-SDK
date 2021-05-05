from cast import Event
from cast.analysers import ua, log
from interpreters import SimpleInfoPrint, RuleAllContainingOnlyStrings

        
class PythonQualityRule(ua.Extension):
    """
    UA extension that injects additional quality rules
    to 'com.castsoftware.python' analyzer.
    """

    def __init__(self):
        pass
        
    def start_analysis(self):
        pass

    @Event('com.castsoftware.python', 'add_quality_rules')
    def add_quality_rules(self, externalQualityRules):

        def add_rule(interpreter):
            """Add interpreter and current plugin for proper logging"""
            externalQualityRules.add_interpreter(interpreter, self.get_plugin())
            log.info("Added rule interpreter: {}".format(interpreter.__name__))

        # Add rule interpreters
        add_rule(SimpleInfoPrint)
        add_rule(RuleAllContainingOnlyStrings)
        ...

    @Event('com.castsoftware.python', 'finished_rule_analysis')
    def on_finished_rule_analysis(self):
        """
        Here one can perform post quality-rule analysis processing.
        Interpreter class attributes can be used to collect data
        from different analyzed modules.
        """
        log.info("[on_finished_rule_analysis]")

    def end_analysis(self):
        pass
