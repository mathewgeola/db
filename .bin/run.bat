@echo off

set VERSION=0.0.4

poetry version %VERSION%

for /f %%i in ('git merge-base HEAD origin/main') do set BASE=%%i

git reset %BASE%

git add -A

git commit -m "version = \"v%VERSION%\""

git push -f origin main

git tag v%VERSION%

git push origin v%VERSION%