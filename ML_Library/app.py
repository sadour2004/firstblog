"""
ML Academy Library — Point d'entrée principal.
Lancez avec : streamlit run app.py  (depuis le dossier ML_Library)
"""

import streamlit as st

from utils.style import (
    inject_custom_css,
    hero,
    section_header,
    algo_card_html,
    glass_card_html,
    footer,
    page_config,
    sidebar_brand,
)


def render_home():
    """Page d'accueil premium."""
    hero(
        title="ML Academy Library",
        subtitle=(
            "Une bibliothèque interactive et pédagogique de Machine Learning. "
            "Explorez KNN, Decision Tree, SVM, PCA et LDA avec des explications claires, "
            "des formules essentielles et des démonstrations Scikit-Learn en temps réel."
        ),
        badge="Bibliothèque académique interactive",
    )

    section_header(
        "🎯 Objectifs du projet",
        "Comprendre, visualiser et comparer les algorithmes étudiés ce semestre.",
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            glass_card_html(
                "Apprendre",
                "Des explications pédagogiques, des formules clés et des exemples "
                "mathématiques simples pour chaque algorithme.",
                "📖",
            ),
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            glass_card_html(
                "Expérimenter",
                "Des sliders, des paramètres interactifs et des entraînements "
                "en direct sur le dataset Iris avec Scikit-Learn.",
                "🧪",
            ),
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            glass_card_html(
                "Comparer",
                "Des métriques, des matrices de confusion et des graphiques Plotly "
                "pour évaluer et comparer les performances.",
                "📊",
            ),
            unsafe_allow_html=True,
        )

    section_header(
        "🧠 Algorithmes étudiés",
        "Cinq piliers du Machine Learning — classification et réduction de dimension.",
    )

    algos = [
        ("📍", "KNN", "Classification basée sur la proximité des K plus proches voisins.", "Supervisé · Classification"),
        ("🌳", "Decision Tree", "Partitions successives selon Gini ou entropie.", "Supervisé · Classification"),
        ("📐", "SVM", "Hyperplan à marge maximale avec kernels.", "Supervisé · Classification"),
        ("📉", "PCA", "Réduction non supervisée par variance.", "Non supervisé · Réduction"),
        ("🎯", "LDA", "Réduction supervisée et classification linéaire.", "Supervisé · Réduction / Classification"),
    ]

    row1 = st.columns(3)
    for col, algo in zip(row1, algos[:3]):
        with col:
            st.markdown(algo_card_html(*algo), unsafe_allow_html=True)

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    row2 = st.columns([1, 1, 1, 1])
    with row2[1]:
        st.markdown(algo_card_html(*algos[3]), unsafe_allow_html=True)
    with row2[2]:
        st.markdown(algo_card_html(*algos[4]), unsafe_allow_html=True)

    section_header(
        "🔬 Méthodologie",
        "Une approche académique structurée pour chaque algorithme.",
    )

    st.markdown(
        """
        <div class="glass-card">
            <div class="step-item">
                <div class="step-num">1</div>
                <div>
                    <strong style="color:#f8fafc;">Introduction & définition</strong>
                    <p style="margin:0.25rem 0 0 0; color:#94a3b8;">
                        Présentation claire du contexte et de l'intuition derrière l'algorithme.
                    </p>
                </div>
            </div>
            <div class="step-item">
                <div class="step-num">2</div>
                <div>
                    <strong style="color:#f8fafc;">Principe & formules</strong>
                    <p style="margin:0.25rem 0 0 0; color:#94a3b8;">
                        Explication logique, formules importantes et exemple mathématique simple.
                    </p>
                </div>
            </div>
            <div class="step-item">
                <div class="step-num">3</div>
                <div>
                    <strong style="color:#f8fafc;">Implémentation Scikit-Learn</strong>
                    <p style="margin:0.25rem 0 0 0; color:#94a3b8;">
                        Code Python propre, commenté et prêt à être réutilisé.
                    </p>
                </div>
            </div>
            <div class="step-item" style="border-bottom:none;">
                <div class="step-num">4</div>
                <div>
                    <strong style="color:#f8fafc;">Démo interactive & évaluation</strong>
                    <p style="margin:0.25rem 0 0 0; color:#94a3b8;">
                        Paramètres ajustables, visualisation Plotly, accuracy et matrice de confusion.
                    </p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header(
        "🛠️ Stack technique",
        "Outils utilisés pour construire cette bibliothèque interactive.",
    )

    tech_cols = st.columns(6)
    techs = [
        ("Streamlit", "Interface web"),
        ("Pandas", "Données"),
        ("NumPy", "Calcul"),
        ("Scikit-Learn", "Modèles ML"),
        ("Matplotlib", "Graphiques"),
        ("Plotly", "Interactivité"),
    ]
    for col, (name, desc) in zip(tech_cols, techs):
        with col:
            st.markdown(
                f"""
                <div class="glass-card" style="text-align:center; padding:1.2rem 0.8rem;">
                    <div style="font-weight:700; color:#f8fafc; margin-bottom:0.3rem;">{name}</div>
                    <div style="color:#64748b; font-size:0.85rem;">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    section_header(
        "🚀 Commencer l'exploration",
        "Utilisez le menu latéral pour accéder aux pages pédagogiques.",
    )

    st.markdown(
        """
        <div class="info-box">
            <strong style="color:#f8fafc;">Conseil :</strong>
            commencez par <em>Introduction ML</em> pour revisiter les bases,
            puis explorez chaque algorithme. Terminez par <em>Comparaison</em>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    footer()


# ---------------------------------------------------------------------------
# Configuration globale + navigation explicite (Streamlit 1.36+)
# ---------------------------------------------------------------------------
page_config("ML Academy Library")
inject_custom_css()
sidebar_brand()

st.sidebar.markdown("---")
st.sidebar.info(
    "Sélectionnez une page dans le menu ci-dessus pour explorer "
    "chaque algorithme et ses démonstrations interactives."
)

pages = {
    "🏠 Accueil": [
        st.Page(render_home, title="ML Academy Library", icon="🎓", default=True),
        st.Page("pages/1_Accueil.py", title="Introduction ML", icon="📖"),
    ],
    "🧠 Algorithmes": [
        st.Page("pages/2_KNN.py", title="KNN", icon="📍"),
        st.Page("pages/3_Decision_Tree.py", title="Decision Tree", icon="🌳"),
        st.Page("pages/4_SVM.py", title="SVM", icon="📐"),
        st.Page("pages/5_PCA.py", title="PCA", icon="📉"),
        st.Page("pages/6_LDA.py", title="LDA", icon="🎯"),
    ],
    "📊 Synthèse": [
        st.Page("pages/7_Comparaison.py", title="Comparaison", icon="⚖️"),
    ],
}

pg = st.navigation(pages)
pg.run()
