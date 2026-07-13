"""
Page LDA — Linear Discriminant Analysis.
"""

import sys
from pathlib import Path

import numpy as np
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
    formula_box,
    footer,
)
from utils.data_loader import load_iris_data, split_data
from utils.model_utils import train_lda, train_pca, evaluate_classifier
from utils.plots import (
    plot_confusion_matrix,
    plot_lda_2d,
    plot_pca_2d,
)


hero(
    title="LDA — Analyse Discriminante Linéaire",
    subtitle=(
        "Réduction de dimension supervisée et classificateur : "
        "LDA utilise les labels pour maximiser la séparabilité des classes."
    ),
    badge="Supervisé · Réduction / Classification",
)

tab_theory, tab_code, tab_demo = st.tabs(
    ["📖 Théorie", "💻 Code Python", "🧪 Démonstration interactive"]
)

# ===========================================================================
# THÉORIE
# ===========================================================================
with tab_theory:
    section_header("Définition", "Qu'est-ce que LDA ?")
    st.markdown(
        """
        <div class="glass-card">
            <p style="color:#cbd5e1; line-height:1.7; margin:0;">
                La <strong style="color:#f8fafc;">LDA</strong> (Linear Discriminant Analysis)
                est une méthode <em>supervisée</em> qui cherche des projections linéaires
                maximisant le rapport entre la <strong>variance inter-classes</strong>
                et la <strong>variance intra-classe</strong>. Elle sert à la fois
                à la réduction de dimension et à la classification.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header("PCA vs LDA", "La différence essentielle")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="glass-card">
                <h4 style="color:#38bdf8; margin-top:0;">📉 PCA</h4>
                <ul style="color:#94a3b8; line-height:1.7;">
                    <li>Non supervisée</li>
                    <li><strong>Ignore</strong> les classes</li>
                    <li>Maximise la variance totale</li>
                    <li>Bon pour compression / visualisation</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="glass-card">
                <h4 style="color:#34d399; margin-top:0;">🎯 LDA</h4>
                <ul style="color:#94a3b8; line-height:1.7;">
                    <li>Supervisée</li>
                    <li><strong>Utilise</strong> les classes</li>
                    <li>Maximise la séparabilité</li>
                    <li>Bon pour classification / visualisation séparée</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    info_box(
        "PCA ne regarde pas les classes. LDA, au contraire, oriente la projection "
        "pour que les groupes étiquetés soient le plus distincts possible.",
        kind="warning",
    )

    section_header("Principe mathématique", "Critère de Fisher")
    formula_box(
        "J(w) = (wᵀ S<sub>B</sub> w) / (wᵀ S<sub>W</sub> w)"
    )
    st.markdown(
        """
        - **S_B** : matrice de dispersion *between-class* (inter-classes)
        - **S_W** : matrice de dispersion *within-class* (intra-classe)
        - On cherche w qui maximise J(w)

        Pour C classes, LDA produit au plus **C − 1** composantes discriminantes.
        Sur Iris (3 classes) → maximum **2** axes LDA.
        """
    )

    section_header("Deux usages de LDA", "")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="glass-card">
                <h4 style="color:#f8fafc; margin-top:0;">1️⃣ Classification</h4>
                <p style="color:#94a3b8; margin:0;">
                    LDA estime des densités gaussiennes par classe et assigne
                    le label de la densité la plus probable (règle de Bayes).
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="glass-card">
                <h4 style="color:#f8fafc; margin-top:0;">2️⃣ Réduction supervisée</h4>
                <p style="color:#94a3b8; margin:0;">
                    On projette X → espace LDA (1D ou 2D pour Iris),
                    puis on visualise ou on enchaîne avec un autre classificateur.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    section_header("Avantages & limites", "")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color:#34d399; margin-top:0;">✅ Avantages</h3>
                <ul style="color:#94a3b8; line-height:1.7;">
                    <li>Exploite les labels → meilleure séparation</li>
                    <li>Interprétable et rapide</li>
                    <li>Fonctionne bien si classes gaussiennes</li>
                    <li>Utile en visualisation supervisée</li>
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
                    <li>Hypothèse de matrices de covariance partagées</li>
                    <li>Limité à C−1 composantes</li>
                    <li>Moins robuste si classes très non linéaires</li>
                    <li>Sensible aux outliers</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ===========================================================================
# CODE
# ===========================================================================
with tab_code:
    section_header("Implémentation Scikit-Learn", "LDA classificateur + projection")
    st.code(
        '''from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# LDA comme classificateur
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)
y_pred = lda.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# LDA pour réduction de dimension (max 2 pour 3 classes)
lda_2d = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda_2d.fit_transform(X, y)
''',
        language="python",
    )

# ===========================================================================
# DÉMO
# ===========================================================================
with tab_demo:
    section_header(
        "Démonstration interactive — Dataset Iris",
        "Classification LDA + visualisation de la projection supervisée.",
    )

    X, y, feature_names, target_names, df = load_iris_data()

    test_size = st.slider("Taille du test (%)", 20, 40, 30, 5) / 100
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=test_size)

    # --- Classification ---
    lda_clf = train_lda(X_train, y_train, n_components=None)
    metrics = evaluate_classifier(lda_clf, X_test, y_test, target_names)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Accuracy", f"{metrics['accuracy']:.3f}")
    m2.metric("Precision", f"{metrics['precision']:.3f}")
    m3.metric("Recall", f"{metrics['recall']:.3f}")
    m4.metric("F1-Score", f"{metrics['f1']:.3f}")

    c_left, c_right = st.columns(2)
    with c_left:
        fig_cm = plot_confusion_matrix(
            metrics["confusion_matrix"],
            target_names,
            title="Matrice de confusion — LDA classificateur",
        )
        st.plotly_chart(fig_cm, width='stretch')
    with c_right:
        st.markdown("##### Rapport de classification")
        st.dataframe(
            metrics["classification_report"].style.format("{:.3f}"),
            width='stretch',
        )

    st.markdown("---")
    section_header(
        "Projection LDA vs PCA",
        "Même données, deux philosophies de réduction.",
    )

    # Projection LDA (fit sur tout le set pour la viz pédagogique)
    lda_proj = train_lda(X, y, n_components=2)
    X_lda = lda_proj.transform(X)

    # Projection PCA pour comparaison
    X_scaled = StandardScaler().fit_transform(X)
    pca, X_pca = train_pca(X_scaled, n_components=2)

    col_a, col_b = st.columns(2)
    with col_a:
        fig_lda = plot_lda_2d(
            X_lda, y, target_names, title="Projection LDA (supervisée)"
        )
        st.plotly_chart(fig_lda, width='stretch')
    with col_b:
        fig_pca = plot_pca_2d(
            X_pca,
            y,
            target_names,
            explained_variance=pca.explained_variance_ratio_,
            title="Projection PCA (non supervisée)",
        )
        st.plotly_chart(fig_pca, width='stretch')

    info_box(
        f"LDA classificateur → accuracy = <strong>{metrics['accuracy']*100:.1f}%</strong>. "
        "Observez comment LDA sépare souvent mieux les classes que PCA en 2D.",
        kind="success",
    )

footer()
