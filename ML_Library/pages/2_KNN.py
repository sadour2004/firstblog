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
    hero,
    section_header,
    info_box,
    formula_box,
    footer,
    render_score_metrics,
    panel_header,
    plot_header,
)
from utils.data_loader import load_iris_data, split_data, standardize
from utils.model_utils import train_knn, evaluate_classifier
from utils.plots import plot_confusion_matrix, plot_iris_scatter

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

with tab_theory:
    section_header("Définition", "Qu'est-ce que KNN ?", label="Concept")
    st.markdown(
        """
        <div class="glass-card">
          <p style="color:#a7b6c9; line-height:1.75; margin:0;">
            <strong style="color:#f1f5f9;">KNN</strong> (K-Nearest Neighbors) est un
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

    section_header("Principe des K voisins", "Logique étape par étape", label="Algorithme")
    st.markdown(
        """
        <div class="glass-card">
          <div class="step-item">
            <div class="step-num">1</div>
            <div><strong style="color:#f1f5f9;">Choisir K</strong>
            <p style="margin:0.2rem 0 0; color:#a7b6c9;">Nombre de voisins à consulter.</p></div>
          </div>
          <div class="step-item">
            <div class="step-num">2</div>
            <div><strong style="color:#f1f5f9;">Calculer les distances</strong>
            <p style="margin:0.2rem 0 0; color:#a7b6c9;">Distance entre le point requête et chaque exemple.</p></div>
          </div>
          <div class="step-item">
            <div class="step-num">3</div>
            <div><strong style="color:#f1f5f9;">Sélectionner les K plus proches</strong>
            <p style="margin:0.2rem 0 0; color:#a7b6c9;">Trier par distance croissante.</p></div>
          </div>
          <div class="step-item" style="border-bottom:none;">
            <div class="step-num">4</div>
            <div><strong style="color:#f1f5f9;">Voter</strong>
            <p style="margin:0.2rem 0 0; color:#a7b6c9;">La classe majoritaire devient la prédiction.</p></div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header("Distance euclidienne", "Mesure la plus courante", label="Formule")
    formula_box(
        "d(x, x′) = √( Σ<sub>i=1</sub><sup>n</sup> (x<sub>i</sub> − x′<sub>i</sub>)² )"
    )
    info_box(
        "D'autres distances existent (Manhattan, Minkowski). "
        "La <strong>standardisation</strong> des features est recommandée : KNN est sensible à l'échelle.",
        kind="info",
    )

    section_header("Choix de K", "Un hyperparamètre critique", label="Hyperparamètre")
    st.markdown(
        """
        <div class="glass-card">
          <ul style="color:#a7b6c9; line-height:1.8; margin:0; padding-left:1.2rem;">
            <li><strong style="color:#f1f5f9;">K trop petit</strong> (ex. K=1) → sensible au bruit (overfitting).</li>
            <li><strong style="color:#f1f5f9;">K trop grand</strong> → frontières trop lisses (sous-apprentissage).</li>
            <li>En pratique : tester plusieurs valeurs (souvent impaires) via validation croisée.</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header("Exemple mathématique", "Classification en 2D", label="Illustration")
    st.markdown(
        """
        <div class="glass-card">
          <p style="color:#a7b6c9; margin:0 0 0.8rem 0;">Point requête <strong style="color:#f1f5f9;">P = (2, 3)</strong>, K = 3.</p>
          <p style="color:#a7b6c9; margin:0; line-height:1.7;">
            A(1,2) Rouge ≈ 1.41 · B(2,5) Bleu = 2 · C(4,3) Rouge = 2 · D(6,7) Bleu ≈ 5.66<br/>
            Les 3 plus proches : A, B, C → <strong style="color:#2dd4bf;">2 Rouges, 1 Bleu → P classé Rouge</strong>.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header("Avantages & limites", "", label="Bilan")
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown(
            """
            <div class="glass-card">
              <h3 style="color:#5eead4; margin-top:0;">✅ Avantages</h3>
              <ul style="color:#a7b6c9; line-height:1.75;">
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
              <h3 style="color:#fb7185; margin-top:0;">⚠️ Limites</h3>
              <ul style="color:#a7b6c9; line-height:1.75;">
                <li>Coût de prédiction élevé</li>
                <li>Sensible à l'échelle des features</li>
                <li>Maladapté aux très grandes dimensions</li>
                <li>Sensible aux outliers si K est petit</li>
              </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

with tab_code:
    section_header("Implémentation Scikit-Learn", "Pipeline complet sur Iris", label="Code")
    with st.container(border=True):
        panel_header("📄 Script Python", "KNeighborsClassifier + standardisation")
        st.code(
            '''from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5, metric="euclidean")
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=iris.target_names))
''',
            language="python",
        )

with tab_demo:
    section_header(
        "Démonstration interactive",
        "Ajustez K et observez l'impact sur les performances Iris.",
        label="Live demo",
    )

    X, y, feature_names, target_names, df = load_iris_data()

    with st.expander("Aperçu du dataset Iris", expanded=False):
        st.dataframe(df.head(10), width="stretch")
        fig_scatter = plot_iris_scatter(
            df,
            x="petal length (cm)",
            y="petal width (cm)",
            title="Iris — Longueur vs largeur des pétales",
        )
        st.plotly_chart(fig_scatter, width="stretch")

    with st.container(border=True):
        panel_header("⚙️ Paramètres du modèle", "Hyperparamètres KNN + split train/test")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            k = st.slider("Nombre de voisins (K)", 1, 25, 5, 1)
        with col_b:
            metric = st.selectbox("Distance", ["euclidean", "manhattan", "minkowski"])
        with col_c:
            test_size = st.slider("Taille du test (%)", 20, 40, 30, 5) / 100

    X_train, X_test, y_train, y_test = split_data(X, y, test_size=test_size)
    X_train_s, X_test_s, _ = standardize(X_train, X_test)
    model = train_knn(X_train_s, y_train, n_neighbors=k, metric=metric)
    metrics = evaluate_classifier(model, X_test_s, y_test, target_names)

    section_header("Résultats", "Métriques sur le jeu de test", label="Performance")
    render_score_metrics(metrics)

    c_left, c_right = st.columns(2, gap="medium")
    with c_left:
        with st.container(border=True):
            plot_header("Matrice de confusion", f"K={k} · {metric}")
            fig_cm = plot_confusion_matrix(
                metrics["confusion_matrix"],
                target_names,
                title=f"Matrice de confusion (K={k})",
            )
            st.plotly_chart(fig_cm, width="stretch")
    with c_right:
        with st.container(border=True):
            plot_header("Rapport de classification", "Precision / Recall / F1 par classe")
            st.dataframe(
                metrics["classification_report"].style.format("{:.3f}"),
                width="stretch",
            )

    info_box(
        f"Avec <strong>K={k}</strong> et la distance <strong>{metric}</strong>, "
        f"l'accuracy sur le jeu de test est de "
        f"<strong style='color:#2dd4bf;'>{metrics['accuracy']*100:.1f}%</strong>.",
        kind="success",
    )

footer()
