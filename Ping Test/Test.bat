@echo off
set /p url="Enter URL: "
set /p timeCount="Enter timeout: "
set /p logyn="Create log file? (Y/N): "

@REM echo "url: %url%" >> debug.txt
@REM echo "timeCount: %timeCount%" >> debug.txt
@REM echo "logyn: %logyn%" >> debug.txt

if "%logyn%" == "Y" (
echo "starting test with log file, press ctrl+c to stop"
echo "started at %Date% %Time%" >> "./log.txt"
ping -n %timeCount% %url% >> "./log.txt"
) else (
echo "starting test, press ctrl+c to stop"
ping -n %timeCount% %url%
)

echo "test finished"
pause