@echo off
@SetLocal EnableDelayedExpansion
@for %%a in (%0) do set CMDDIR=%%~dpa
java -cp "%CMDDIR%\*" -jar "%CMDDIR%\MetricsCompilerCLI.jar" %*