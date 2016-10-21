'''
Created on 16 juin 2015

@author: MRO
'''
import cast.analysers.jee
from cast.analysers import log


class JEEAllEvents(cast.analysers.jee.Extension):
    """
    Logs all jee callbacks
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
        """
        Called at the beginning of analysis

        :param cast.analysers.JEEExecutionUnit options: analysis option

        @type options: cast.analysers.JEEExecutionUnit
        """
        self.display('start_analysis')
        self.increase_indent()
        
        # allow to 'see' our xml file see http://cast-projects.github.io/Extension-SDK/doc/analysers_specif.html#manipulating-options
        options.handle_xml_with_xpath('//DATA')
        

    def start_web_xml(self, file):
        """
        Called at the beginning of the analysis of the web.xml file

        :param cast.analysers.File file: web.xml file

        @type file: cast.analysers.File
        """
        self.display('start_web_xml ' + str(file))
        self.increase_indent()

    def end_web_xml(self, file):
        """
        Called at the end of the analysis of the web.xml file

        :param cast.analysers.File file: web.xml file

        @type file: cast.analysers.File
        """
        self.decrease_indent()
        self.display('end_web_xml ' + str(file))

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

    def start_xml_files(self):
        """
        Called at the beginning of the xml files analysis.
        """
        self.display('start_xml_files')
        self.increase_indent()

    def start_xml_file(self, file):
        """
        Called at the beginning of the analysis of a specific xml file.

        :param cast.analysers.File file: visited xml file

        @type file: cast.analysers.File
        """
        self.display('start_xml_file ' + str(file))
        self.increase_indent()

    def end_xml_file(self, file):
        """
        Called at the end of the analysis of a specific xml file.

        :param cast.analysers.File file: visited xml file

        @type file: cast.analysers.File
        """
        self.decrease_indent()
        self.display('end_xml_file ' + str(file))

    def end_xml_files(self):
        """
        Called at the end of the xml files analysis.
        """
        self.decrease_indent()
        self.display('end_xml_files')

    def start_web_files(self):
        """
        Called at the beginning of the web files analysis.
        """
        self.display('start_web_files')
        self.increase_indent()

    def start_web_file(self, file):
        """
        Called at the beginning of the analysis of a specific Web file.

        :param cast.analysers.File file: visited web file

        @type file: cast.analysers.File
        """
        self.display('start_web_file ' + str(file))
        self.increase_indent()

    def end_web_file(self, file):
        """
        Called at the end of the analysis of a specific Web file.

        :param cast.analysers.File file: visited web file

        @type file: cast.analysers.File
        """
        self.decrease_indent()
        self.display('end_web_file ' + str(file))

    def end_web_files(self):
        """
        Called at the end of the web files analysis.
        """
        self.decrease_indent()
        self.display('end_web_files')

    def end_analysis(self):
        """
        Called at the end of analysis
        """
        self.decrease_indent()
        self.display('end_analysis')
