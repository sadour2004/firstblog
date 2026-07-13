"""
CSS global et composants HTML pour ML Academy Library.
Design premium : glassmorphism, gradients, cards modernes.
"""

import streamlit as st


def inject_custom_css():
    """Injecte le CSS global du site (thème sombre académique premium)."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

        :root {
            --bg-primary: #0b1220;
            --bg-secondary: #111827;
            --bg-card: rgba(255, 255, 255, 0.05);
            --bg-card-hover: rgba(255, 255, 255, 0.09);
            --border-glass: rgba(255, 255, 255, 0.12);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --accent: #38bdf8;
            --accent-2: #22d3ee;
            --accent-soft: rgba(56, 189, 248, 0.15);
            --success: #34d399;
            --warning: #fbbf24;
            --danger: #f87171;
            --gradient-hero: linear-gradient(135deg, #0b1220 0%, #0f2744 45%, #0b3a4a 100%);
            --gradient-accent: linear-gradient(135deg, #0284c7 0%, #06b6d4 100%);
            --shadow-card: 0 20px 50px rgba(0, 0, 0, 0.35);
            --radius: 18px;
            --font: 'Outfit', sans-serif;
            --mono: 'JetBrains Mono', monospace;
        }

        /* ---------- Base Streamlit ---------- */
        .stApp {
            background: var(--gradient-hero) !important;
            font-family: var(--font) !important;
            color: var(--text-primary) !important;
        }

        .stApp::before {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            background:
                radial-gradient(ellipse 80% 50% at 10% -10%, rgba(56, 189, 248, 0.18), transparent 50%),
                radial-gradient(ellipse 60% 40% at 90% 10%, rgba(34, 211, 238, 0.12), transparent 45%),
                radial-gradient(ellipse 50% 40% at 50% 100%, rgba(14, 165, 233, 0.08), transparent 50%);
            z-index: 0;
        }

        .main .block-container {
            padding-top: 2rem !important;
            padding-bottom: 4rem !important;
            max-width: 1180px !important;
            position: relative;
            z-index: 1;
        }

        h1, h2, h3, h4, h5, h6, p, span, label, div {
            font-family: var(--font) !important;
        }

        /* ---------- Sidebar ---------- */
        [data-testid="stSidebar"] {
            background: rgba(8, 14, 26, 0.92) !important;
            border-right: 1px solid var(--border-glass) !important;
            backdrop-filter: blur(18px);
        }

        [data-testid="stSidebar"] * {
            color: var(--text-primary) !important;
        }

        [data-testid="stSidebarNav"] a {
            border-radius: 12px !important;
            margin: 4px 8px !important;
            padding: 0.65rem 0.9rem !important;
            transition: all 0.25s ease !important;
            border: 1px solid transparent !important;
        }

        [data-testid="stSidebarNav"] a:hover {
            background: var(--accent-soft) !important;
            border-color: rgba(56, 189, 248, 0.25) !important;
            transform: translateX(4px);
        }

        [data-testid="stSidebarNav"] a[aria-selected="true"] {
            background: var(--gradient-accent) !important;
            box-shadow: 0 8px 24px rgba(14, 165, 233, 0.35);
        }

        /* ---------- Widgets ---------- */
        .stButton > button {
            background: var(--gradient-accent) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.65rem 1.4rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.02em;
            box-shadow: 0 10px 28px rgba(14, 165, 233, 0.35);
            transition: all 0.25s ease !important;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 34px rgba(14, 165, 233, 0.45) !important;
            filter: brightness(1.08);
        }

        .stSelectbox > div > div,
        .stSlider > div,
        .stNumberInput > div > div,
        .stTextInput > div > div {
            border-radius: 12px !important;
        }

        [data-testid="stMetric"] {
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: var(--radius);
            padding: 1rem 1.2rem;
            backdrop-filter: blur(12px);
            box-shadow: var(--shadow-card);
        }

        [data-testid="stMetricLabel"] {
            color: var(--text-secondary) !important;
        }

        [data-testid="stMetricValue"] {
            color: var(--accent) !important;
            font-weight: 700 !important;
        }

        /* ---------- Tabs / Expanders ---------- */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background: transparent;
        }

        .stTabs [data-baseweb="tab"] {
            background: var(--bg-card) !important;
            border: 1px solid var(--border-glass) !important;
            border-radius: 12px !important;
            color: var(--text-secondary) !important;
            padding: 0.5rem 1rem !important;
        }

        .stTabs [aria-selected="true"] {
            background: var(--accent-soft) !important;
            color: var(--accent) !important;
            border-color: rgba(56, 189, 248, 0.35) !important;
        }

        .streamlit-expanderHeader {
            background: var(--bg-card) !important;
            border-radius: 12px !important;
            border: 1px solid var(--border-glass) !important;
        }

        /* ---------- Code ---------- */
        .stCodeBlock, pre, code {
            font-family: var(--mono) !important;
            border-radius: 14px !important;
        }

        /* ---------- Dataframes ---------- */
        [data-testid="stDataFrame"] {
            border-radius: 14px !important;
            overflow: hidden;
            border: 1px solid var(--border-glass);
        }

        /* ---------- Hide default chrome ---------- */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        header { visibility: hidden; }

        /* ---------- Custom components ---------- */
        .hero-section {
            position: relative;
            padding: 3.5rem 2.5rem;
            border-radius: 28px;
            background:
                linear-gradient(145deg, rgba(15, 39, 68, 0.85), rgba(11, 58, 74, 0.55)),
                radial-gradient(circle at top right, rgba(56, 189, 248, 0.25), transparent 45%);
            border: 1px solid var(--border-glass);
            box-shadow: var(--shadow-card);
            overflow: hidden;
            margin-bottom: 2rem;
            animation: fadeUp 0.7s ease;
        }

        .hero-section::after {
            content: "";
            position: absolute;
            width: 280px;
            height: 280px;
            right: -60px;
            top: -80px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(34, 211, 238, 0.35), transparent 70%);
            pointer-events: none;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.35rem 0.9rem;
            border-radius: 999px;
            background: var(--accent-soft);
            border: 1px solid rgba(56, 189, 248, 0.3);
            color: var(--accent);
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            margin-bottom: 1.2rem;
        }

        .hero-title {
            font-size: clamp(2.4rem, 5vw, 3.6rem);
            font-weight: 800;
            line-height: 1.1;
            margin: 0 0 1rem 0;
            background: linear-gradient(120deg, #f8fafc 20%, #7dd3fc 60%, #22d3ee 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero-subtitle {
            font-size: 1.15rem;
            color: var(--text-secondary);
            max-width: 720px;
            line-height: 1.7;
            margin: 0 0 1.8rem 0;
        }

        .hero-cta-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.8rem;
        }

        .hero-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.55rem 1rem;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border-glass);
            color: var(--text-primary);
            font-size: 0.92rem;
            font-weight: 500;
        }

        .section-header {
            margin: 2.2rem 0 1.2rem 0;
            animation: fadeUp 0.6s ease;
        }

        .section-header h2 {
            font-size: 1.75rem;
            font-weight: 700;
            margin: 0 0 0.4rem 0;
            color: var(--text-primary);
        }

        .section-header p {
            color: var(--text-secondary);
            margin: 0;
            font-size: 1.02rem;
        }

        .glass-card {
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: var(--radius);
            padding: 1.5rem;
            backdrop-filter: blur(16px);
            box-shadow: var(--shadow-card);
            transition: all 0.3s ease;
            height: 100%;
            animation: fadeUp 0.65s ease;
        }

        .glass-card:hover {
            background: var(--bg-card-hover);
            transform: translateY(-4px);
            border-color: rgba(56, 189, 248, 0.35);
            box-shadow: 0 24px 55px rgba(0, 0, 0, 0.4);
        }

        .algo-card {
            background: linear-gradient(160deg, rgba(255,255,255,0.07), rgba(255,255,255,0.03));
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 1.6rem;
            height: 100%;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .algo-card::before {
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(56,189,248,0.12), transparent 55%);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .algo-card:hover {
            transform: translateY(-6px);
            border-color: rgba(56, 189, 248, 0.4);
            box-shadow: 0 22px 48px rgba(14, 165, 233, 0.18);
        }

        .algo-card:hover::before { opacity: 1; }

        .algo-icon {
            width: 52px;
            height: 52px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            background: var(--accent-soft);
            border: 1px solid rgba(56, 189, 248, 0.25);
            margin-bottom: 1rem;
        }

        .algo-card h3 {
            margin: 0 0 0.5rem 0;
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--text-primary);
        }

        .algo-card p {
            margin: 0;
            color: var(--text-secondary);
            font-size: 0.95rem;
            line-height: 1.55;
        }

        .algo-tag {
            display: inline-block;
            margin-top: 1rem;
            padding: 0.25rem 0.7rem;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.03em;
            background: rgba(52, 211, 153, 0.12);
            color: var(--success);
            border: 1px solid rgba(52, 211, 153, 0.25);
        }

        .info-box {
            background: var(--bg-card);
            border-left: 4px solid var(--accent);
            border-radius: 0 14px 14px 0;
            padding: 1.1rem 1.3rem;
            margin: 1rem 0;
            backdrop-filter: blur(10px);
        }

        .info-box.warning { border-left-color: var(--warning); }
        .info-box.success { border-left-color: var(--success); }
        .info-box.danger { border-left-color: var(--danger); }

        .formula-box {
            background: rgba(8, 14, 26, 0.75);
            border: 1px solid var(--border-glass);
            border-radius: 14px;
            padding: 1.2rem 1.4rem;
            margin: 1rem 0;
            text-align: center;
            font-family: var(--mono) !important;
            color: #7dd3fc;
            font-size: 1.05rem;
            overflow-x: auto;
        }

        .metric-chip {
            display: inline-flex;
            flex-direction: column;
            gap: 0.2rem;
            min-width: 140px;
            padding: 1rem 1.2rem;
            border-radius: 16px;
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            backdrop-filter: blur(12px);
        }

        .metric-chip .label {
            color: var(--text-muted);
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .metric-chip .value {
            color: var(--accent);
            font-size: 1.6rem;
            font-weight: 700;
        }

        .step-item {
            display: flex;
            gap: 1rem;
            padding: 1rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.06);
        }

        .step-num {
            flex-shrink: 0;
            width: 36px;
            height: 36px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--gradient-accent);
            font-weight: 700;
            font-size: 0.9rem;
        }

        .footer-bar {
            margin-top: 3rem;
            padding: 1.5rem;
            text-align: center;
            color: var(--text-muted);
            border-top: 1px solid var(--border-glass);
            font-size: 0.9rem;
        }

        .pros-cons {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }

        @media (max-width: 768px) {
            .hero-section { padding: 2rem 1.3rem; }
            .pros-cons { grid-template-columns: 1fr; }
            .hero-title { font-size: 2.1rem; }
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(16px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Markdown text colors */
        .stMarkdown, .stMarkdown p, .stMarkdown li {
            color: var(--text-secondary) !important;
        }

        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: var(--text-primary) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def hero(title: str, subtitle: str, badge: str = "ML Academy Library"):
    """Affiche une section hero premium."""
    st.markdown(
        f"""
        <div class="hero-section">
            <div class="hero-badge">✨ {badge}</div>
            <h1 class="hero-title">{title}</h1>
            <p class="hero-subtitle">{subtitle}</p>
            <div class="hero-cta-row">
                <span class="hero-pill">📚 Théorie pédagogique</span>
                <span class="hero-pill">🧪 Démos interactives</span>
                <span class="hero-pill">📊 Visualisations Plotly</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_header(title: str, subtitle: str = ""):
    """Titre de section stylé."""
    sub = f"<p>{subtitle}</p>" if subtitle else ""
    st.markdown(
        f"""
        <div class="section-header">
            <h2>{title}</h2>
            {sub}
        </div>
        """,
        unsafe_allow_html=True,
    )


def info_box(text: str, kind: str = "info"):
    """Encadré informatif (info / warning / success / danger)."""
    st.markdown(
        f"""
        <div class="info-box {kind}">
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )


def formula_box(formula: str):
    """Affiche une formule mathématique dans un encadré monospace."""
    st.markdown(
        f"""
        <div class="formula-box">
            {formula}
        </div>
        """,
        unsafe_allow_html=True,
    )


def algo_card_html(icon: str, title: str, description: str, tag: str) -> str:
    """Retourne le HTML d'une carte algorithme."""
    return f"""
    <div class="algo-card">
        <div class="algo-icon">{icon}</div>
        <h3>{title}</h3>
        <p>{description}</p>
        <span class="algo-tag">{tag}</span>
    </div>
    """


def glass_card_html(title: str, body: str, icon: str = "📌") -> str:
    """Retourne le HTML d'une carte glassmorphism."""
    return f"""
    <div class="glass-card">
        <h3 style="margin:0 0 0.6rem 0; color:#f8fafc;">{icon} {title}</h3>
        <p style="margin:0; color:#94a3b8; line-height:1.6;">{body}</p>
    </div>
    """


def footer():
    """Pied de page du site."""
    st.markdown(
        """
        <div class="footer-bar">
            ML Academy Library · Bibliothèque interactive de Machine Learning ·
            Scikit-Learn · Streamlit · Plotly
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_config(page_title: str = "ML Academy Library"):
    """Configuration commune des pages Streamlit."""
    st.set_page_config(
        page_title=page_title,
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def sidebar_brand():
    """En-tête de la barre latérale."""
    st.sidebar.markdown(
        """
        <div style="padding: 0.5rem 0.2rem 1.2rem 0.2rem;">
            <div style="font-size:1.35rem; font-weight:800;
                        background: linear-gradient(120deg,#f8fafc,#38bdf8);
                        -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
                🎓 ML Academy
            </div>
            <div style="color:#64748b; font-size:0.85rem; margin-top:0.25rem;">
                Bibliothèque interactive
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
