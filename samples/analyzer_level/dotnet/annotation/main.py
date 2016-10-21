from cast.analysers import log, external_link, filter, create_link
import cast.analysers.dotnet


def link_to_table(type_, table_name):

    # search all tables or views with table_name as name
    tables = external_link.find_objects(table_name, filter.tables_or_views)
    
    # the position of the link will be the position of the class
    position = type_.get_position()
    for table in tables:
        create_link('useLink', type_, table, position)
    
    
class Extension(cast.analysers.dotnet.Extension):
    """
    Handle links from classes to tables with System.Data.Linq.Mapping.TableAttribute
    """

    def start_type(self, type_):
        """
        @type type_: cast.analysers.Type
        """
        
        # iterate on annotations of the class
        for annotation in type_.get_annotations():
            
            
            # annotation is a structure, first element is the 'annotation class'
            annotationType = annotation[0]

            if annotationType.get_fullname() == 'System.Data.Linq.Mapping.TableAttribute':
                
                # now we can focus on parameters of the annotation 
                parameters = annotation[1]

                if 'Name' in parameters:
                    table_name = parameters['Name']
                else:
                    # default value when no parameter is provided...
                    table_name = type_.get_name()
                
                log.debug('firing link between ' + str(type_) + ' and ' + table_name)
                link_to_table(type_, table_name)

