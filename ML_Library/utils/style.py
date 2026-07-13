"""
CSS global et composants HTML — ML Academy Library
Direction visuelle : « Midnight Observatory »
Encre profonde, teal académique, champagne doré, grain, mesh, motion.
"""

import streamlit as st


def inject_custom_css():
    """Injecte le design system premium du site."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=IBM+Plex+Mono:wght@400;500&display=swap');

        :root {
            --ink: #050a12;
            --ink-2: #0a1422;
            --ink-3: #101c2e;
            --surface: rgba(255, 255, 255, 0.035);
            --surface-2: rgba(255, 255, 255, 0.06);
            --surface-3: rgba(255, 255, 255, 0.09);
            --border: rgba(186, 230, 253, 0.12);
            --border-strong: rgba(125, 211, 252, 0.28);
            --text: #f1f5f9;
            --text-2: #a8b6c8;
            --text-3: #6b7c91;
            --teal: #2dd4bf;
            --cyan: #67e8f9;
            --sky: #7dd3fc;
            --gold: #e8c47c;
            --gold-soft: rgba(232, 196, 124, 0.14);
            --mint: #5eead4;
            --rose: #fb7185;
            --amber: #fbbf24;
            --grad-accent: linear-gradient(135deg, #0d9488 0%, #0891b2 55%, #38bdf8 100%);
            --grad-gold: linear-gradient(135deg, #e8c47c 0%, #f5e6c0 100%);
            --shadow-lg: 0 28px 80px rgba(0, 0, 0, 0.45);
            --shadow-glow: 0 0 60px rgba(45, 212, 191, 0.12);
            --radius: 22px;
            --radius-sm: 14px;
            --font-display: 'Syne', sans-serif;
            --font: 'DM Sans', sans-serif;
            --mono: 'IBM Plex Mono', monospace;
        }

        html, body, [class*="css"] {
            font-family: var(--font) !important;
        }

        .stApp {
            background: var(--ink) !important;
            color: var(--text) !important;
        }

        /* Atmosphere — mesh + grain + drifting light */
        .stApp::before {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
            background:
                radial-gradient(ellipse 90% 55% at 8% -5%, rgba(13, 148, 136, 0.28), transparent 55%),
                radial-gradient(ellipse 70% 45% at 92% 5%, rgba(14, 116, 144, 0.22), transparent 50%),
                radial-gradient(ellipse 60% 50% at 70% 95%, rgba(232, 196, 124, 0.07), transparent 55%),
                radial-gradient(ellipse 50% 40% at 20% 80%, rgba(56, 189, 248, 0.08), transparent 50%),
                linear-gradient(180deg, #050a12 0%, #071018 40%, #0a1524 100%);
            animation: ambience 18s ease-in-out infinite alternate;
        }

        .stApp::after {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
            opacity: 0.045;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
        }

        .main .block-container {
            padding-top: 1.25rem !important;
            padding-bottom: 5rem !important;
            max-width: 1200px !important;
            position: relative;
            z-index: 1;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: var(--font-display) !important;
            letter-spacing: -0.02em;
            color: var(--text) !important;
        }

        p, span, label, li, div {
            font-family: var(--font) !important;
        }

        /* ---------- Sidebar ---------- */
        [data-testid="stSidebar"] {
            background:
                linear-gradient(180deg, rgba(5, 10, 18, 0.97), rgba(10, 20, 34, 0.95)) !important;
            border-right: 1px solid var(--border) !important;
            backdrop-filter: blur(24px) saturate(1.2);
        }

        [data-testid="stSidebar"] > div:first-child {
            padding-top: 1.2rem;
        }

        [data-testid="stSidebarNav"] {
            padding-top: 0.5rem;
        }

        [data-testid="stSidebarNav"] a {
            border-radius: 12px !important;
            margin: 3px 6px !important;
            padding: 0.7rem 0.95rem !important;
            transition: all 0.28s cubic-bezier(0.22, 1, 0.36, 1) !important;
            border: 1px solid transparent !important;
            font-weight: 500 !important;
        }

        [data-testid="stSidebarNav"] a:hover {
            background: rgba(45, 212, 191, 0.08) !important;
            border-color: rgba(45, 212, 191, 0.22) !important;
            transform: translateX(5px);
        }

        [data-testid="stSidebarNav"] a[aria-selected="true"] {
            background: var(--grad-accent) !important;
            color: #041016 !important;
            font-weight: 700 !important;
            box-shadow: 0 10px 30px rgba(13, 148, 136, 0.35);
        }

        [data-testid="stSidebarNav"] [data-testid="stSidebarNavSeparator"] {
            margin: 0.8rem 0.6rem !important;
            border-color: rgba(255,255,255,0.06) !important;
        }

        /* Section labels in nav */
        [data-testid="stSidebarNav"] ul ul {
            margin-left: 0 !important;
        }

        /* ---------- Widgets ---------- */
        .stButton > button {
            background: var(--grad-accent) !important;
            color: #041016 !important;
            border: none !important;
            border-radius: 14px !important;
            padding: 0.7rem 1.5rem !important;
            font-family: var(--font-display) !important;
            font-weight: 700 !important;
            letter-spacing: 0.01em;
            box-shadow: 0 12px 32px rgba(13, 148, 136, 0.35);
            transition: all 0.28s cubic-bezier(0.22, 1, 0.36, 1) !important;
        }

        .stButton > button:hover {
            transform: translateY(-3px) scale(1.01);
            box-shadow: 0 18px 40px rgba(45, 212, 191, 0.4) !important;
            filter: brightness(1.06);
        }

        .stSelectbox > div > div,
        .stNumberInput > div > div,
        .stTextInput > div > div {
            border-radius: 12px !important;
            background: var(--surface) !important;
            border-color: var(--border) !important;
        }

        [data-testid="stMetric"] {
            background: linear-gradient(160deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1.15rem 1.25rem;
            backdrop-filter: blur(16px);
            box-shadow: var(--shadow-lg);
            position: relative;
            overflow: hidden;
            transition: transform 0.3s ease, border-color 0.3s ease;
        }

        [data-testid="stMetric"]::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 2px;
            background: var(--grad-accent);
            opacity: 0.85;
        }

        [data-testid="stMetric"]:hover {
            transform: translateY(-3px);
            border-color: var(--border-strong);
        }

        [data-testid="stMetricLabel"] {
            color: var(--text-3) !important;
            font-size: 0.78rem !important;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 600 !important;
        }

        [data-testid="stMetricValue"] {
            color: var(--cyan) !important;
            font-family: var(--font-display) !important;
            font-weight: 800 !important;
            font-size: 1.75rem !important;
        }

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background: transparent;
            border-bottom: none !important;
            padding: 0.25rem 0 0.75rem;
        }

        .stTabs [data-baseweb="tab"] {
            background: var(--surface) !important;
            border: 1px solid var(--border) !important;
            border-radius: 999px !important;
            color: var(--text-2) !important;
            padding: 0.55rem 1.15rem !important;
            font-weight: 500 !important;
            transition: all 0.25s ease !important;
        }

        .stTabs [data-baseweb="tab"]:hover {
            border-color: var(--border-strong) !important;
            color: var(--text) !important;
        }

        .stTabs [aria-selected="true"] {
            background: rgba(45, 212, 191, 0.12) !important;
            color: var(--teal) !important;
            border-color: rgba(45, 212, 191, 0.4) !important;
            box-shadow: 0 0 24px rgba(45, 212, 191, 0.15);
        }

        .streamlit-expanderHeader {
            background: var(--surface) !important;
            border-radius: var(--radius-sm) !important;
            border: 1px solid var(--border) !important;
        }

        .stCodeBlock, pre, code {
            font-family: var(--mono) !important;
            border-radius: 16px !important;
        }

        [data-testid="stDataFrame"] {
            border-radius: 16px !important;
            overflow: hidden;
            border: 1px solid var(--border);
            box-shadow: var(--shadow-lg);
        }

        /* Hide chrome */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        header[data-testid="stHeader"] {
            background: transparent !important;
        }

        /* =========================================================
           CUSTOM COMPONENTS
           ========================================================= */

        /* ---- Full-bleed home hero ---- */
        .home-hero {
            position: relative;
            margin: -0.5rem -1rem 2.5rem -1rem;
            min-height: min(78vh, 640px);
            border-radius: 0 0 36px 36px;
            overflow: hidden;
            display: flex;
            align-items: flex-end;
            padding: 3.5rem 2.75rem 3rem;
            isolation: isolate;
            animation: fadeUp 0.9s cubic-bezier(0.22, 1, 0.36, 1);
        }

        .home-hero__bg {
            position: absolute;
            inset: 0;
            z-index: 0;
            background:
                linear-gradient(180deg, transparent 0%, rgba(5,10,18,0.35) 45%, rgba(5,10,18,0.92) 100%),
                radial-gradient(ellipse 80% 70% at 75% 30%, rgba(13,148,136,0.45), transparent 55%),
                radial-gradient(ellipse 50% 50% at 15% 60%, rgba(14,116,144,0.3), transparent 50%),
                linear-gradient(135deg, #06101c 0%, #0a1f2e 40%, #0c2a32 70%, #071820 100%);
        }

        .home-hero__grid {
            position: absolute;
            inset: 0;
            z-index: 1;
            opacity: 0.35;
            background-image:
                linear-gradient(rgba(125, 211, 252, 0.07) 1px, transparent 1px),
                linear-gradient(90deg, rgba(125, 211, 252, 0.07) 1px, transparent 1px);
            background-size: 48px 48px;
            mask-image: radial-gradient(ellipse 70% 60% at 70% 35%, black 20%, transparent 75%);
            animation: gridDrift 28s linear infinite;
        }

        .home-hero__orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(40px);
            z-index: 1;
            animation: floatOrb 12s ease-in-out infinite;
        }

        .home-hero__orb--1 {
            width: 340px; height: 340px;
            right: 8%; top: 5%;
            background: rgba(45, 212, 191, 0.35);
        }

        .home-hero__orb--2 {
            width: 220px; height: 220px;
            right: 28%; top: 35%;
            background: rgba(232, 196, 124, 0.18);
            animation-delay: -4s;
        }

        .home-hero__svg {
            position: absolute;
            right: -2%;
            top: 8%;
            width: min(52%, 520px);
            height: auto;
            z-index: 2;
            opacity: 0.85;
            animation: fadeIn 1.2s ease 0.2s both, floatSoft 8s ease-in-out infinite;
        }

        .home-hero__content {
            position: relative;
            z-index: 3;
            max-width: 640px;
        }

        .home-hero__brand {
            font-family: var(--font-display) !important;
            font-size: clamp(2.8rem, 6.5vw, 4.6rem);
            font-weight: 800;
            line-height: 0.98;
            letter-spacing: -0.035em;
            margin: 0 0 1.1rem 0;
            color: #f8fafc;
            text-shadow: 0 8px 40px rgba(0,0,0,0.35);
        }

        .home-hero__brand span {
            display: block;
            background: linear-gradient(110deg, #f8fafc 10%, #99f6e4 42%, #67e8f9 68%, #e8c47c 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer 8s ease-in-out infinite;
        }

        .home-hero__line {
            font-size: clamp(1.05rem, 2vw, 1.25rem);
            color: var(--text-2);
            line-height: 1.65;
            margin: 0 0 1.75rem 0;
            max-width: 520px;
            font-weight: 400;
        }

        .home-hero__cta {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
        }

        .cta-chip {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.7rem 1.15rem;
            border-radius: 999px;
            background: rgba(255,255,255,0.06);
            border: 1px solid var(--border);
            color: var(--text);
            font-size: 0.92rem;
            font-weight: 500;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }

        .cta-chip:hover {
            border-color: var(--border-strong);
            background: rgba(45, 212, 191, 0.1);
            transform: translateY(-2px);
        }

        .cta-chip--gold {
            background: var(--gold-soft);
            border-color: rgba(232, 196, 124, 0.35);
            color: var(--gold);
        }

        /* ---- Page hero (inner pages) ---- */
        .page-hero {
            position: relative;
            padding: 2.75rem 2.4rem 2.5rem;
            border-radius: 28px;
            margin-bottom: 2rem;
            overflow: hidden;
            border: 1px solid var(--border);
            background:
                linear-gradient(145deg, rgba(16, 28, 46, 0.9), rgba(8, 24, 36, 0.75));
            box-shadow: var(--shadow-lg), var(--shadow-glow);
            animation: fadeUp 0.7s cubic-bezier(0.22, 1, 0.36, 1);
        }

        .page-hero::before {
            content: "";
            position: absolute;
            inset: 0;
            background:
                radial-gradient(ellipse 60% 80% at 100% 0%, rgba(45, 212, 191, 0.18), transparent 55%),
                radial-gradient(ellipse 40% 50% at 0% 100%, rgba(232, 196, 124, 0.08), transparent 50%);
            pointer-events: none;
        }

        .page-hero::after {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(125,211,252,0.45), transparent);
        }

        .page-hero__kicker {
            font-family: var(--font) !important;
            font-size: 0.78rem;
            font-weight: 600;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: var(--teal);
            margin: 0 0 0.85rem 0;
            position: relative;
        }

        .page-hero__title {
            font-family: var(--font-display) !important;
            font-size: clamp(2rem, 4vw, 3rem);
            font-weight: 800;
            line-height: 1.08;
            letter-spacing: -0.03em;
            margin: 0 0 0.85rem 0;
            position: relative;
            background: linear-gradient(120deg, #f8fafc 30%, #99f6e4 70%, #7dd3fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .page-hero__sub {
            font-size: 1.08rem;
            color: var(--text-2);
            max-width: 680px;
            line-height: 1.7;
            margin: 0;
            position: relative;
        }

        /* ---- Section headers ---- */
        .section-header {
            margin: 2.75rem 0 1.35rem 0;
            animation: fadeUp 0.55s ease;
        }

        .section-header__label {
            display: inline-block;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            color: var(--gold);
            margin-bottom: 0.45rem;
        }

        .section-header h2 {
            font-family: var(--font-display) !important;
            font-size: clamp(1.45rem, 2.5vw, 1.85rem);
            font-weight: 700;
            margin: 0 0 0.4rem 0;
            letter-spacing: -0.02em;
            color: var(--text);
        }

        .section-header p {
            color: var(--text-2);
            margin: 0;
            font-size: 1.02rem;
            max-width: 640px;
        }

        .section-header__rule {
            width: 56px;
            height: 3px;
            border-radius: 999px;
            background: var(--grad-accent);
            margin-top: 0.85rem;
        }

        /* ---- Cards ---- */
        .glass-card {
            background: linear-gradient(165deg, rgba(255,255,255,0.055), rgba(255,255,255,0.02));
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1.6rem 1.55rem;
            backdrop-filter: blur(18px);
            box-shadow: var(--shadow-lg);
            transition: all 0.35s cubic-bezier(0.22, 1, 0.36, 1);
            height: 100%;
            position: relative;
            overflow: hidden;
            animation: fadeUp 0.65s ease;
        }

        .glass-card::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.25), transparent);
        }

        .glass-card:hover {
            background: linear-gradient(165deg, rgba(255,255,255,0.08), rgba(255,255,255,0.03));
            transform: translateY(-5px);
            border-color: var(--border-strong);
            box-shadow: 0 32px 70px rgba(0,0,0,0.5), 0 0 40px rgba(45,212,191,0.08);
        }

        .glass-card h3 {
            font-family: var(--font-display) !important;
            margin: 0 0 0.55rem 0;
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text);
        }

        .glass-card p {
            margin: 0;
            color: var(--text-2);
            line-height: 1.65;
            font-size: 0.95rem;
        }

        .feature-icon {
            width: 48px;
            height: 48px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.35rem;
            margin-bottom: 1rem;
            background: rgba(45, 212, 191, 0.1);
            border: 1px solid rgba(45, 212, 191, 0.22);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.08);
        }

        /* Algo cards */
        .algo-card {
            background: linear-gradient(165deg, rgba(16,28,46,0.9), rgba(8,18,30,0.7));
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 1.7rem 1.55rem;
            height: 100%;
            transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
            position: relative;
            overflow: hidden;
            animation: fadeUp 0.7s ease;
        }

        .algo-card::after {
            content: "";
            position: absolute;
            width: 160px; height: 160px;
            right: -40px; top: -50px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(45,212,191,0.2), transparent 70%);
            transition: opacity 0.4s ease, transform 0.4s ease;
            opacity: 0.5;
        }

        .algo-card:hover {
            transform: translateY(-8px);
            border-color: rgba(45, 212, 191, 0.4);
            box-shadow: 0 28px 60px rgba(0,0,0,0.45), 0 0 50px rgba(45,212,191,0.12);
        }

        .algo-card:hover::after {
            opacity: 1;
            transform: scale(1.2);
        }

        .algo-icon {
            width: 54px;
            height: 54px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.55rem;
            background: linear-gradient(145deg, rgba(45,212,191,0.18), rgba(56,189,248,0.08));
            border: 1px solid rgba(45, 212, 191, 0.28);
            margin-bottom: 1.1rem;
            position: relative;
            z-index: 1;
            transition: transform 0.35s ease;
        }

        .algo-card:hover .algo-icon {
            transform: scale(1.08) rotate(-3deg);
        }

        .algo-card h3 {
            font-family: var(--font-display) !important;
            margin: 0 0 0.5rem 0;
            font-size: 1.22rem;
            font-weight: 700;
            color: var(--text);
            position: relative;
            z-index: 1;
        }

        .algo-card p {
            margin: 0;
            color: var(--text-2);
            font-size: 0.93rem;
            line-height: 1.6;
            position: relative;
            z-index: 1;
        }

        .algo-tag {
            display: inline-block;
            margin-top: 1.15rem;
            padding: 0.3rem 0.75rem;
            border-radius: 999px;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.04em;
            background: rgba(232, 196, 124, 0.1);
            color: var(--gold);
            border: 1px solid rgba(232, 196, 124, 0.28);
            position: relative;
            z-index: 1;
        }

        /* Info / formula */
        .info-box {
            background: linear-gradient(90deg, rgba(45,212,191,0.08), rgba(255,255,255,0.03));
            border-left: 3px solid var(--teal);
            border-radius: 0 16px 16px 0;
            padding: 1.15rem 1.35rem;
            margin: 1.1rem 0;
            backdrop-filter: blur(12px);
            border-top: 1px solid var(--border);
            border-right: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            color: var(--text-2);
            line-height: 1.65;
            animation: fadeUp 0.5s ease;
        }

        .info-box.warning {
            border-left-color: var(--amber);
            background: linear-gradient(90deg, rgba(251,191,36,0.08), rgba(255,255,255,0.03));
        }
        .info-box.success {
            border-left-color: var(--mint);
            background: linear-gradient(90deg, rgba(94,234,212,0.08), rgba(255,255,255,0.03));
        }
        .info-box.danger {
            border-left-color: var(--rose);
            background: linear-gradient(90deg, rgba(251,113,133,0.08), rgba(255,255,255,0.03));
        }

        .formula-box {
            position: relative;
            background:
                linear-gradient(160deg, rgba(8, 18, 30, 0.95), rgba(12, 28, 42, 0.85));
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 1.4rem 1.5rem;
            margin: 1.1rem 0;
            text-align: center;
            font-family: var(--mono) !important;
            color: var(--cyan);
            font-size: 1.08rem;
            overflow-x: auto;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.05), var(--shadow-lg);
            letter-spacing: 0.01em;
        }

        .formula-box::before {
            content: "FORMULE";
            position: absolute;
            top: 10px; left: 14px;
            font-family: var(--font) !important;
            font-size: 0.62rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            color: var(--text-3);
        }

        .formula-box > * , .formula-box {
            padding-top: 0.5rem;
        }

        /* Steps */
        .step-item {
            display: flex;
            gap: 1.1rem;
            padding: 1.15rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            transition: background 0.25s ease;
        }

        .step-item:hover {
            background: rgba(255,255,255,0.02);
        }

        .step-num {
            flex-shrink: 0;
            width: 40px;
            height: 40px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--grad-accent);
            color: #041016;
            font-family: var(--font-display) !important;
            font-weight: 800;
            font-size: 0.95rem;
            box-shadow: 0 8px 20px rgba(13, 148, 136, 0.3);
        }

        /* Tech pills */
        .tech-tile {
            text-align: center;
            padding: 1.35rem 0.75rem;
            border-radius: 18px;
            background: linear-gradient(165deg, rgba(255,255,255,0.05), rgba(255,255,255,0.015));
            border: 1px solid var(--border);
            transition: all 0.3s ease;
            height: 100%;
        }

        .tech-tile:hover {
            transform: translateY(-4px);
            border-color: var(--border-strong);
            box-shadow: 0 16px 40px rgba(0,0,0,0.3);
        }

        .tech-tile__name {
            font-family: var(--font-display) !important;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 0.3rem;
            font-size: 0.95rem;
        }

        .tech-tile__desc {
            color: var(--text-3);
            font-size: 0.8rem;
        }

        /* Journey strip */
        .journey {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 0.75rem;
            margin: 0.5rem 0 1rem;
        }

        .journey-step {
            padding: 1.2rem 1rem;
            border-radius: 18px;
            background: var(--surface);
            border: 1px solid var(--border);
            text-align: center;
            transition: all 0.3s ease;
            position: relative;
        }

        .journey-step:hover {
            border-color: var(--border-strong);
            transform: translateY(-3px);
            background: var(--surface-2);
        }

        .journey-step__n {
            font-family: var(--font-display) !important;
            font-size: 1.5rem;
            font-weight: 800;
            background: var(--grad-accent);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.35rem;
        }

        .journey-step__t {
            font-weight: 600;
            color: var(--text);
            font-size: 0.9rem;
            margin-bottom: 0.25rem;
        }

        .journey-step__d {
            color: var(--text-3);
            font-size: 0.78rem;
            line-height: 1.4;
        }

        /* Footer */
        .footer-bar {
            margin-top: 3.5rem;
            padding: 2rem 1rem 1rem;
            text-align: center;
            color: var(--text-3);
            border-top: 1px solid var(--border);
            font-size: 0.88rem;
            letter-spacing: 0.02em;
        }

        .footer-bar strong {
            color: var(--teal);
            font-family: var(--font-display) !important;
            font-weight: 700;
        }

        /* Sidebar brand */
        .sb-brand {
            padding: 0.35rem 0.35rem 1.4rem;
            border-bottom: 1px solid rgba(255,255,255,0.06);
            margin-bottom: 0.6rem;
        }

        .sb-brand__mark {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .sb-brand__logo {
            width: 42px;
            height: 42px;
            border-radius: 14px;
            background: var(--grad-accent);
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: var(--font-display) !important;
            font-weight: 800;
            color: #041016;
            font-size: 0.95rem;
            box-shadow: 0 10px 28px rgba(13, 148, 136, 0.4);
            flex-shrink: 0;
        }

        .sb-brand__name {
            font-family: var(--font-display) !important;
            font-size: 1.15rem;
            font-weight: 800;
            line-height: 1.15;
            background: linear-gradient(120deg, #f8fafc, #67e8f9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .sb-brand__sub {
            color: var(--text-3);
            font-size: 0.75rem;
            margin-top: 0.15rem;
            letter-spacing: 0.04em;
        }

        /* Markdown polish */
        .stMarkdown, .stMarkdown p, .stMarkdown li {
            color: var(--text-2) !important;
        }

        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: var(--text) !important;
            font-family: var(--font-display) !important;
        }

        hr {
            border: none !important;
            border-top: 1px solid var(--border) !important;
            margin: 2rem 0 !important;
        }

        /* Animations */
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(22px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 0.85; }
        }
        @keyframes shimmer {
            0%, 100% { background-position: 0% center; }
            50% { background-position: 100% center; }
        }
        @keyframes floatOrb {
            0%, 100% { transform: translate(0, 0) scale(1); }
            50% { transform: translate(-18px, 22px) scale(1.06); }
        }
        @keyframes floatSoft {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-12px); }
        }
        @keyframes gridDrift {
            from { background-position: 0 0; }
            to { background-position: 48px 48px; }
        }
        @keyframes ambience {
            from { filter: hue-rotate(0deg) brightness(1); }
            to { filter: hue-rotate(8deg) brightness(1.05); }
        }

        @media (max-width: 900px) {
            .home-hero {
                min-height: auto;
                margin: -0.5rem -0.5rem 2rem;
                padding: 2.5rem 1.5rem 2.2rem;
                border-radius: 0 0 28px 28px;
            }
            .home-hero__svg { opacity: 0.35; width: 70%; right: -15%; }
            .journey { grid-template-columns: 1fr 1fr; }
            .page-hero { padding: 2rem 1.4rem; }
        }

        @media (max-width: 560px) {
            .journey { grid-template-columns: 1fr; }
            .home-hero__brand { font-size: 2.4rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# Neural constellation SVG used as hero visual anchor
_HERO_SVG = """
<svg class="home-hero__svg" viewBox="0 0 520 420" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <linearGradient id="lg1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#2dd4bf" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.5"/>
    </linearGradient>
    <linearGradient id="lg2" x1="1" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e8c47c" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#2dd4bf" stop-opacity="0.2"/>
    </linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <g opacity="0.55" stroke="url(#lg1)" stroke-width="1.2">
    <line x1="80" y1="90" x2="180" y2="140"/><line x1="180" y1="140" x2="280" y2="80"/>
    <line x1="280" y1="80" x2="380" y2="130"/><line x1="180" y1="140" x2="220" y2="230"/>
    <line x1="220" y1="230" x2="320" y2="210"/><line x1="320" y1="210" x2="380" y2="130"/>
    <line x1="220" y1="230" x2="160" y2="320"/><line x1="320" y1="210" x2="360" y2="310"/>
    <line x1="160" y1="320" x2="260" y2="350"/><line x1="360" y1="310" x2="260" y2="350"/>
    <line x1="380" y1="130" x2="450" y2="200"/><line x1="450" y1="200" x2="360" y2="310"/>
    <line x1="80" y1="90" x2="100" y2="200"/><line x1="100" y1="200" x2="160" y2="320"/>
    <line x1="280" y1="80" x2="220" y2="230"/>
  </g>
  <g filter="url(#glow)">
    <circle cx="80" cy="90" r="6" fill="#67e8f9"/><circle cx="180" cy="140" r="9" fill="#2dd4bf"/>
    <circle cx="280" cy="80" r="7" fill="#e8c47c"/><circle cx="380" cy="130" r="8" fill="#38bdf8"/>
    <circle cx="220" cy="230" r="11" fill="#2dd4bf"/><circle cx="320" cy="210" r="7" fill="#67e8f9"/>
    <circle cx="160" cy="320" r="6" fill="#e8c47c"/><circle cx="360" cy="310" r="8" fill="#2dd4bf"/>
    <circle cx="260" cy="350" r="7" fill="#38bdf8"/><circle cx="450" cy="200" r="6" fill="#e8c47c"/>
    <circle cx="100" cy="200" r="5" fill="#67e8f9"/>
  </g>
  <path d="M60 360 Q160 300 260 340 T460 300" stroke="url(#lg2)" stroke-width="1.5" fill="none" opacity="0.5" stroke-dasharray="4 6"/>
</svg>
"""


def home_hero():
    """Hero full-bleed de la page d'accueil — composition unique brand-first."""
    st.markdown(
        f"""
        <section class="home-hero">
            <div class="home-hero__bg"></div>
            <div class="home-hero__grid"></div>
            <div class="home-hero__orb home-hero__orb--1"></div>
            <div class="home-hero__orb home-hero__orb--2"></div>
            {_HERO_SVG}
            <div class="home-hero__content">
                <h1 class="home-hero__brand">
                    <span>ML Academy</span>
                    <span>Library</span>
                </h1>
                <p class="home-hero__line">
                    La bibliothèque interactive pour comprendre, expérimenter
                    et comparer les algorithmes de Machine Learning.
                </p>
                <div class="home-hero__cta">
                    <span class="cta-chip cta-chip--gold">5 algorithmes</span>
                    <span class="cta-chip">Théorie &amp; code</span>
                    <span class="cta-chip">Démos live</span>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def hero(title: str, subtitle: str, badge: str = "ML Academy Library"):
    """Hero des pages internes — brand kicker + titre expressif."""
    st.markdown(
        f"""
        <div class="page-hero">
            <p class="page-hero__kicker">{badge}</p>
            <h1 class="page-hero__title">{title}</h1>
            <p class="page-hero__sub">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_header(title: str, subtitle: str = "", label: str = ""):
    """Titre de section avec filet accent et label optionnel."""
    # Strip leading emoji-heavy noise for cleaner hierarchy; keep title as provided
    lab = f'<div class="section-header__label">{label}</div>' if label else ""
    sub = f"<p>{subtitle}</p>" if subtitle else ""
    st.markdown(
        f"""
        <div class="section-header">
            {lab}
            <h2>{title}</h2>
            {sub}
            <div class="section-header__rule"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def info_box(text: str, kind: str = "info"):
    st.markdown(
        f'<div class="info-box {kind}">{text}</div>',
        unsafe_allow_html=True,
    )


def formula_box(formula: str):
    st.markdown(
        f'<div class="formula-box">{formula}</div>',
        unsafe_allow_html=True,
    )


def algo_card_html(icon: str, title: str, description: str, tag: str) -> str:
    return f"""
    <div class="algo-card">
        <div class="algo-icon">{icon}</div>
        <h3>{title}</h3>
        <p>{description}</p>
        <span class="algo-tag">{tag}</span>
    </div>
    """


def glass_card_html(title: str, body: str, icon: str = "📌") -> str:
    return f"""
    <div class="glass-card">
        <div class="feature-icon">{icon}</div>
        <h3>{title}</h3>
        <p>{body}</p>
    </div>
    """


def journey_strip_html() -> str:
    steps = [
        ("01", "Comprendre", "Définition & intuition"),
        ("02", "Formaliser", "Formules & logique"),
        ("03", "Coder", "Scikit-Learn clair"),
        ("04", "Expérimenter", "Démo & métriques"),
    ]
    items = "".join(
        f"""
        <div class="journey-step">
            <div class="journey-step__n">{n}</div>
            <div class="journey-step__t">{t}</div>
            <div class="journey-step__d">{d}</div>
        </div>
        """
        for n, t, d in steps
    )
    return f'<div class="journey">{items}</div>'


def footer():
    st.markdown(
        """
        <div class="footer-bar">
            <strong>ML Academy Library</strong>
            &nbsp;·&nbsp; Bibliothèque interactive de Machine Learning
            &nbsp;·&nbsp; Scikit-Learn · Streamlit · Plotly
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_config(page_title: str = "ML Academy Library"):
    st.set_page_config(
        page_title=page_title,
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def sidebar_brand():
    st.sidebar.markdown(
        """
        <div class="sb-brand">
            <div class="sb-brand__mark">
                <div class="sb-brand__logo">ML</div>
                <div>
                    <div class="sb-brand__name">ML Academy</div>
                    <div class="sb-brand__sub">Interactive Library</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
