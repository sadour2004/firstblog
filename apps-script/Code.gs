/**
 * Die Centre — menu et dialogue formulaire.
 * Copiez ce fichier et Form.html dans l’éditeur Apps Script lié à votre classeur.
 */
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu("Die Center")
    .addItem("Nouveau ticket", "openForm")
    .addToUi();
}

function openForm() {
  const html = HtmlService.createHtmlOutputFromFile("Form")
    .setWidth(760)
    .setHeight(620);
  SpreadsheetApp.getUi().showModalDialog(html, "Die Centre Management");
}

function getOptions() {
  return {
    shifts: ["Matin", "Après-midi", "Nuit"],
    equipTypes: ["Imprimante", "Vérin", "Setup", "Appareil adhésif", "Autre"],
    actionTypes: ["Réparation", "Vérification", "Maintenance préventive", "Diagnostic"],
    status: ["Terminé", "En attente", "En cours"],
    techniciens: ["Tech A", "Tech B", "Tech C"]
  };
}

/** Colonnes Data : A dateHeure, B technicien, C shift, D reference, E typeEquipement, F typeAction, G duree, H statut */
var DATA_COLS = {
  DATE: 1,
  TECH: 2,
  SHIFT: 3,
  REF: 4,
  EQUIP: 5,
  ACTION: 6,
  DUREE: 7,
  STATUT: 8
};

function getDataSheet_() {
  const sh = SpreadsheetApp.getActive().getSheetByName("Data");
  if (!sh) throw new Error("La feuille 'Data' est introuvable.");
  return sh;
}

function rowToPayload_(row) {
  return {
    dateHeure: row[DATA_COLS.DATE - 1] != null ? String(row[DATA_COLS.DATE - 1]) : "",
    technicien: row[DATA_COLS.TECH - 1] != null ? String(row[DATA_COLS.TECH - 1]) : "",
    shift: row[DATA_COLS.SHIFT - 1] != null ? String(row[DATA_COLS.SHIFT - 1]) : "",
    reference: row[DATA_COLS.REF - 1] != null ? String(row[DATA_COLS.REF - 1]) : "",
    typeEquipement: row[DATA_COLS.EQUIP - 1] != null ? String(row[DATA_COLS.EQUIP - 1]) : "",
    typeAction: row[DATA_COLS.ACTION - 1] != null ? String(row[DATA_COLS.ACTION - 1]) : "",
    duree: row[DATA_COLS.DUREE - 1] != null && row[DATA_COLS.DUREE - 1] !== "" ? Number(row[DATA_COLS.DUREE - 1]) : 0,
    statut: row[DATA_COLS.STATUT - 1] != null ? String(row[DATA_COLS.STATUT - 1]) : ""
  };
}

/**
 * Charge le dernier enregistrement dont la colonne référence correspond (insensible aux espaces).
 * @param {string} reference
 * @return {Object|null} payload ou null si introuvable
 */
function getTicketByReference(reference) {
  const ref = (reference || "").toString().trim();
  if (!ref) return null;

  const sh = getDataSheet_();
  const last = sh.getLastRow();
  if (last < 1) return null;

  const values = sh.getRange(1, 1, last, DATA_COLS.STATUT).getValues();
  for (var i = values.length - 1; i >= 0; i--) {
    var cell = values[i][DATA_COLS.REF - 1];
    if (cell != null && String(cell).trim() === ref) {
      return rowToPayload_(values[i]);
    }
  }
  return null;
}

function saveTicket(payload) {
  const sh = getDataSheet_();
  const row = [
    payload.dateHeure || "",
    payload.technicien || "",
    payload.shift || "",
    (payload.reference || "").toString().trim(),
    payload.typeEquipement || "",
    payload.typeAction || "",
    Number(payload.duree || 0),
    payload.statut || ""
  ];
  sh.appendRow(row);
  return "OK";
}

/**
 * Met à jour la dernière ligne dont la référence correspond.
 * @param {Object} payload même structure que saveTicket
 * @return {string} "OK" ou erreur
 */
function updateTicket(payload) {
  const ref = (payload.reference || "").toString().trim();
  if (!ref) throw new Error("La référence est obligatoire pour la modification.");

  const sh = getDataSheet_();
  const last = sh.getLastRow();
  if (last < 1) throw new Error("Aucune donnée dans 'Data'.");

  const values = sh.getRange(1, 1, last, DATA_COLS.STATUT).getValues();
  var rowIndex = -1;
  for (var i = values.length - 1; i >= 0; i--) {
    var cell = values[i][DATA_COLS.REF - 1];
    if (cell != null && String(cell).trim() === ref) {
      rowIndex = i + 1;
      break;
    }
  }
  if (rowIndex < 0) throw new Error("Référence introuvable : " + ref);

  sh.getRange(rowIndex, 1, rowIndex, DATA_COLS.STATUT).setValues([[
    payload.dateHeure || "",
    payload.technicien || "",
    payload.shift || "",
    ref,
    payload.typeEquipement || "",
    payload.typeAction || "",
    Number(payload.duree || 0),
    payload.statut || ""
  ]]);
  return "OK";
}
