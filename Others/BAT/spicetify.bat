@echo off
powershell.exe -command "iwr -useb https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.ps1 | iex"
start "" "C:\Users\manav\AppData\Roaming\Spotify\Spotify.exe"
exit