"""
ML Academy Library — Design System & composants UI premium.

Direction visuelle : Midnight Observatory
Encre profonde · teal académique · champagne gold · glassmorphism · motion
"""

from __future__ import annotations

from typing import Optional, Sequence

import streamlit as st


# =============================================================================
# CSS GLOBAL
# =============================================================================

def inject_custom_css() -> None:
    """Injecte le design system CSS complet du site."""
    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=IBM+Plex+Mono:wght@400;500&display=swap');

:root {
  --ink: #04080f;
  --ink-2: #08111c;
  --ink-3: #0d1828;
  --surface: rgba(255,255,255,0.04);
  --surface-2: rgba(255,255,255,0.065);
  --surface-3: rgba(255,255,255,0.095);
  --border: rgba(148, 210, 230, 0.12);
  --border-strong: rgba(94, 234, 212, 0.32);
  --border-glow: rgba(45, 212, 191, 0.45);
  --text: #f1f5f9;
  --text-2: #a7b6c9;
  --text-3: #64768b;
  --teal: #2dd4bf;
  --cyan: #67e8f9;
  --sky: #7dd3fc;
  --gold: #e8c47c;
  --gold-soft: rgba(232,196,124,0.14);
  --mint: #5eead4;
  --rose: #fb7185;
  --amber: #fbbf24;
  --grad-accent: linear-gradient(135deg, #0f766e 0%, #0e7490 45%, #38bdf8 100%);
  --grad-gold: linear-gradient(135deg, #e8c47c, #f5e6c0);
  --grad-card: linear-gradient(165deg, rgba(255,255,255,0.07), rgba(255,255,255,0.015));
  --shadow-lg: 0 30px 80px rgba(0,0,0,0.5);
  --shadow-md: 0 16px 40px rgba(0,0,0,0.35);
  --shadow-glow: 0 0 50px rgba(45,212,191,0.14);
  --radius: 22px;
  --radius-sm: 14px;
  --font-display: 'Syne', sans-serif;
  --font: 'DM Sans', sans-serif;
  --mono: 'IBM Plex Mono', monospace;
}

html, body, [class*="css"] { font-family: var(--font) !important; }

.stApp {
  background: var(--ink) !important;
  color: var(--text) !important;
}

/* Atmosphere */
.stApp::before {
  content: "";
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background:
    radial-gradient(ellipse 95% 55% at 5% -8%, rgba(15,118,110,0.32), transparent 55%),
    radial-gradient(ellipse 70% 45% at 95% 0%, rgba(14,116,144,0.26), transparent 50%),
    radial-gradient(ellipse 55% 45% at 75% 100%, rgba(232,196,124,0.08), transparent 55%),
    radial-gradient(ellipse 45% 35% at 15% 85%, rgba(56,189,248,0.08), transparent 50%),
    linear-gradient(180deg, #04080f 0%, #071018 45%, #0a1524 100%);
  animation: ambience 20s ease-in-out infinite alternate;
}
.stApp::after {
  content: "";
  position: fixed; inset: 0; z-index: 0; pointer-events: none; opacity: 0.04;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

.main .block-container {
  padding-top: 1.1rem !important;
  padding-bottom: 4.5rem !important;
  max-width: 1180px !important;
  position: relative; z-index: 1;
}

h1,h2,h3,h4,h5,h6 {
  font-family: var(--font-display) !important;
  letter-spacing: -0.02em;
  color: var(--text) !important;
}
p, span, label, li, div { font-family: var(--font) !important; }

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, rgba(4,8,15,0.98), rgba(8,17,28,0.96)) !important;
  border-right: 1px solid var(--border) !important;
  backdrop-filter: blur(28px) saturate(1.25);
}
[data-testid="stSidebarNav"] a {
  border-radius: 12px !important;
  margin: 3px 6px !important;
  padding: 0.68rem 0.95rem !important;
  transition: all 0.28s cubic-bezier(0.22,1,0.36,1) !important;
  border: 1px solid transparent !important;
  font-weight: 500 !important;
}
[data-testid="stSidebarNav"] a:hover {
  background: rgba(45,212,191,0.09) !important;
  border-color: rgba(45,212,191,0.22) !important;
  transform: translateX(5px);
}
[data-testid="stSidebarNav"] a[aria-selected="true"] {
  background: var(--grad-accent) !important;
  color: #031018 !important;
  font-weight: 700 !important;
  box-shadow: 0 12px 32px rgba(15,118,110,0.4);
}

/* ---------- Buttons ---------- */
.stButton > button {
  background: var(--grad-accent) !important;
  color: #031018 !important;
  border: none !important;
  border-radius: 14px !important;
  padding: 0.7rem 1.45rem !important;
  font-family: var(--font-display) !important;
  font-weight: 700 !important;
  box-shadow: 0 12px 32px rgba(15,118,110,0.38);
  transition: all 0.28s cubic-bezier(0.22,1,0.36,1) !important;
}
.stButton > button:hover {
  transform: translateY(-3px) scale(1.01);
  box-shadow: 0 18px 42px rgba(45,212,191,0.42) !important;
  filter: brightness(1.06);
}

/* ---------- Inputs ---------- */
.stSelectbox > div > div,
.stNumberInput > div > div,
.stTextInput > div > div,
[data-baseweb="select"] > div {
  border-radius: 12px !important;
  background: rgba(255,255,255,0.04) !important;
  border-color: var(--border) !important;
}
.stSlider [data-baseweb="slider"] div[role="slider"] {
  background: var(--teal) !important;
}

/* ---------- Hide default metric chrome (we use custom) ---------- */
[data-testid="stMetric"] {
  background: var(--grad-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.1rem 1.2rem;
  box-shadow: var(--shadow-md);
  position: relative; overflow: hidden;
}
[data-testid="stMetric"]::before {
  content:""; position:absolute; top:0; left:0; right:0; height:2px;
  background: var(--grad-accent);
}
[data-testid="stMetricLabel"] {
  color: var(--text-3) !important;
  text-transform: uppercase; letter-spacing: 0.08em;
  font-size: 0.75rem !important; font-weight: 600 !important;
}
[data-testid="stMetricValue"] {
  color: var(--cyan) !important;
  font-family: var(--font-display) !important;
  font-weight: 800 !important;
}

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab-list"] {
  gap: 10px; background: transparent; border-bottom: none !important;
  padding: 0.2rem 0 0.9rem;
}
.stTabs [data-baseweb="tab"] {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 999px !important;
  color: var(--text-2) !important;
  padding: 0.55rem 1.2rem !important;
  font-weight: 500 !important;
  transition: all 0.25s ease !important;
}
.stTabs [data-baseweb="tab"]:hover {
  border-color: var(--border-strong) !important; color: var(--text) !important;
}
.stTabs [aria-selected="true"] {
  background: rgba(45,212,191,0.14) !important;
  color: var(--teal) !important;
  border-color: rgba(45,212,191,0.42) !important;
  box-shadow: 0 0 28px rgba(45,212,191,0.16);
}

/* ---------- Bordered containers = premium panels ---------- */
div[data-testid="stVerticalBlockBorderWrapper"] {
  background: var(--grad-card) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  box-shadow: var(--shadow-lg), var(--shadow-glow) !important;
  padding: 0.35rem 0.15rem 0.6rem !important;
  position: relative;
  overflow: hidden;
}
div[data-testid="stVerticalBlockBorderWrapper"]::before {
  content:""; position:absolute; top:0; left:0; right:0; height:1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.28), transparent);
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
div[data-testid="stCode"] {
  border: 1px solid var(--border) !important;
  border-radius: 16px !important;
  box-shadow: var(--shadow-md);
  overflow: hidden;
}

[data-testid="stDataFrame"] {
  border-radius: 16px !important;
  overflow: hidden;
  border: 1px solid var(--border);
  box-shadow: var(--shadow-md);
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent !important; }

.stMarkdown, .stMarkdown p, .stMarkdown li { color: var(--text-2) !important; }
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
  color: var(--text) !important;
  font-family: var(--font-display) !important;
}
hr { border: none !important; border-top: 1px solid var(--border) !important; margin: 1.8rem 0 !important; }

/* =========================================================
   CUSTOM COMPONENTS
   ========================================================= */

/* Sidebar brand */
.sb-brand {
  padding: 0.4rem 0.3rem 1.35rem;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  margin-bottom: 0.65rem;
}
.sb-brand__mark { display:flex; align-items:center; gap:0.75rem; }
.sb-brand__logo {
  width:44px; height:44px; border-radius:14px;
  background: var(--grad-accent);
  display:flex; align-items:center; justify-content:center;
  font-family: var(--font-display) !important; font-weight:800;
  color:#031018; font-size:0.95rem;
  box-shadow: 0 12px 30px rgba(15,118,110,0.45);
  flex-shrink:0;
}
.sb-brand__name {
  font-family: var(--font-display) !important;
  font-size:1.15rem; font-weight:800; line-height:1.15;
  background: linear-gradient(120deg,#f8fafc,#67e8f9);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
.sb-brand__sub { color:var(--text-3); font-size:0.74rem; margin-top:0.15rem; letter-spacing:0.05em; }

/* Home hero */
.home-hero {
  position: relative;
  margin: -0.4rem -0.9rem 2.4rem -0.9rem;
  min-height: min(76vh, 620px);
  border-radius: 0 0 36px 36px;
  overflow: hidden;
  display: flex; align-items: flex-end;
  padding: 3.4rem 2.7rem 2.9rem;
  isolation: isolate;
  animation: fadeUp 0.9s cubic-bezier(0.22,1,0.36,1);
}
.home-hero__bg {
  position:absolute; inset:0; z-index:0;
  background:
    linear-gradient(180deg, transparent 0%, rgba(4,8,15,0.4) 48%, rgba(4,8,15,0.94) 100%),
    radial-gradient(ellipse 80% 70% at 78% 28%, rgba(15,118,110,0.48), transparent 55%),
    radial-gradient(ellipse 50% 50% at 12% 55%, rgba(14,116,144,0.32), transparent 50%),
    linear-gradient(135deg, #05101c 0%, #0a1f2e 42%, #0c2a32 72%, #061820 100%);
}
.home-hero__grid {
  position:absolute; inset:0; z-index:1; opacity:0.32;
  background-image:
    linear-gradient(rgba(125,211,252,0.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(125,211,252,0.08) 1px, transparent 1px);
  background-size: 48px 48px;
  mask-image: radial-gradient(ellipse 70% 60% at 72% 32%, black 20%, transparent 75%);
  animation: gridDrift 30s linear infinite;
}
.home-hero__orb {
  position:absolute; border-radius:50%; filter:blur(42px); z-index:1;
  animation: floatOrb 12s ease-in-out infinite;
}
.home-hero__orb--1 { width:340px; height:340px; right:8%; top:4%; background:rgba(45,212,191,0.36); }
.home-hero__orb--2 { width:220px; height:220px; right:28%; top:36%; background:rgba(232,196,124,0.18); animation-delay:-4s; }
.home-hero__svg {
  position:absolute; right:-2%; top:8%; width:min(52%,520px); height:auto;
  z-index:2; opacity:0.88;
  animation: fadeIn 1.2s ease 0.2s both, floatSoft 8s ease-in-out infinite;
}
.home-hero__content { position:relative; z-index:3; max-width:640px; }
.home-hero__brand {
  font-family: var(--font-display) !important;
  font-size: clamp(2.7rem, 6.4vw, 4.5rem);
  font-weight:800; line-height:0.98; letter-spacing:-0.035em;
  margin:0 0 1.05rem 0; color:#f8fafc;
  text-shadow: 0 8px 40px rgba(0,0,0,0.35);
}
.home-hero__brand span {
  display:block;
  background: linear-gradient(110deg, #f8fafc 10%, #99f6e4 40%, #67e8f9 68%, #e8c47c 100%);
  background-size: 200% auto;
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
  animation: shimmer 8s ease-in-out infinite;
}
.home-hero__line {
  font-size: clamp(1.02rem, 2vw, 1.22rem);
  color: var(--text-2); line-height:1.65; margin:0 0 1.7rem 0;
  max-width:520px; font-weight:400;
}
.home-hero__cta { display:flex; flex-wrap:wrap; gap:0.7rem; }
.cta-chip {
  display:inline-flex; align-items:center; gap:0.45rem;
  padding:0.68rem 1.12rem; border-radius:999px;
  background: rgba(255,255,255,0.06); border:1px solid var(--border);
  color:var(--text); font-size:0.9rem; font-weight:500;
  backdrop-filter: blur(10px); transition: all 0.3s ease;
}
.cta-chip:hover { border-color:var(--border-strong); background:rgba(45,212,191,0.1); transform:translateY(-2px); }
.cta-chip--gold { background:var(--gold-soft); border-color:rgba(232,196,124,0.35); color:var(--gold); }

/* Page hero */
.page-hero {
  position:relative; padding:2.6rem 2.3rem 2.4rem; border-radius:28px;
  margin-bottom:1.8rem; overflow:hidden;
  border:1px solid var(--border);
  background: linear-gradient(145deg, rgba(13,24,40,0.92), rgba(8,24,36,0.78));
  box-shadow: var(--shadow-lg), var(--shadow-glow);
  animation: fadeUp 0.7s cubic-bezier(0.22,1,0.36,1);
}
.page-hero::before {
  content:""; position:absolute; inset:0; pointer-events:none;
  background:
    radial-gradient(ellipse 60% 80% at 100% 0%, rgba(45,212,191,0.18), transparent 55%),
    radial-gradient(ellipse 40% 50% at 0% 100%, rgba(232,196,124,0.08), transparent 50%);
}
.page-hero::after {
  content:""; position:absolute; top:0; left:0; right:0; height:1px;
  background: linear-gradient(90deg, transparent, rgba(125,211,252,0.5), transparent);
}
.page-hero__kicker {
  font-size:0.76rem; font-weight:700; letter-spacing:0.15em; text-transform:uppercase;
  color:var(--teal); margin:0 0 0.8rem 0; position:relative;
}
.page-hero__title {
  font-family: var(--font-display) !important;
  font-size: clamp(1.9rem, 3.8vw, 2.85rem);
  font-weight:800; line-height:1.08; letter-spacing:-0.03em;
  margin:0 0 0.8rem 0; position:relative;
  background: linear-gradient(120deg, #f8fafc 30%, #99f6e4 70%, #7dd3fc 100%);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
.page-hero__sub {
  font-size:1.05rem; color:var(--text-2); max-width:680px; line-height:1.7; margin:0; position:relative;
}

/* Section header */
.section-header { margin:2.5rem 0 1.25rem 0; animation: fadeUp 0.5s ease; }
.section-header__label {
  display:inline-block; font-size:0.7rem; font-weight:700; letter-spacing:0.16em;
  text-transform:uppercase; color:var(--gold); margin-bottom:0.4rem;
}
.section-header h2 {
  font-family: var(--font-display) !important;
  font-size: clamp(1.4rem, 2.4vw, 1.8rem);
  font-weight:700; margin:0 0 0.35rem 0; letter-spacing:-0.02em; color:var(--text);
}
.section-header p { color:var(--text-2); margin:0; font-size:1rem; max-width:640px; }
.section-header__rule {
  width:56px; height:3px; border-radius:999px; background:var(--grad-accent); margin-top:0.8rem;
}

/* Glass / algo cards */
.glass-card {
  background: var(--grad-card); border:1px solid var(--border); border-radius:var(--radius);
  padding:1.55rem 1.5rem; backdrop-filter:blur(18px); box-shadow:var(--shadow-lg);
  transition: all 0.35s cubic-bezier(0.22,1,0.36,1); height:100%; position:relative; overflow:hidden;
  animation: fadeUp 0.6s ease;
}
.glass-card::before {
  content:""; position:absolute; top:0; left:0; right:0; height:1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.28), transparent);
}
.glass-card:hover {
  transform: translateY(-5px); border-color:var(--border-strong);
  box-shadow: 0 34px 72px rgba(0,0,0,0.52), 0 0 40px rgba(45,212,191,0.1);
}
.glass-card h3 {
  font-family: var(--font-display) !important; margin:0 0 0.5rem 0;
  font-size:1.12rem; font-weight:700; color:var(--text);
}
.glass-card p { margin:0; color:var(--text-2); line-height:1.65; font-size:0.94rem; }
.feature-icon {
  width:48px; height:48px; border-radius:14px; display:flex; align-items:center; justify-content:center;
  font-size:1.3rem; margin-bottom:0.95rem;
  background: rgba(45,212,191,0.1); border:1px solid rgba(45,212,191,0.24);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.08);
}

.algo-card {
  background: linear-gradient(165deg, rgba(13,24,40,0.95), rgba(6,16,28,0.75));
  border:1px solid var(--border); border-radius:24px; padding:1.65rem 1.5rem; height:100%;
  transition: all 0.4s cubic-bezier(0.22,1,0.36,1); position:relative; overflow:hidden;
  animation: fadeUp 0.65s ease;
}
.algo-card::after {
  content:""; position:absolute; width:160px; height:160px; right:-40px; top:-50px; border-radius:50%;
  background: radial-gradient(circle, rgba(45,212,191,0.22), transparent 70%);
  transition: opacity 0.4s, transform 0.4s; opacity:0.5;
}
.algo-card:hover {
  transform: translateY(-8px); border-color:rgba(45,212,191,0.42);
  box-shadow: 0 28px 60px rgba(0,0,0,0.48), 0 0 50px rgba(45,212,191,0.14);
}
.algo-card:hover::after { opacity:1; transform:scale(1.2); }
.algo-icon {
  width:54px; height:54px; border-radius:16px; display:flex; align-items:center; justify-content:center;
  font-size:1.5rem; margin-bottom:1.05rem; position:relative; z-index:1;
  background: linear-gradient(145deg, rgba(45,212,191,0.2), rgba(56,189,248,0.08));
  border:1px solid rgba(45,212,191,0.3); transition: transform 0.35s ease;
}
.algo-card:hover .algo-icon { transform: scale(1.08) rotate(-3deg); }
.algo-card h3 {
  font-family: var(--font-display) !important; margin:0 0 0.45rem 0;
  font-size:1.2rem; font-weight:700; color:var(--text); position:relative; z-index:1;
}
.algo-card p { margin:0; color:var(--text-2); font-size:0.92rem; line-height:1.6; position:relative; z-index:1; }
.algo-tag {
  display:inline-block; margin-top:1.1rem; padding:0.28rem 0.72rem; border-radius:999px;
  font-size:0.7rem; font-weight:600; letter-spacing:0.04em;
  background: rgba(232,196,124,0.1); color:var(--gold);
  border:1px solid rgba(232,196,124,0.28); position:relative; z-index:1;
}

/* Metric card custom */
.metric-card {
  background: var(--grad-card); border:1px solid var(--border); border-radius:20px;
  padding:1.2rem 1.25rem; height:100%; position:relative; overflow:hidden;
  box-shadow: var(--shadow-md); transition: all 0.3s ease; animation: fadeUp 0.45s ease;
}
.metric-card::before {
  content:""; position:absolute; top:0; left:0; right:0; height:2px; background:var(--grad-accent);
}
.metric-card:hover { transform:translateY(-3px); border-color:var(--border-strong); box-shadow:var(--shadow-lg); }
.metric-card__top { display:flex; align-items:center; justify-content:space-between; margin-bottom:0.55rem; }
.metric-card__label {
  color:var(--text-3); font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:0.1em;
}
.metric-card__icon {
  width:32px; height:32px; border-radius:10px; display:flex; align-items:center; justify-content:center;
  background: rgba(45,212,191,0.12); border:1px solid rgba(45,212,191,0.22); font-size:0.95rem;
}
.metric-card__value {
  font-family: var(--font-display) !important;
  font-size:1.75rem; font-weight:800; color:var(--cyan); letter-spacing:-0.02em; line-height:1.1;
}
.metric-card__hint { margin-top:0.35rem; color:var(--text-3); font-size:0.78rem; }

/* Info / formula */
.info-box {
  background: linear-gradient(90deg, rgba(45,212,191,0.09), rgba(255,255,255,0.03));
  border-left:3px solid var(--teal); border-radius:0 16px 16px 0;
  padding:1.1rem 1.3rem; margin:1rem 0; color:var(--text-2); line-height:1.65;
  border-top:1px solid var(--border); border-right:1px solid var(--border); border-bottom:1px solid var(--border);
  animation: fadeUp 0.45s ease;
}
.info-box.warning { border-left-color:var(--amber); background:linear-gradient(90deg, rgba(251,191,36,0.09), rgba(255,255,255,0.03)); }
.info-box.success { border-left-color:var(--mint); background:linear-gradient(90deg, rgba(94,234,212,0.09), rgba(255,255,255,0.03)); }
.info-box.danger { border-left-color:var(--rose); background:linear-gradient(90deg, rgba(251,113,133,0.09), rgba(255,255,255,0.03)); }

.formula-box {
  position:relative;
  background: linear-gradient(160deg, rgba(6,14,24,0.96), rgba(10,26,40,0.88));
  border:1px solid var(--border); border-radius:18px; padding:1.55rem 1.5rem 1.3rem;
  margin:1rem 0; text-align:center; font-family:var(--mono) !important;
  color:var(--cyan); font-size:1.08rem; overflow-x:auto;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.05), var(--shadow-lg);
}
.formula-box::before {
  content:"FORMULE"; position:absolute; top:10px; left:14px;
  font-family:var(--font) !important; font-size:0.6rem; font-weight:700;
  letter-spacing:0.14em; color:var(--text-3);
}

/* Panel titles inside bordered containers */
.panel-title {
  font-family: var(--font-display) !important;
  font-size:1.05rem; font-weight:700; color:var(--text); margin:0.15rem 0 0.15rem 0;
}
.panel-sub { color:var(--text-3); font-size:0.88rem; margin:0 0 0.75rem 0; }

.plot-card-title {
  font-family: var(--font-display) !important;
  font-size:1rem; font-weight:700; color:var(--text); margin:0 0 0.2rem 0;
}
.plot-card-sub { color:var(--text-3); font-size:0.82rem; margin:0 0 0.65rem 0; }

.badge {
  display:inline-flex; align-items:center; gap:0.3rem;
  padding:0.28rem 0.7rem; border-radius:999px; font-size:0.72rem; font-weight:700;
  letter-spacing:0.04em; border:1px solid var(--border);
  background: var(--surface-2); color:var(--text-2);
}
.badge--teal { background:rgba(45,212,191,0.12); border-color:rgba(45,212,191,0.3); color:var(--teal); }
.badge--gold { background:var(--gold-soft); border-color:rgba(232,196,124,0.3); color:var(--gold); }

/* Steps */
.step-item {
  display:flex; gap:1.05rem; padding:1.1rem 0;
  border-bottom:1px solid rgba(255,255,255,0.05);
}
.step-num {
  flex-shrink:0; width:40px; height:40px; border-radius:12px;
  display:flex; align-items:center; justify-content:center;
  background:var(--grad-accent); color:#031018;
  font-family:var(--font-display) !important; font-weight:800; font-size:0.95rem;
  box-shadow: 0 8px 20px rgba(15,118,110,0.32);
}

/* Journey / tech */
.journey { display:grid; grid-template-columns:repeat(4,1fr); gap:0.75rem; margin:0.4rem 0 1rem; }
.journey-step {
  padding:1.15rem 1rem; border-radius:18px; background:var(--surface);
  border:1px solid var(--border); text-align:center; transition:all 0.3s ease;
}
.journey-step:hover { border-color:var(--border-strong); transform:translateY(-3px); background:var(--surface-2); }
.journey-step__n {
  font-family:var(--font-display) !important; font-size:1.45rem; font-weight:800;
  background:var(--grad-accent); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
  margin-bottom:0.3rem;
}
.journey-step__t { font-weight:600; color:var(--text); font-size:0.9rem; margin-bottom:0.2rem; }
.journey-step__d { color:var(--text-3); font-size:0.76rem; line-height:1.4; }

.tech-tile {
  text-align:center; padding:1.3rem 0.7rem; border-radius:18px;
  background:var(--grad-card); border:1px solid var(--border); transition:all 0.3s ease; height:100%;
}
.tech-tile:hover { transform:translateY(-4px); border-color:var(--border-strong); box-shadow:var(--shadow-md); }
.tech-tile__name { font-family:var(--font-display) !important; font-weight:700; color:var(--text); margin-bottom:0.25rem; font-size:0.92rem; }
.tech-tile__desc { color:var(--text-3); font-size:0.78rem; }

.footer-bar {
  margin-top:3.2rem; padding:2rem 1rem 0.8rem; text-align:center;
  color:var(--text-3); border-top:1px solid var(--border); font-size:0.86rem; letter-spacing:0.02em;
}
.footer-bar strong { color:var(--teal); font-family:var(--font-display) !important; font-weight:700; }

/* Animations */
@keyframes fadeUp { from { opacity:0; transform:translateY(20px); } to { opacity:1; transform:translateY(0); } }
@keyframes fadeIn { from { opacity:0; } to { opacity:0.88; } }
@keyframes shimmer { 0%,100% { background-position:0% center; } 50% { background-position:100% center; } }
@keyframes floatOrb { 0%,100% { transform:translate(0,0) scale(1); } 50% { transform:translate(-16px,20px) scale(1.05); } }
@keyframes floatSoft { 0%,100% { transform:translateY(0); } 50% { transform:translateY(-12px); } }
@keyframes gridDrift { from { background-position:0 0; } to { background-position:48px 48px; } }
@keyframes ambience { from { filter:hue-rotate(0deg) brightness(1); } to { filter:hue-rotate(8deg) brightness(1.04); } }

@media (max-width:900px) {
  .home-hero { min-height:auto; margin:-0.4rem -0.4rem 2rem; padding:2.4rem 1.4rem 2.1rem; border-radius:0 0 28px 28px; }
  .home-hero__svg { opacity:0.32; width:70%; right:-15%; }
  .journey { grid-template-columns:1fr 1fr; }
  .page-hero { padding:1.9rem 1.35rem; }
}
@media (max-width:560px) {
  .journey { grid-template-columns:1fr; }
  .home-hero__brand { font-size:2.35rem; }
}
</style>
        """,
        unsafe_allow_html=True,
    )


# =============================================================================
# COMPOSANTS UI
# =============================================================================

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


def page_config(title: str = "ML Academy Library") -> None:
    """Configuration commune des pages."""
    st.set_page_config(
        page_title=title,
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def sidebar_brand() -> None:
    """Logo / marque dans la sidebar."""
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


def home_hero() -> None:
    """Hero full-bleed de la landing — brand first."""
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


def hero(title: str, subtitle: str, badge: str = "ML Academy Library") -> None:
    """Hero premium des pages internes."""
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


def section_header(title: str, subtitle: str = "", label: Optional[str] = None) -> None:
    """Titre de section avec filet accent."""
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


def glass_card_html(title: str, text: str, icon: str = "📌") -> str:
    """Carte glassmorphism (HTML string)."""
    return f"""
    <div class="glass-card">
      <div class="feature-icon">{icon}</div>
      <h3>{title}</h3>
      <p>{text}</p>
    </div>
    """


def algo_card_html(icon: str, title: str, description: str, tag: str) -> str:
    """Carte algorithme (HTML string)."""
    return f"""
    <div class="algo-card">
      <div class="algo-icon">{icon}</div>
      <h3>{title}</h3>
      <p>{description}</p>
      <span class="algo-tag">{tag}</span>
    </div>
    """


def metric_card(
    label: str,
    value: str,
    icon: Optional[str] = None,
    hint: str = "",
) -> None:
    """Metric card HTML premium (remplace st.metric)."""
    icon_html = f'<div class="metric-card__icon">{icon}</div>' if icon else ""
    hint_html = f'<div class="metric-card__hint">{hint}</div>' if hint else ""
    st.markdown(
        f"""
        <div class="metric-card">
          <div class="metric-card__top">
            <div class="metric-card__label">{label}</div>
            {icon_html}
          </div>
          <div class="metric-card__value">{value}</div>
          {hint_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_score_metrics(metrics: dict) -> None:
    """Affiche Accuracy / Precision / Recall / F1 en metric cards."""
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Accuracy", f"{metrics['accuracy']:.3f}", "🎯")
    with c2:
        metric_card("Precision", f"{metrics['precision']:.3f}", "📐")
    with c3:
        metric_card("Recall", f"{metrics['recall']:.3f}", "📡")
    with c4:
        metric_card("F1-Score", f"{metrics['f1']:.3f}", "⭐")


def formula_box(formula: str) -> None:
    """Bloc formule mathématique stylé."""
    st.markdown(f'<div class="formula-box">{formula}</div>', unsafe_allow_html=True)


def info_box(text: str, kind: str = "info") -> None:
    """Encadré informatif (info / warning / success / danger)."""
    st.markdown(f'<div class="info-box {kind}">{text}</div>', unsafe_allow_html=True)


def panel_header(title: str, subtitle: str = "") -> None:
    """Titre interne d'un st.container(border=True)."""
    sub = f'<p class="panel-sub">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f'<p class="panel-title">{title}</p>{sub}',
        unsafe_allow_html=True,
    )


def plot_header(title: str, subtitle: str = "") -> None:
    """En-tête au-dessus d'un graphique."""
    sub = f'<p class="plot-card-sub">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f'<p class="plot-card-title">{title}</p>{sub}',
        unsafe_allow_html=True,
    )


def badge(text: str, kind: str = "default") -> str:
    """Badge HTML."""
    cls = {"teal": "badge badge--teal", "gold": "badge badge--gold"}.get(
        kind, "badge"
    )
    return f'<span class="{cls}">{text}</span>'


def journey_strip_html() -> str:
    """Bandeau méthodologie 4 étapes."""
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


def footer() -> None:
    """Pied de page."""
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
