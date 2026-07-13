"""
Page PCA — Analyse en Composantes Principales.
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from utils.style import (
    inject_custom_css,
    hero,
    section_header,
    info_box,
    formula_box,
    footer,
    page_config,
    sidebar_brand,
)
from utils.data_loader import load_iris_data
from utils.model_utils import train_pca
from utils.plots import plot_pca_2d, plot_explained_variance, plot_iris_scatter
from sklearn.preprocessing import StandardScaler

page_config("PCA · ML Academy")
inject_custom_css()
sidebar_brand()

hero(
    title="PCA — Analyse en Composantes Principales",
    subtitle=(
        "Réduire la dimensionnalité en projetant les données sur les directions "
        "qui capturent le maximum de variance — sans utiliser les labels."
    ),
    badge="Non supervisé · Réduction de dimension",
)

tab_theory, tab_code, tab_demo = st.tabs(
    ["📖 Théorie", "💻 Code Python", "🧪 Démonstration interactive"]
)

# ===========================================================================
# THÉORIE
# ===========================================================================
with tab_theory:
    section_header("Définition", "Qu'est-ce que PCA ?")
    st.markdown(
        """
        <div class="glass-card">
            <p style="color:#cbd5e1; line-height:1.7; margin:0;">
                La <strong style="color:#f8fafc;">PCA</strong> (Principal Component Analysis)
                est une technique <em>non supervisée</em> de réduction de dimension.
                Elle transforme un ensemble de variables corrélées en un nouvel ensemble
                de variables non corrélées appelées
                <strong>composantes principales</strong>, ordonnées par variance décroissante.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header("Réduction de dimension", "Pourquoi réduire ?")
    st.markdown(
        """
        - Visualiser des données en 2D / 3D
        - Accélérer les algorithmes en aval
        - Atténuer le bruit et la redondance
        - Combattre la malédiction de la dimension
        """
    )

    section_header("Variance & composantes principales", "Idée mathématique")
    formula_box(
        "On cherche u₁ qui maximise Var(X u₁) sous ‖u₁‖ = 1"
    )
    formula_box(
        "Les composantes sont les vecteurs propres de la matrice de covariance Σ = (1/n) XᵀX"
    )
    st.markdown(
        """
        - **PC1** : direction de variance maximale
        - **PC2** : direction de variance maximale, orthogonale à PC1
        - etc.
        """
    )

    section_header(
        "Données originales vs données projetées",
        "Ce que l'on conserve, ce que l'on perd",
    )
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="glass-card">
                <h4 style="color:#38bdf8; margin-top:0;">Espace original</h4>
                <p style="color:#94a3b8; margin:0;">
                    Iris : 4 dimensions (sépal/pétal longueur & largeur).
                    Information complète, mais difficile à visualiser.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="glass-card">
                <h4 style="color:#22d3ee; margin-top:0;">Espace projeté (2D)</h4>
                <p style="color:#94a3b8; margin:0;">
                    On conserve les 2 premières composantes.
                    Une partie de la variance est perdue, mais la structure
                    globale (souvent les clusters) reste visible.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    info_box(
        "<strong style='color:#f8fafc;'>Important :</strong> PCA <em>ne regarde pas</em> "
        "les classes. Elle peut donc mélanger des groupes si la variance dominante "
        "n'est pas alignée avec la séparation des labels. C'est la différence clé avec LDA.",
        kind="warning",
    )

    section_header("Avantages & limites", "")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color:#34d399; margin-top:0;">✅ Avantages</h3>
                <ul style="color:#94a3b8; line-height:1.7;">
                    <li>Réduit la dimension efficacement</li>
                    <li>Dénuise et décorrèle les features</li>
                    <li>Excellent pour la visualisation</li>
                    <li>Sans labels nécessaires</li>
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
                    <li>Composantes parfois difficiles à interpréter</li>
                    <li>Suppose des relations linéaires</li>
                    <li>Sensible à l'échelle → standardiser</li>
                    <li>Ignore les labels (peut mal séparer les classes)</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ===========================================================================
# CODE
# ===========================================================================
with tab_code:
    section_header("Implémentation Scikit-Learn", "PCA 2D sur Iris")
    st.code(
        '''from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

iris = load_iris()
X, y = iris.data, iris.target

# Standardisation obligatoire avant PCA
X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Variance cumulée:", pca.explained_variance_ratio_.sum())

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap="viridis")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Iris projeté par PCA")
plt.show()
''',
        language="python",
    )

# ===========================================================================
# DÉMO
# ===========================================================================
with tab_demo:
    section_header(
        "Démonstration interactive — Dataset Iris",
        "Standardisation → PCA → visualisation 2D & variance expliquée.",
    )

    X, y, feature_names, target_names, df = load_iris_data()

    n_components = st.slider("Nombre de composantes", 2, 4, 2)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca, X_pca = train_pca(X_scaled, n_components=n_components)
    ratios = pca.explained_variance_ratio_

    m1, m2, m3 = st.columns(3)
    m1.metric("PC1 — variance", f"{ratios[0]*100:.1f}%")
    m2.metric("PC2 — variance", f"{ratios[1]*100:.1f}%")
    m3.metric("Variance cumulée", f"{ratios.sum()*100:.1f}%")

    c_left, c_right = st.columns(2)
    with c_left:
        fig_pca = plot_pca_2d(
            X_pca[:, :2],
            y,
            target_names,
            explained_variance=ratios,
            title="Projection PCA (2D)",
        )
        st.plotly_chart(fig_pca, width='stretch')
    with c_right:
        fig_var = plot_explained_variance(
            ratios, title="Variance expliquée par composante"
        )
        st.plotly_chart(fig_var, width='stretch')

    st.markdown("##### Comparaison : espace original (2 features) vs PCA")
    fig_orig = plot_iris_scatter(
        df,
        x="petal length (cm)",
        y="petal width (cm)",
        title="Espace original — 2 features choisies",
    )
    st.plotly_chart(fig_orig, width='stretch')

    # Tableau des ratios
    var_df = pd.DataFrame(
        {
            "Composante": [f"PC{i+1}" for i in range(len(ratios))],
            "Variance expliquée": ratios,
            "Variance cumulée": np.cumsum(ratios),
        }
    )
    st.dataframe(
        var_df.style.format(
            {"Variance expliquée": "{:.4f}", "Variance cumulée": "{:.4f}"}
        ),
        width='stretch',
        hide_index=True,
    )

    info_box(
        f"Avec <strong>{n_components}</strong> composantes, PCA conserve "
        f"<strong>{ratios.sum()*100:.1f}%</strong> de la variance totale d'Iris.",
        kind="success",
    )

footer()
