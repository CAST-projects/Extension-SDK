@echo off
@SetLocal EnableDelayedExpansion
@for %%a in (%0) do set CMDDIR=%%~dpa

:: ... command accepting options from call
java -cp "%CMDDIR%\*" -jar "%CMDDIR%\MetricsCompilerCLI.jar" %*

:: ... command with options ...
:: java -cp "%CMDDIR%\*" -jar "%CMDDIR%\MetricsCompilerCLI.jar" -encodeUA -inputdir . -outputdir .. -pck ADG_METRIC_TREE_PYTHON_RULES