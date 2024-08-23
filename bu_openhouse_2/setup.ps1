# Set the Python version and download URL
$pythonVersion = "3.11.5"
$pythonInstallerUrl = "https://www.python.org/ftp/python/$pythonVersion/python-$pythonVersion-amd64.exe"

# Download Python installer
$installerPath = "$env:TEMP\python-installer.exe"
Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $installerPath

# Install Python with default settings and add it to PATH
Start-Process -FilePath $installerPath -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

# Verify Python installation
python --version

# Upgrade pip
python -m ensurepip --upgrade
python -m pip install --upgrade pip

# Install required Python packages
python -m pip install flask flask_sqlalchemy werkzeug

# Clone the GitHub repository to the Desktop
$desktopPath = [Environment]::GetFolderPath("Desktop")
$repoUrl = "https://github.com/ITPATJIDR/Bu_openhouse.git"
git clone $repoUrl $desktopPath\Bu_openhouse

# Clean up installer
Remove-Item $installerPath -Force
