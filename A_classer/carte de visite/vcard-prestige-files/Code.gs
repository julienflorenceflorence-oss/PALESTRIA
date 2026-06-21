/**
 * CONFIGURATION DE VOTRE CARTE
 * 1. Créez un Google Sheet avec deux onglets : "Config" et "Tracking"
 * 2. Copiez l'ID de votre Sheet (dans l'URL entre /d/ et /edit)
 * 3. Collez l'ID ci-dessous entre les guillemets
 */
const SPREADSHEET_ID = 'VOTRE_ID_GOOGLE_SHEET_ICI'; 

/**
 * Affiche la carte de visite (Frontend)
 */
function doGet(e) {
  // Vérification de la configuration
  if (SPREADSHEET_ID === 'VOTRE_ID_GOOGLE_SHEET_ICI') {
    return HtmlService.createHtmlOutput("<h1>Erreur de Configuration</h1><p>Veuillez configurer votre SPREADSHEET_ID dans le fichier Code.gs.</p>");
  }

  // API JSON pour récupérer les données (utilisée par le frontend)
  if (e.parameter.get === 'data') {
    return ContentService.createTextOutput(JSON.stringify(getCardData()))
      .setMimeType(ContentService.MimeType.JSON);
  }
  
  // Rendu de la page HTML
  return HtmlService.createTemplateFromFile('index')
    .evaluate()
    .setTitle('Julien FLORENCE - CERCLE ORIGINE')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

/**
 * Enregistre le scan ou une action dans l'onglet 'Tracking'
 */
function doPost(e) {
  try {
    const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    const sheet = ss.getSheetByName('Tracking');
    
    if (!sheet) {
      return ContentService.createTextOutput("Error: Onglet 'Tracking' non trouvé").setMimeType(ContentService.MimeType.TEXT);
    }

    const data = JSON.parse(e.postData.contents);
    const now = new Date();
    
    sheet.appendRow([
      Utilities.formatDate(now, "GMT+1", "dd/MM/yyyy"),
      Utilities.formatDate(now, "GMT+1", "HH:mm:ss"),
      data.userAgent || 'Inconnu',
      data.action || 'Ouverture'
    ]);
    
    return ContentService.createTextOutput("Success").setMimeType(ContentService.MimeType.TEXT);
  } catch(err) {
    console.error(err);
    return ContentService.createTextOutput("Error: " + err.message).setMimeType(ContentService.MimeType.TEXT);
  }
}

/**
 * Récupère les données de configuration depuis l'onglet 'Config'
 */
function getCardData() {
  try {
    const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    const sheet = ss.getSheetByName('Config');
    
    if (!sheet) return { error: "Onglet 'Config' non trouvé" };
    
    const rows = sheet.getDataRange().getValues();
    const data = {};
    
    // On boucle sur les lignes pour créer l'objet data (clé = Paramètre, valeur = Valeur)
    for (let i = 1; i < rows.length; i++) {
      if (rows[i][0]) {
        data[rows[i][0].toString().trim()] = rows[i][1];
      }
    }
    return data;
  } catch (err) {
    console.error(err);
    return { error: err.message };
  }
}
