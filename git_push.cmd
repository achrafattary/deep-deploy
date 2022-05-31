@echo off
set /p UserInput= what is the commit desc ? : 



git add .
git commit -m %UserInput%
git push

pause