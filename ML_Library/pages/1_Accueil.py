"""
Page Accueil — Introduction au Machine Learning.
"""

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from utils.style import (
    hero,
    section_header,
    info_box,
    glass_card_html,
    footer,
)


hero(
    title="Introduction au Machine Learning",
    subtitle=(
        "Comprendre les fondements : apprentissage supervisé et non supervisé, "
        "étapes d'un projet ML, et panorama des algorithmes de cette bibliothèque."
    ),
    badge="Fondamentaux · ML Academy",
)

section_header(
    "Qu'est-ce que le Machine Learning ?",
    "Une branche de l'intelligence artificielle qui apprend à partir des données.",
    label="Définition",
)

st.markdown(
    """
    <div class="glass-card">
        <p style="color:#a8b6c8; line-height:1.75; margin:0;">
            Le <strong style="color:#f1f5f9;">Machine Learning</strong> (apprentissage automatique)
            désigne l'ensemble des méthodes qui permettent à un système d'améliorer ses
            performances sur une tâche en s'appuyant sur des données, sans être
            explicitement programmé pour chaque cas.
        </p>
        <br/>
        <p style="color:#6b7c91; line-height:1.75; margin:0;">
            Au lieu d'écrire des règles manuelles, on <em>entraîne</em> un modèle sur des
            exemples. Le modèle généralise ensuite à de nouvelles observations.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

section_header(
    "Deux grandes familles d'apprentissage",
    "La présence (ou non) d'étiquettes guide le choix de l'algorithme.",
    label="Familles",
)

col1, col2 = st.columns(2, gap="medium")
with col1:
    st.markdown(
        glass_card_html(
            "Apprentissage supervisé",
            "Les données d'entraînement sont <strong>étiquetées</strong> (X, y). "
            "L'objectif est d'apprendre une fonction f : X → y. "
            "Exemples : classification (KNN, Decision Tree, SVM, LDA) et régression.",
            "✅",
        ),
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        glass_card_html(
            "Apprentissage non supervisé",
            "Les données n'ont <strong>pas de labels</strong>. "
            "L'algorithme cherche une structure : clusters, réduction de dimension, "
            "associations. Exemple étudié ici : <strong>PCA</strong>.",
            "🔍",
        ),
        unsafe_allow_html=True,
    )

info_box(
    "<strong style='color:#f1f5f9;'>À retenir :</strong> "
    "PCA est non supervisé (il ignore les classes). "
    "LDA est supervisé (il utilise les labels pour maximiser la séparation).",
    kind="info",
)

section_header(
    "Étapes d'un projet Machine Learning",
    "Un pipeline classique, de la donnée à l'évaluation.",
    label="Pipeline",
)

steps = [
    ("1", "Compréhension du problème", "Définir l'objectif et le type de tâche (classification, régression…)."),
    ("2", "Collecte & exploration", "Charger les données, analyser distributions, valeurs manquantes, corrélations."),
    ("3", "Préparation", "Nettoyage, encodage, standardisation, split train/test."),
    ("4", "Modélisation", "Choisir un algorithme, entraîner, ajuster les hyperparamètres."),
    ("5", "Évaluation", "Accuracy, precision, recall, F1, matrice de confusion, validation croisée."),
    ("6", "Déploiement & suivi", "Mettre le modèle en production et monitorer sa performance."),
]

steps_html = '<div class="glass-card">'
for num, title, desc in steps:
    border = ' style="border-bottom:none;"' if num == "6" else ""
    steps_html += f"""
    <div class="step-item"{border}>
        <div class="step-num">{num}</div>
        <div>
            <strong style="color:#f1f5f9;">{title}</strong>
            <p style="margin:0.25rem 0 0 0; color:#a8b6c8;">{desc}</p>
        </div>
    </div>
    """
steps_html += "</div>"
st.markdown(steps_html, unsafe_allow_html=True)

section_header(
    "Tableau récapitulatif des algorithmes",
    "Vue d'ensemble des cinq algorithmes de cette bibliothèque.",
    label="Synthèse",
)

recap = pd.DataFrame(
    [
        {
            "Algorithme": "KNN",
            "Type": "Supervisé",
            "Tâche": "Classification / Régression",
            "Idée clé": "Vote des K voisins les plus proches",
            "Paramètre clé": "K (n_neighbors)",
        },
        {
            "Algorithme": "Decision Tree",
            "Type": "Supervisé",
            "Tâche": "Classification / Régression",
            "Idée clé": "Partitions selon Gini / Entropie",
            "Paramètre clé": "criterion, max_depth",
        },
        {
            "Algorithme": "SVM",
            "Type": "Supervisé",
            "Tâche": "Classification / Régression",
            "Idée clé": "Hyperplan à marge maximale",
            "Paramètre clé": "kernel, C",
        },
        {
            "Algorithme": "PCA",
            "Type": "Non supervisé",
            "Tâche": "Réduction de dimension",
            "Idée clé": "Maximiser la variance",
            "Paramètre clé": "n_components",
        },
        {
            "Algorithme": "LDA",
            "Type": "Supervisé",
            "Tâche": "Réduction / Classification",
            "Idée clé": "Maximiser la séparabilité des classes",
            "Paramètre clé": "n_components",
        },
    ]
)

st.dataframe(recap, width="stretch", hide_index=True)

info_box(
    "Dans ce projet, toutes les démonstrations de classification utilisent le "
    "<strong>dataset Iris</strong> (150 fleurs, 4 features, 3 espèces).",
    kind="success",
)

footer()
