import cast.analysers.ua
from cast.analysers import CustomObject

class MyLanguage(cast.analysers.ua.Extension):
    """
    Do something
    """
    
    def start_file(self, file):
        
        # we create one object under each file...
        o = CustomObject()
        o.set_type('MyLanguage_Object1')
        o.set_name('name1')
        o.set_parent(file)
        o.save()
