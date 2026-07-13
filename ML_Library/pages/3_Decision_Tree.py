"""
Page Decision Tree — Arbre de décision.
"""

import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from utils.style import (
    hero,
    section_header,
    info_box,
    formula_box,
    footer,
    render_score_metrics,
    panel_header,
    plot_header,
    metric_card,
)
from utils.data_loader import load_iris_data, split_data
from utils.model_utils import train_decision_tree, evaluate_classifier
from utils.plots import (
    plot_confusion_matrix,
    plot_feature_importance_tree,
    plot_tree_matplotlib,
)


hero(
    title="Decision Tree",
    subtitle=(
        "Un modèle interprétable qui partitionne l'espace des features par des "
        "questions successives, jusqu'à atteindre des feuilles de décision."
    ),
    badge="Supervisé · Classification",
)

tab_theory, tab_code, tab_demo = st.tabs(
    ["📖 Théorie", "💻 Code Python", "🧪 Démonstration interactive"]
)

# ===========================================================================
# THÉORIE
# ===========================================================================
with tab_theory:
    section_header("Définition", "Qu'est-ce qu'un arbre de décision ?")
    st.markdown(
        """
        <div class="glass-card">
            <p style="color:#cbd5e1; line-height:1.7; margin:0;">
                Un <strong style="color:#f8fafc;">arbre de décision</strong> est un modèle
                qui représente une séquence de tests sur les variables. Chaque test
                divise les données en sous-groupes de plus en plus homogènes
                (au sens d'une impureté : Gini ou Entropie).
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header("Vocabulaire", "Racine, nœud, branche, feuille")
    c1, c2, c3, c4 = st.columns(4)
    cards = [
        ("🌱", "Racine", "Nœud de départ de l'arbre (premier split)."),
        ("🔷", "Nœud", "Test sur une feature (ex. pétale ≤ 2.45)."),
        ("➡️", "Branche", "Issue du test (vrai / faux)."),
        ("🍃", "Feuille", "Décision finale : la classe prédite."),
    ]
    for col, (icon, title, desc) in zip([c1, c2, c3, c4], cards):
        with col:
            st.markdown(
                f"""
                <div class="glass-card" style="text-align:center;">
                    <div style="font-size:1.6rem;">{icon}</div>
                    <h4 style="color:#f8fafc; margin:0.4rem 0;">{title}</h4>
                    <p style="color:#94a3b8; margin:0; font-size:0.9rem;">{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    section_header("Critères d'impureté", "Gini, Entropie et Gain d'information")

    st.markdown("##### Indice de Gini")
    formula_box("Gini(S) = 1 − Σ<sub>k</sub> p<sub>k</sub>²")
    st.markdown(
        "Plus Gini est proche de 0, plus le nœud est pur (une seule classe)."
    )

    st.markdown("##### Entropie")
    formula_box("H(S) = − Σ<sub>k</sub> p<sub>k</sub> log₂(p<sub>k</sub>)")
    st.markdown(
        "L'entropie mesure le désordre. Elle vaut 0 pour un nœud parfaitement pur."
    )

    st.markdown("##### Gain d'information")
    formula_box(
        "Gain(S, A) = H(S) − Σ<sub>v</sub> (|S<sub>v</sub>| / |S|) · H(S<sub>v</sub>)"
    )
    info_box(
        "À chaque split, l'algorithme choisit la feature et le seuil qui "
        "<strong>maximisent</strong> la réduction d'impureté (ou le gain d'information).",
        kind="info",
    )

    section_header("Exemple simple de décision", "Fleur Iris")
    st.markdown(
        """
        ```
        petal length ≤ 2.45 ?
        ├── Oui → setosa
        └── Non → petal width ≤ 1.75 ?
                  ├── Oui → versicolor
                  └── Non → virginica
        ```
        Cet arbre (simplifié) illustre comment des seuils successifs mènent à une classe.
        """
    )

    section_header("Avantages & limites", "")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color:#34d399; margin-top:0;">✅ Avantages</h3>
                <ul style="color:#94a3b8; line-height:1.7;">
                    <li>Très interprétable (règles lisibles)</li>
                    <li>Gère variables numériques et catégorielles</li>
                    <li>Peu de prétraitement requis</li>
                    <li>Capture des interactions non linéaires</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color:#f87171; margin-top:0;">⚠️ Limites</h3>
                <ul style="color:#94a3b8; line-height:1.7;">
                    <li>Tendance au surapprentissage (arbres trop profonds)</li>
                    <li>Instable : petites variations → arbres différents</li>
                    <li>Frontières orthogonales aux axes</li>
                    <li>Souvent battu par Random Forest / Boosting</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ===========================================================================
# CODE
# ===========================================================================
with tab_code:
    section_header("Implémentation Scikit-Learn", "DecisionTreeClassifier sur Iris", label="Code")
    with st.container(border=True):
        panel_header("📄 Script Python", "Arbre de décision sur Iris")
        st.code(
        '''from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

clf = DecisionTreeClassifier(
    criterion="gini",   # ou "entropy"
    max_depth=3,
    random_state=42,
)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Visualisation de l'arbre
plt.figure(figsize=(12, 6))
plot_tree(clf, feature_names=iris.feature_names,
          class_names=iris.target_names, filled=True)
plt.show()
''',
        language="python",
    )

# ===========================================================================
# DÉMO
# ===========================================================================
with tab_demo:
    section_header(
        "Démonstration interactive",
        "Choisissez le critère et la profondeur maximale.",
        label="Live demo",
    )

    X, y, feature_names, target_names, df = load_iris_data()

    with st.container(border=True):
        panel_header("⚙️ Paramètres du modèle", "Critère d'impureté, profondeur et split")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            criterion = st.selectbox("Critère", ["gini", "entropy"])
        with col_b:
            max_depth = st.slider("max_depth", 1, 10, 3)
        with col_c:
            test_size = st.slider("Taille du test (%)", 20, 40, 30, 5) / 100

    X_train, X_test, y_train, y_test = split_data(X, y, test_size=test_size)
    model = train_decision_tree(
        X_train, y_train, criterion=criterion, max_depth=max_depth
    )
    metrics = evaluate_classifier(model, X_test, y_test, target_names)

    section_header("Résultats", "Métriques sur le jeu de test", label="Performance")
    render_score_metrics(metrics)

    c_left, c_right = st.columns(2, gap="medium")
    with c_left:
        with st.container(border=True):
            plot_header("Matrice de confusion", f"{criterion} · depth={max_depth}")
            fig_cm = plot_confusion_matrix(
                metrics["confusion_matrix"],
                target_names,
                title=f"Matrice de confusion ({criterion}, depth={max_depth})",
            )
            st.plotly_chart(fig_cm, width="stretch")
    with c_right:
        with st.container(border=True):
            plot_header("Importance des features", "Contribution relative de chaque variable")
            fig_imp = plot_feature_importance_tree(
                model, feature_names, title="Importance des features"
            )
            st.plotly_chart(fig_imp, width="stretch")

    with st.container(border=True):
        plot_header("Rapport de classification", "Détail par classe")
        st.dataframe(
            metrics["classification_report"].style.format("{:.3f}"),
            width="stretch",
        )

    with st.container(border=True):
        plot_header("Visualisation de l'arbre", "Structure des décisions")
        fig_tree = plot_tree_matplotlib(model, feature_names, target_names)
        st.pyplot(fig_tree, clear_figure=True)

    info_box(
        f"Critère <strong>{criterion}</strong>, profondeur max = <strong>{max_depth}</strong> → "
        f"accuracy = <strong style='color:#2dd4bf;'>{metrics['accuracy']*100:.1f}%</strong>.",
        kind="success",
    )

footer()
