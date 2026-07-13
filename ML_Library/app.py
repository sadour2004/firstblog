"""
ML Academy Library — Landing page premium.
Lancer : streamlit run app.py  (depuis ML_Library/)
"""

import streamlit as st

from utils.style import (
    inject_custom_css,
    home_hero,
    section_header,
    algo_card_html,
    glass_card_html,
    journey_strip_html,
    info_box,
    footer,
    page_config,
    sidebar_brand,
)


def render_home():
    """Landing page — composition brand-first."""
    home_hero()

    section_header(
        "Objectifs du projet",
        "Comprendre, visualiser et comparer les algorithmes du semestre.",
        label="Mission",
    )
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown(
            glass_card_html(
                "Apprendre",
                "Explications pédagogiques, formules essentielles et exemples "
                "mathématiques simples pour chaque algorithme.",
                "📖",
            ),
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            glass_card_html(
                "Expérimenter",
                "Sliders, hyperparamètres en direct et entraînements Scikit-Learn "
                "sur le dataset Iris.",
                "🧪",
            ),
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            glass_card_html(
                "Comparer",
                "Accuracy, matrices de confusion et graphiques Plotly pour "
                "évaluer et trancher entre les modèles.",
                "📊",
            ),
            unsafe_allow_html=True,
        )

    section_header(
        "Algorithmes étudiés",
        "Cinq piliers — classification et réduction de dimension.",
        label="Catalogue",
    )
    algos = [
        ("📍", "KNN", "Classification par proximité : vote des K voisins les plus proches.", "Supervisé · Classification"),
        ("🌳", "Decision Tree", "Partitions successives de l'espace selon Gini ou entropie.", "Supervisé · Classification"),
        ("📐", "SVM", "Hyperplan à marge maximale, kernels linéaire, RBF ou polynomial.", "Supervisé · Classification"),
        ("📉", "PCA", "Réduction non supervisée en maximisant la variance expliquée.", "Non supervisé · Réduction"),
        ("🎯", "LDA", "Réduction supervisée et classification par séparabilité des classes.", "Supervisé · Réduction / Classification"),
    ]
    row1 = st.columns(3, gap="medium")
    for col, algo in zip(row1, algos[:3]):
        with col:
            st.markdown(algo_card_html(*algo), unsafe_allow_html=True)

    st.markdown("<div style='height:0.85rem'></div>", unsafe_allow_html=True)
    row2 = st.columns([0.5, 1, 1, 0.5], gap="medium")
    with row2[1]:
        st.markdown(algo_card_html(*algos[3]), unsafe_allow_html=True)
    with row2[2]:
        st.markdown(algo_card_html(*algos[4]), unsafe_allow_html=True)

    section_header(
        "Méthodologie",
        "Une trajectoire académique claire pour chaque algorithme.",
        label="Parcours",
    )
    st.markdown(journey_strip_html(), unsafe_allow_html=True)

    section_header(
        "Stack technique",
        "Les outils derrière cette bibliothèque interactive.",
        label="Technologies",
    )
    tech_cols = st.columns(6)
    techs = [
        ("Streamlit", "Interface"),
        ("Pandas", "Données"),
        ("NumPy", "Calcul"),
        ("Scikit-Learn", "Modèles"),
        ("Matplotlib", "Figures"),
        ("Plotly", "Interactif"),
    ]
    for col, (name, desc) in zip(tech_cols, techs):
        with col:
            st.markdown(
                f"""
                <div class="tech-tile">
                  <div class="tech-tile__name">{name}</div>
                  <div class="tech-tile__desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    section_header(
        "Par où commencer ?",
        "Suggestion de parcours pour présenter le projet.",
        label="Guide",
    )
    info_box(
        "Commencez par <strong style='color:#f1f5f9;'>Introduction ML</strong>, "
        "explorez ensuite chaque algorithme (théorie → code → démo), "
        "puis terminez par <strong style='color:#f1f5f9;'>Comparaison</strong> "
        "pour la synthèse des performances sur Iris.",
        kind="success",
    )
    footer()


# ---------------------------------------------------------------------------
# Shell + navigation
# ---------------------------------------------------------------------------
page_config("ML Academy Library")
inject_custom_css()
sidebar_brand()

st.sidebar.markdown(
    """
    <div style="padding:0.35rem 0.2rem 0.9rem; color:#64768b; font-size:0.82rem; line-height:1.55;">
      Naviguez entre les sections pour explorer théorie, code et démos interactives.
    </div>
    """,
    unsafe_allow_html=True,
)

pages = {
    "Accueil": [
        st.Page(render_home, title="ML Academy Library", icon="🏠", default=True),
        st.Page("pages/1_Accueil.py", title="Introduction ML", icon="📖"),
    ],
    "Algorithmes": [
        st.Page("pages/2_KNN.py", title="KNN", icon="📍"),
        st.Page("pages/3_Decision_Tree.py", title="Decision Tree", icon="🌳"),
        st.Page("pages/4_SVM.py", title="SVM", icon="📐"),
        st.Page("pages/5_PCA.py", title="PCA", icon="📉"),
        st.Page("pages/6_LDA.py", title="LDA", icon="🎯"),
    ],
    "Synthèse": [
        st.Page("pages/7_Comparaison.py", title="Comparaison", icon="⚖️"),
    ],
}

pg = st.navigation(pages)
pg.run()
