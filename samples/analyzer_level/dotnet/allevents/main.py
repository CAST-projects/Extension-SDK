import cast.analysers.dotnet
from cast.analysers import log


class DotNetAllEvents(cast.analysers.dotnet.Extension):
    """
    Logs all dotnet callbacks
    """
    
    def __init__(self):
        self.indentation = 0
        
    def increase_indent(self):
        self.indentation += 1
    
    def decrease_indent(self):
        self.indentation -= 1

    def display(self, message):
        log.info(' '*self.indentation + message)
        
        
    def start_analysis(self, options):
        self.display('start_analysis')
        self.increase_indent()
        
    def start_project(self, project):
        self.display('start_project ' + str(project))
        self.increase_indent()

    def introducing_file(self, file):
        self.display('introducing_file ' + str(file))

    def start_types(self):
        """
        Begin visit of classes, intefaces, etc..
        """
        self.display('start_types')
        self.increase_indent()

    def start_type(self, _type):
        """
        Called on each class, interface, etc...

        :param cast.analysers.Type _type: visited class

        @type _type: cast.analysers.Type
        """
        self.display('start_type ' + str(_type))
        self.increase_indent()

    def start_member(self, member):
        """
        Called on each class member field, method etc...

        :param cast.analysers.Member member: visited member

        @type member: cast.analysers.Member
        """
        self.display('start_member ' + str(member))
        self.increase_indent()

    def end_member(self, member):
        """
        Called on each class member field, method etc...

        :param cast.analysers.Member member: visited member

        @type member: cast.analysers.Member
        """
        self.decrease_indent()
        self.display('end_member ' + str(member))

    def end_type(self, _type):
        """
        Called on each class, interface, etc...

        :param cast.analysers.Type _type: visited class

        @type _type: cast.analysers.Type
        """
        self.decrease_indent()
        self.display('end_type ' + str(_type))

    def end_types(self):
        """
        End visit of classes, intefaces, etc..
        """
        self.decrease_indent()
        self.display('end_types')

    def start_files(self):
        self.display('start_files')
        self.increase_indent()

    def start_file(self, file):
        self.display('start_file ' + str(file))
        self.increase_indent()

    def end_file(self, file):
        self.decrease_indent()
        self.display('end_file ' + str(file))

    def end_files(self):
        self.decrease_indent()
        self.display('end_files')

    def end_project(self):
        self.decrease_indent()
        self.display('end_project')

    def end_analysis(self):
        """
        Called at the end of analysis
        """
        self.decrease_indent()
        self.display('end_analysis')
