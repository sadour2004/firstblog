"""
Page Comparaison — Tableau comparatif & performances sur Iris.
"""

import sys
from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from utils.style import (
    hero,
    section_header,
    info_box,
    footer,
    metric_card,
    panel_header,
    plot_header,
)
from utils.data_loader import load_iris_data, split_data, standardize
from utils.model_utils import (
    train_knn,
    train_decision_tree,
    train_svm,
    train_lda,
    compare_classifiers,
)
from utils.plots import plot_metrics_comparison, plot_confusion_matrix
from utils.model_utils import evaluate_classifier


hero(
    title="Comparaison des algorithmes",
    subtitle=(
        "Synthèse qualitative (type, avantages, limites, cas d'usage) "
        "et comparaison quantitative des performances sur le dataset Iris."
    ),
    badge="Synthèse académique",
)

# ---------------------------------------------------------------------------
# Tableau qualitatif
# ---------------------------------------------------------------------------
section_header(
    "Tableau comparatif",
    "Vue d'ensemble qualitative des cinq algorithmes.",
    label="Qualitatif",
)

comparison_table = pd.DataFrame(
    [
        {
            "Algorithme": "KNN",
            "Type": "Supervisé",
            "Tâche principale": "Classification",
            "Avantages": "Simple, non paramétrique, frontières flexibles",
            "Limites": "Lent en prédiction, sensible à l'échelle & à K",
            "Cas d'utilisation": "Petits datasets, baseline rapide, recommandation",
        },
        {
            "Algorithme": "Decision Tree",
            "Type": "Supervisé",
            "Tâche principale": "Classification",
            "Avantages": "Interprétable, peu de preprocessing, règles explicites",
            "Limites": "Surapprentissage, instabilité",
            "Cas d'utilisation": "Explicabilité, règles métier, features mixtes",
        },
        {
            "Algorithme": "SVM",
            "Type": "Supervisé",
            "Tâche principale": "Classification",
            "Avantages": "Bonne généralisation, kernels non linéaires",
            "Limites": "Choix kernel/C délicat, peu scalable",
            "Cas d'utilisation": "Haute dimension, texte, bio-informatique",
        },
        {
            "Algorithme": "PCA",
            "Type": "Non supervisé",
            "Tâche principale": "Réduction de dimension",
            "Avantages": "Compression, visualisation, débruitage",
            "Limites": "Ignore les labels, composantes peu interprétables",
            "Cas d'utilisation": "Prétraitement, visualisation, réduction de bruit",
        },
        {
            "Algorithme": "LDA",
            "Type": "Supervisé",
            "Tâche principale": "Réduction / Classification",
            "Avantages": "Exploite les labels, bonne séparation",
            "Limites": "Hypothèses gaussiennes, max C−1 axes",
            "Cas d'utilisation": "Classification linéaire, visualisation supervisée",
        },
    ]
)

with st.container(border=True):
    plot_header("Vue d'ensemble", "Type · avantages · limites · cas d'usage")
    st.dataframe(comparison_table, width="stretch", hide_index=True)

# ---------------------------------------------------------------------------
# Comparaison performances
# ---------------------------------------------------------------------------
section_header(
    "Performances sur Iris",
    "Même split train/test pour une comparaison équitable des classificateurs.",
    label="Quantitatif",
)

X, y, feature_names, target_names, df = load_iris_data()

with st.container(border=True):
    panel_header("⚙️ Paramètres d'évaluation", "Split et reproductibilité")
    col_a, col_b = st.columns(2)
    with col_a:
        test_size = st.slider("Taille du test (%)", 20, 40, 30, 5) / 100
    with col_b:
        random_state = st.number_input("Random state", 0, 999, 42)

X_train, X_test, y_train, y_test = split_data(
    X, y, test_size=test_size, random_state=int(random_state)
)
X_train_s, X_test_s, _ = standardize(X_train, X_test)

# Modèles (KNN/SVM sur données standardisées ; Tree/LDA sur brutes — cohérent)
models = {
    "KNN (K=5)": train_knn(X_train_s, y_train, n_neighbors=5),
    "Decision Tree": train_decision_tree(
        X_train, y_train, criterion="gini", max_depth=4
    ),
    "SVM (RBF)": train_svm(X_train_s, y_train, kernel="rbf", C=1.0),
    "LDA": train_lda(X_train, y_train),
}

# Évaluation : KNN & SVM → scaled ; Tree & LDA → raw
results_rows = []
cms = {}
for name, model in models.items():
    if name.startswith("KNN") or name.startswith("SVM"):
        metrics = evaluate_classifier(model, X_test_s, y_test, target_names)
    else:
        metrics = evaluate_classifier(model, X_test, y_test, target_names)
    results_rows.append(
        {
            "Algorithme": name,
            "Accuracy": metrics["accuracy"],
            "Precision": metrics["precision"],
            "Recall": metrics["recall"],
            "F1-Score": metrics["f1"],
        }
    )
    cms[name] = metrics["confusion_matrix"]

results_df = (
    pd.DataFrame(results_rows)
    .sort_values("Accuracy", ascending=False)
    .reset_index(drop=True)
)

best = results_df.iloc[0]
b1, b2, b3 = st.columns(3)
with b1:
    metric_card("Meilleur modèle", str(best["Algorithme"]), "🏆")
with b2:
    metric_card("Accuracy", f"{best['Accuracy']:.3f}", "🎯")
with b3:
    metric_card("F1-Score", f"{best['F1-Score']:.3f}", "⭐")

with st.container(border=True):
    plot_header("Tableau des performances", "Classé par accuracy décroissante")
    st.dataframe(
        results_df.style.format(
            {
                "Accuracy": "{:.3f}",
                "Precision": "{:.3f}",
                "Recall": "{:.3f}",
                "F1-Score": "{:.3f}",
            }
        ).background_gradient(subset=["Accuracy", "F1-Score"], cmap="Blues"),
        width="stretch",
        hide_index=True,
    )

with st.container(border=True):
    plot_header("Graphique comparatif", "Accuracy · Precision · Recall · F1")
    fig = plot_metrics_comparison(
        results_df, title="Comparaison des métriques sur Iris"
    )
    st.plotly_chart(fig, width="stretch")

section_header(
    "Matrices de confusion",
    "Détail des erreurs par algorithme.",
    label="Diagnostic",
)

cm_cols = st.columns(2, gap="medium")
for i, (name, cm) in enumerate(cms.items()):
    with cm_cols[i % 2]:
        with st.container(border=True):
            plot_header(name, "Prédictions vs vérité terrain")
            fig_cm = plot_confusion_matrix(cm, target_names, title=name)
            st.plotly_chart(fig_cm, width="stretch")

info_box(
    "<strong style='color:#f1f5f9;'>Note sur PCA :</strong> "
    "PCA n'est pas un classificateur. Elle sert à la réduction de dimension. "
    "On la compare qualitativement (voir tableau) plutôt qu'en accuracy.",
    kind="info",
)

section_header(
    "Conclusion générale",
    "Que retenir pour choisir un algorithme ?",
    label="Synthèse",
)

st.markdown(
    f"""
    <div class="glass-card">
        <p style="color:#a7b6c9; line-height:1.75; margin:0 0 1rem 0;">
            Sur le dataset <strong style="color:#f1f5f9;">Iris</strong> (petit, bien séparé),
            la plupart des classificateurs obtiennent d'excellents scores.
            Le meilleur modèle de cette session est
            <strong style="color:#67e8f9;">{best['Algorithme']}</strong>
            avec une accuracy de
            <strong style="color:#2dd4bf;">{best['Accuracy']*100:.1f}%</strong>.
        </p>
        <ul style="color:#a7b6c9; line-height:1.8;">
            <li><strong style="color:#f1f5f9;">KNN</strong> : excellent point de départ pédagogique.</li>
            <li><strong style="color:#f1f5f9;">Decision Tree</strong> : idéal quand l'interprétabilité prime.</li>
            <li><strong style="color:#f1f5f9;">SVM</strong> : puissant dès que les frontières se complexifient.</li>
            <li><strong style="color:#f1f5f9;">PCA</strong> : indispensable pour compresser / visualiser sans labels.</li>
            <li><strong style="color:#f1f5f9;">LDA</strong> : le choix naturel pour une réduction <em>supervisée</em>
                et une classification linéaire propre.</li>
        </ul>
        <p style="color:#a7b6c9; line-height:1.7; margin:1rem 0 0 0;">
            En pratique, le « meilleur » algorithme dépend du problème, de la taille des données,
            du besoin d'explicabilité et des contraintes de déploiement.
            Cette bibliothèque vous donne les outils pour <em>comprendre</em>,
            <em>expérimenter</em> et <em>comparer</em> — les trois piliers d'un projet ML réussi.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

footer()
