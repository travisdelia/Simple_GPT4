@echo off
:: Activate the environment
call GPT4\Scripts\activate.bat
echo Environment 'GPT4' activated.
echo Running GPT_Simple 
python CurrentBuild.py
echo process complete
pause
:: Deactivate the environment
call GPT4\Scripts\deactivate.bat
echo Environment 'GPT4' deactivated.
pause



