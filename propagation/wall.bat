reg add "HKEY_CURRENT_USER\control panel\desktop" /v wallpaper /t REG_SZ /d "" /f 
reg add "HKEY_CURRENT_USER\control panel\desktop" /v wallpaper /t REG_SZ /d "C:\Users\Administrator\Desktop\GOKU.jpg" /f
reg add "HKEY_CURRENT_USER\control panel\desktop" /v WallpaperStyle /t REG_SZ /d 2 /f
timeout 2>NUL
RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters 
timeout 3>NUL
exit
