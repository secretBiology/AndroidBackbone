@echo off
set /P id=Enter package name (e.g. com.example.package) :
if not defined id (
	echo WARNNING: empty package name will raise error
) else (
	rmdir /S /Q output
)
echo ====== script started at %TIME%
python main.py %id%
echo ====== script ended at %TIME%
set /p DUMMY=Hit ENTER to exit...