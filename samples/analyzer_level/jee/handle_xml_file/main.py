import cast.analysers.jee
from cast.analysers import log


class HandleXMLFile(cast.analysers.jee.Extension):
    
    def start_analysis(self, options):
        
        # register a new type of xml file to be handled by analyzer
        options.handle_xml_with_xpath('/root')

    def start_xml_file(self, file):
        # we get it + all other xml files
        log.info("We have access to this xml file " + str(file))
        
