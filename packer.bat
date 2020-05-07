@echo off
set program=%1
shift
pyarmor pack -e " --onefile" %program%
pause
