import cast.analysers.dotnet
import cast.analysers.log


class MyExtension(cast.analysers.dotnet.Extension):

    def start_analysis(self, options):
        cast.analysers.log.debug('Hello World!!')
