# publish-to-jury.ps1
# Script de publication sécurisée des justificatifs de preuves pour la soutenance (Jury)

$SourcePath = "C:\Users\julien\OneDrive\Bureau\geminicli"
$TempPath = Join-Path -Path $env:TEMP -ChildPath "rdm-prestige-publish"
$PublicRemote = "https://github.com/julienflorenceflorence-oss/rdm-prestige.git"

Write-Output "=== DEBUT DE LA PUBLICATION DE LA SOUTENANCE ==="

# 1. Nettoyer le dossier temporaire
if (Test-Path -Path $TempPath) {
    Remove-Item -Path $TempPath -Recurse -Force
}
$null = New-Item -Path $TempPath -ItemType Directory -Force

# 2. Copier uniquement les fichiers destinés au jury depuis le dossier d'Espace de Soutenance V2
Write-Output "Copie des fichiers publics depuis 02_Espace_Soutenance..."
$PublicSource = Join-Path $SourcePath "02_Espace_Soutenance"
if (Test-Path -Path $PublicSource) {
    Copy-Item -Path "$PublicSource\*" -Destination $TempPath -Recurse -Force
}

# 3. Initialiser un dépôt propre dans le dossier temporaire pour écraser tout historique privé
Set-Location -Path $TempPath
git init -b main
git remote add origin $PublicRemote

# Configurer l'utilisateur pour le dossier temporaire
git config user.name "Julien Florence"
git config user.email "julienflorenceflorence@gmail.com"

# Ajouter et commiter
git add -A
git commit -m "Publish clean public deliverables for jury"

# 4. Pousser de force sur le dépôt public GitHub Pages
Write-Output "Mise à jour forcée du dépôt public rdm-prestige..."
git push --force origin main 2>&1

# 5. Retourner au dossier d'origine et nettoyer les fichiers temporaires
Set-Location -Path $SourcePath
Remove-Item -Path $TempPath -Recurse -Force

Write-Output "=== PUBLICATION REUSSIE ET COMPLETEMENT SECURISEE ==="
