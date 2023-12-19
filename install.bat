echo off

:: Create the new environment
python -m venv GPT4
echo Environment 'GPT4' created.

:: Activate the environment
call GPT4\Scripts\activate.bat
echo Environment 'GPT4' activated.


:: Run install.py script
python install.py
echo Required packages installed.


:: Deactivate the environment
call GPT4\Scripts\deactivate.bat
echo Environment 'GPT4' deactivated.

:: Pause to keep the window open and view any output/error messages
pause