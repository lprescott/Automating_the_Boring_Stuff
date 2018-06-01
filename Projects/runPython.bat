rem This batch file calls py.exe on the first argument supplied.

set arg1=%1
@py.exe %arg1% %*
