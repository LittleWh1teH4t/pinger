@echo off
title ("Welcome Will! Booting Again?")
color 4
cls                                                                                                       
ECHO 88888888ba   88  888b      88    ,ad8888ba,     d8'  88888888888  88888888ba,    
ECHO 88      "8b  88  8888b     88   d8"'    `"8b   d8'   88           88      `"8b   
ECHO 88      ,8P  88  88 `8b    88  d8'            ""     88           88        `8b  
ECHO 88aaaaaa8P'  88  88  `8b   88  88                    88aaaaa      88         88  
ECHO 88""""""'    88  88   `8b  88  88      88888         88"""""      88         88  
ECHO 88           88  88    `8b 88  Y8,        88         88           88         8P  
ECHO 88           88  88     `8888   Y8a.    .a88         88           88      .a8P   
ECHO 88           88  88      `888    `"Y88888P"          88888888888  88888888Y"'    
ECHO                                 Coded by: LittleWh1te H4t                  "'    
@echo off
:reboot
echo off                                                                                 
set /p IP=Enter Little Shits IP:
:top
PING -n 1 %IP% | FIND "TTL="
IF ERRORLEVEL 1 (SET in=B & echo get booted fag )
color %OUT%
ping -t 2 0 10 127.0.1 >nul
:loop
color 3
timeout 0 >nul
:loop
color 4
timeout 0 >nul
color 5
timeout 0 >nul
color 9 
timeout 0 >nul
color 1
timeout 0 >nul

@echo off
goto top
goto reboot
