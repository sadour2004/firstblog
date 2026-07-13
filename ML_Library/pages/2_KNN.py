"""
Page KNN — K-Nearest Neighbors.
"""

import sys
from pathlib import Path

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
from utils.data_loader import load_iris_data, split_data, standardize
from utils.model_utils import train_knn, evaluate_classifier
from utils.plots import (
    plot_confusion_matrix,
    plot_iris_scatter,
)

page_config("KNN · ML Academy")
inject_custom_css()
sidebar_brand()

hero(
    title="K-Nearest Neighbors (KNN)",
    subtitle=(
        "Un algorithme de classification intuitif : un point est classé selon "
        "la majorité de ses K voisins les plus proches dans l'espace des features."
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
    section_header("Définition", "Qu'est-ce que KNN ?")
    st.markdown(
        """
        <div class="glass-card">
            <p style="color:#cbd5e1; line-height:1.7; margin:0;">
                <strong style="color:#f8fafc;">KNN</strong> (K-Nearest Neighbors) est un
                algorithme d'<em>apprentissage paresseux</em> (lazy learning) :
                il ne construit pas de modèle explicite pendant l'entraînement.
                Pour classer un nouveau point, il calcule sa distance à tous les
                points d'entraînement, sélectionne les <strong>K plus proches</strong>,
                puis attribue la classe majoritaire (vote).
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header("Principe des K voisins", "Logique étape par étape")
    st.markdown(
        """
        <div class="glass-card">
            <div class="step-item">
                <div class="step-num">1</div>
                <div><strong style="color:#f8fafc;">Choisir K</strong>
                <p style="margin:0.2rem 0 0; color:#94a3b8;">Nombre de voisins à consulter.</p></div>
            </div>
            <div class="step-item">
                <div class="step-num">2</div>
                <div><strong style="color:#f8fafc;">Calculer les distances</strong>
                <p style="margin:0.2rem 0 0; color:#94a3b8;">Mesurer la distance entre le point requête et chaque exemple d'entraînement.</p></div>
            </div>
            <div class="step-item">
                <div class="step-num">3</div>
                <div><strong style="color:#f8fafc;">Sélectionner les K plus proches</strong>
                <p style="margin:0.2rem 0 0; color:#94a3b8;">Trier par distance croissante.</p></div>
            </div>
            <div class="step-item" style="border-bottom:none;">
                <div class="step-num">4</div>
                <div><strong style="color:#f8fafc;">Voter</strong>
                <p style="margin:0.2rem 0 0; color:#94a3b8;">La classe majoritaire parmi les K voisins devient la prédiction.</p></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header("Formule — Distance euclidienne", "Mesure la plus courante")
    formula_box(
        "d(x, x′) = √( Σ<sub>i=1</sub><sup>n</sup> (x<sub>i</sub> − x′<sub>i</sub>)² )"
    )
    info_box(
        "D'autres distances existent (Manhattan, Minkowski). "
        "La standardisation des features est recommandée, car KNN est sensible à l'échelle.",
        kind="info",
    )

    section_header("Choix de K", "Un hyperparamètre critique")
    st.markdown(
        """
        - **K trop petit** (ex. K=1) → modèle sensible au bruit (overfitting).
        - **K trop grand** → frontières trop lisses, risque de sous-apprentissage.
        - En pratique, on teste plusieurs valeurs (souvent impaires pour éviter les égalités)
          et on valide (validation croisée).
        """
    )

    section_header("Exemple mathématique simple", "Classification en 2D")
    st.markdown(
        """
        Soit un point requête **P = (2, 3)** et K = 3.

        | Point | Coordonnées | Classe | Distance à P |
        |-------|-------------|--------|--------------|
        | A | (1, 2) | Rouge | √((2-1)²+(3-2)²) = √2 ≈ 1.41 |
        | B | (2, 5) | Bleu | √((2-2)²+(3-5)²) = 2 |
        | C | (4, 3) | Rouge | √((2-4)²+(3-3)²) = 2 |
        | D | (6, 7) | Bleu | √((2-6)²+(3-7)²) = √32 ≈ 5.66 |

        Les 3 plus proches sont A, B, C → **2 Rouges, 1 Bleu** → P est classé **Rouge**.
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
                    <li>Simple à comprendre et à implémenter</li>
                    <li>Pas d'hypothèse forte sur la distribution</li>
                    <li>Adaptatif aux frontières non linéaires</li>
                    <li>Fonctionne aussi en régression</li>
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
                    <li>Coût de prédiction élevé (calcul de toutes les distances)</li>
                    <li>Sensible à l'échelle des features</li>
                    <li>Maladapté aux très grandes dimensions (malédiction de la dimension)</li>
                    <li>Sensible aux outliers si K est petit</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ===========================================================================
# CODE
# ===========================================================================
with tab_code:
    section_header("Implémentation Scikit-Learn", "Pipeline complet sur Iris")
    st.code(
        '''from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Données
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 3. Standardisation (recommandée pour KNN)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Modèle
knn = KNeighborsClassifier(n_neighbors=5, metric="euclidean")
knn.fit(X_train, y_train)

# 5. Évaluation
y_pred = knn.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=iris.target_names))
''',
        language="python",
    )

# ===========================================================================
# DÉMO
# ===========================================================================
with tab_demo:
    section_header(
        "Démonstration interactive — Dataset Iris",
        "Ajustez K et observez l'impact sur les performances.",
    )

    X, y, feature_names, target_names, df = load_iris_data()

    with st.expander("Aperçu du dataset Iris", expanded=False):
        st.dataframe(df.head(10), width='stretch')
        fig_scatter = plot_iris_scatter(
            df,
            x="petal length (cm)",
            y="petal width (cm)",
            title="Iris — Longueur vs largeur des pétales",
        )
        st.plotly_chart(fig_scatter, width='stretch')

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        k = st.slider("Nombre de voisins (K)", min_value=1, max_value=25, value=5, step=1)
    with col_b:
        metric = st.selectbox("Distance", ["euclidean", "manhattan", "minkowski"])
    with col_c:
        test_size = st.slider("Taille du test (%)", 20, 40, 30, 5) / 100

    X_train, X_test, y_train, y_test = split_data(X, y, test_size=test_size)
    X_train_s, X_test_s, _ = standardize(X_train, X_test)

    model = train_knn(X_train_s, y_train, n_neighbors=k, metric=metric)
    metrics = evaluate_classifier(model, X_test_s, y_test, target_names)

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
            title=f"Matrice de confusion (K={k})",
        )
        st.plotly_chart(fig_cm, width='stretch')
    with c_right:
        st.markdown("##### Rapport de classification")
        st.dataframe(
            metrics["classification_report"].style.format("{:.3f}"),
            width='stretch',
        )

    info_box(
        f"Avec <strong>K={k}</strong> et la distance <strong>{metric}</strong>, "
        f"l'accuracy sur le jeu de test est de <strong>{metrics['accuracy']*100:.1f}%</strong>.",
        kind="success",
    )

footer()
