# git-autocommit-autopush.ps1
# Script PowerShell de sauvegarde automatique vers GitHub (privé)

$RepoPath = "C:\Users\julien\OneDrive\Bureau\geminicli"
Set-Location -Path $RepoPath

# Journalisation automatique (déjà ignorée par .gitignore via *.log)
$LogFile = Join-Path -Path $RepoPath -ChildPath "git-autocommit-autopush.log"

function Write-Log {
    param([string]$Message)
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "[$Timestamp] $Message" | Out-File -FilePath $LogFile -Append
}

Write-Log "Démarrage du script de sauvegarde automatique Git."

while ($true) {
    try {
        # Vérifie s'il y a des modifications locales (fichiers modifiés, supprimés ou non suivis)
        $status = git status --porcelain
        if ($status) {
            Write-Log "Modifications détectées."
            
            # Ajout des fichiers
            git add -A 2>&1 | Out-String -Stream | ForEach-Object { Write-Log "git add: $_" }
            
            # Commit avec horodatage
            $CommitMessage = "Auto-backup: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
            git commit -m $CommitMessage 2>&1 | Out-String -Stream | ForEach-Object { Write-Log "git commit: $_" }
            
            # Push vers le dépôt distant sur la branche main
            git push origin main 2>&1 | Out-String -Stream | ForEach-Object { Write-Log "git push: $_" }
            
            Write-Log "Sauvegarde automatique effectuée avec succès."
        }
    }
    catch {
        Write-Log "Erreur lors de la boucle de sauvegarde : $_"
    }
    
    # Pause de 30 secondes avant la vérification suivante
    Start-Sleep -Seconds 30
}
