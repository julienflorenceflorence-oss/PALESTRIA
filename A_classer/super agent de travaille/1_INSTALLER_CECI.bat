@echo off
echo [1/3] Installation de Python...
winget install -e --id Python.Python.3.12 --silent --accept-package-agreements --accept-source-agreements

echo [2/3] Installation de l'environnement virtuel et de Playwright...
python -m pip install --upgrade pip --quiet
pip install playwright --quiet

echo [3/3] Installation des navigateurs pour l'automatisation...
playwright install chromium --with-deps

echo.
echo ✅ Installation terminee avec succes. Vous pouvez lancer le script Python.
pause
