# nvro_py
## Quick start using provided launch sripts
The application includes launch scripts for Linux and Windows (`launch.sh` and `launch.bat` respectively), these should activate the virtual python environment, check and install the required packages and finally execute the application.
These scripts are commonly executed by a double click on Windows, or right clicking and choosing run on Linux
If the provided scripts do not function as expected, one can also launch the application manually
## Manual Start
### If first-time install: Setting up the virtual environment
If installing the software for the first time in a directory, one has to first install the packages provided in `requirements.txt`
This is done *after* activating the virtual environment as described in the "Activating the virtual environment" section using
```
bash
pip install -r requirements.txt
``` 
### Activating the virtual environment
To start the readout software one has to first activate the python virtual environment.
To this end first ensure a shell is opened at the project path, commonly by using 
```
cd *insert install directory here*
```
If on Linux, the activation is then done by typing the shell command:
```
source venv/bin/activate
```
If on Windows, the equivalent command in batch would be:
```
venv\Scripts\activate.bat
```
Alternatively, if using PowerShell:
```
venv\Scripts\Activate.ps1
```
After this is done, to start the application simply run the shell command
```
python main.py
```
## Additional Notes
On Windows machines with restricted PowerShell execution policies it is advisable to use the batch command prompt.