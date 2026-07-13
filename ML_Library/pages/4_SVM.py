"""
Page SVM — Support Vector Machine.
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
from utils.data_loader import load_iris_data, split_data, standardize, make_2d_classification
from utils.model_utils import train_svm, evaluate_classifier
from utils.plots import plot_confusion_matrix, plot_decision_boundary_2d


hero(
    title="Support Vector Machine (SVM)",
    subtitle=(
        "Trouver l'hyperplan qui sépare les classes avec la marge maximale, "
        "éventuellement dans un espace transformé grâce aux kernels."
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
    section_header("Définition", "Qu'est-ce qu'une SVM ?")
    st.markdown(
        """
        <div class="glass-card">
            <p style="color:#cbd5e1; line-height:1.7; margin:0;">
                Une <strong style="color:#f8fafc;">SVM</strong> (Support Vector Machine)
                cherche un <em>hyperplan séparateur</em> qui maximise la marge entre
                les classes. Les points les plus proches de cet hyperplan sont appelés
                <strong>vecteurs de support</strong> : ce sont eux qui définissent la solution.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header("Hyperplan & marge maximale", "Géométrie de la décision")
    formula_box("f(x) = w · x + b = 0 &nbsp;&nbsp;(équation de l'hyperplan)")
    formula_box("Marge = 2 / ‖w‖ &nbsp;&nbsp;→&nbsp;&nbsp; maximiser la marge ⇔ minimiser ‖w‖")
    info_box(
        "Plus la marge est grande, plus le modèle est robuste aux petites perturbations "
        "des données près de la frontière.",
        kind="info",
    )

    section_header("Vecteurs de support", "Les points qui comptent")
    st.markdown(
        """
        Seuls les points situés sur (ou dans) la marge influencent le modèle.
        Les autres points éloignés peuvent être retirés sans changer l'hyperplan :
        c'est une propriété de **parcimonie** des SVM.
        """
    )

    section_header("Kernels", "Passer au non-linéaire")
    st.markdown(
        """
        Si les classes ne sont pas linéairement séparables, on utilise un **kernel**
        pour projeter implicitement les données dans un espace de plus haute dimension
        (astuce du noyau / kernel trick).
        """
    )
    formula_box("Linéaire : K(x, x′) = x · x′")
    formula_box("Polynomial : K(x, x′) = (γ x · x′ + r)<sup>d</sup>")
    formula_box("RBF (gaussien) : K(x, x′) = exp(−γ ‖x − x′‖²)")

    c1, c2, c3 = st.columns(3)
    for col, (title, desc) in zip(
        [c1, c2, c3],
        [
            ("Linear", "Séparation linéaire rapide, interprétable."),
            ("RBF", "Très flexible, bon défaut en pratique."),
            ("Polynomial", "Interactions polynomiales de degré d."),
        ],
    ):
        with col:
            st.markdown(
                f"""
                <div class="glass-card">
                    <h4 style="color:#38bdf8; margin-top:0;">{title}</h4>
                    <p style="color:#94a3b8; margin:0;">{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    section_header("Paramètre C", "Trade-off marge / erreurs")
    st.markdown(
        """
        - **C grand** → moins d'erreurs tolérées (marge plus étroite, risque d'overfitting).
        - **C petit** → marge plus large, plus d'erreurs acceptées (régularisation plus forte).
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
                    <li>Efficace en haute dimension</li>
                    <li>Bonne généralisation grâce à la marge</li>
                    <li>Kernels pour problèmes non linéaires</li>
                    <li>Fonctionne bien avec peu de samples / beaucoup de features</li>
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
                    <li>Choix du kernel / hyperparamètres délicat</li>
                    <li>Peu scalable sur de très grands datasets</li>
                    <li>Moins interprétable qu'un arbre</li>
                    <li>Sensible à l'échelle → standardiser</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ===========================================================================
# CODE
# ===========================================================================
with tab_code:
    section_header("Implémentation Scikit-Learn", "SVC sur Iris", label="Code")
    with st.container(border=True):
        panel_header("📄 Script Python", "SVM avec kernel configurable")
        st.code(
        '''from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

svm = SVC(kernel="rbf", C=1.0, gamma="scale", random_state=42)
svm.fit(X_train, y_train)

y_pred = svm.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
''',
        language="python",
    )

# ===========================================================================
# DÉMO
# ===========================================================================
with tab_demo:
    section_header(
        "Démonstration interactive",
        "Choisissez le kernel et le paramètre C.",
        label="Live demo",
    )

    X, y, feature_names, target_names, df = load_iris_data()

    with st.container(border=True):
        panel_header("⚙️ Paramètres du modèle", "Kernel, régularisation C et degré polynomial")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            kernel = st.selectbox("Kernel", ["linear", "rbf", "poly"])
        with col_b:
            C = st.slider("Paramètre C", 0.01, 10.0, 1.0, 0.01)
        with col_c:
            degree = st.slider("Degré (poly)", 2, 5, 3, disabled=(kernel != "poly"))

    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.3)
    X_train_s, X_test_s, _ = standardize(X_train, X_test)

    model = train_svm(X_train_s, y_train, kernel=kernel, C=C, degree=degree)
    metrics = evaluate_classifier(model, X_test_s, y_test, target_names)

    section_header("Résultats Iris", "Métriques sur le jeu de test", label="Performance")
    render_score_metrics(metrics)

    c_left, c_right = st.columns(2, gap="medium")
    with c_left:
        with st.container(border=True):
            plot_header("Matrice de confusion", f"kernel={kernel} · C={C}")
            fig_cm = plot_confusion_matrix(
                metrics["confusion_matrix"],
                target_names,
                title=f"Matrice de confusion (kernel={kernel}, C={C})",
            )
            st.plotly_chart(fig_cm, width="stretch")
    with c_right:
        with st.container(border=True):
            plot_header("Rapport de classification", "Détail par classe")
            st.dataframe(
                metrics["classification_report"].style.format("{:.3f}"),
                width="stretch",
            )

    section_header(
        "Frontière de décision 2D",
        "Dataset synthétique pour illustrer l'effet du kernel.",
        label="Visualisation",
    )
    X2, y2 = make_2d_classification(n_samples=250)
    X2_train, X2_test, y2_train, y2_test = split_data(X2, y2, test_size=0.3)
    X2_train_s, X2_test_s, scaler2 = standardize(X2_train, X2_test)
    model_2d = train_svm(X2_train_s, y2_train, kernel=kernel, C=C, degree=degree)
    X2_all_s = scaler2.transform(X2)

    with st.container(border=True):
        plot_header("Frontière SVM", f"kernel={kernel} · C={C}")
        fig_bd = plot_decision_boundary_2d(
            model_2d,
            X2_all_s,
            y2,
            title=f"Frontière SVM — kernel={kernel}, C={C}",
            feature_names=("Feature 1 (scalée)", "Feature 2 (scalée)"),
        )
        st.pyplot(fig_bd, clear_figure=True)

    info_box(
        f"Sur Iris : kernel <strong>{kernel}</strong>, C=<strong>{C}</strong> → "
        f"accuracy = <strong style='color:#2dd4bf;'>{metrics['accuracy']*100:.1f}%</strong>.",
        kind="success",
    )

footer()
