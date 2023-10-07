@echo off
setlocal enabledelayedexpansion

:: Chemin par défaut vers 7z.exe
set "path7z=C:\Program Files\7-Zip\7z.exe"

:: Parcourir tous les dossiers du répertoire courant
for /d %%A in (*) do (
    :: Créer une archive pour chaque dossier
    "!path7z!" a -tzip "%%~nA.zip" "%%~nA\*"
)

:: Parcourir tous les fichiers ZIP dans le répertoire courant
for %%F in (*.zip) do (
    :: Retirer l'extension '.zip'
    set "name=%%~nF"
    :: Nouveau nom avec l'extension '.cbz'
    ren "%%F" "!name!.cbz"
)

endlocal
