"""
Visualisations Plotly / Matplotlib pour ML Academy Library.
"""

from __future__ import annotations

from typing import Optional, Sequence

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.inspection import DecisionBoundaryDisplay
import matplotlib.pyplot as plt


# Palette cohérente avec le thème sombre premium
PALETTE = ["#38bdf8", "#22d3ee", "#34d399", "#fbbf24", "#f472b6", "#a78bfa"]
PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(15, 23, 42, 0.35)",
    font=dict(family="Outfit, sans-serif", color="#e2e8f0"),
    margin=dict(l=40, r=30, t=50, b=40),
)


def _apply_layout(fig: go.Figure, title: str = "") -> go.Figure:
    fig.update_layout(title=title, **PLOTLY_LAYOUT)
    fig.update_xaxes(gridcolor="rgba(148,163,184,0.15)", zeroline=False)
    fig.update_yaxes(gridcolor="rgba(148,163,184,0.15)", zeroline=False)
    return fig


def plot_confusion_matrix(
    cm: np.ndarray,
    labels: Sequence[str],
    title: str = "Matrice de confusion",
) -> go.Figure:
    """Heatmap interactive de la matrice de confusion."""
    fig = px.imshow(
        cm,
        text_auto=True,
        x=list(labels),
        y=list(labels),
        color_continuous_scale=["#0b1220", "#0284c7", "#22d3ee"],
        aspect="auto",
    )
    fig.update_layout(
        xaxis_title="Prédiction",
        yaxis_title="Vérité terrain",
        coloraxis_showscale=False,
    )
    return _apply_layout(fig, title)


def plot_iris_scatter(
    df: pd.DataFrame,
    x: str = "sepal length (cm)",
    y: str = "sepal width (cm)",
    color: str = "species",
    title: str = "Dataset Iris",
) -> go.Figure:
    """Nuage de points Iris interactif."""
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        color_discrete_sequence=PALETTE,
        opacity=0.85,
        hover_data=df.columns.tolist(),
    )
    fig.update_traces(marker=dict(size=10, line=dict(width=0.5, color="#0b1220")))
    return _apply_layout(fig, title)


def plot_pca_2d(
    X_pca: np.ndarray,
    y,
    target_names: Sequence[str],
    explained_variance: Optional[Sequence[float]] = None,
    title: str = "Projection PCA (2 composantes)",
) -> go.Figure:
    """Projection 2D après PCA."""
    df = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
    df["Classe"] = [target_names[i] for i in y]
    fig = px.scatter(
        df,
        x="PC1",
        y="PC2",
        color="Classe",
        color_discrete_sequence=PALETTE,
        opacity=0.9,
    )
    fig.update_traces(marker=dict(size=11))
    if explained_variance is not None and len(explained_variance) >= 2:
        fig.update_xaxes(title=f"PC1 ({explained_variance[0]*100:.1f}%)")
        fig.update_yaxes(title=f"PC2 ({explained_variance[1]*100:.1f}%)")
    return _apply_layout(fig, title)


def plot_explained_variance(
    ratios: Sequence[float], title: str = "Variance expliquée"
) -> go.Figure:
    """Barres + cumul de la variance expliquée."""
    ratios = list(ratios)
    cumulative = np.cumsum(ratios)
    components = [f"PC{i+1}" for i in range(len(ratios))]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(
            x=components,
            y=ratios,
            name="Variance individuelle",
            marker_color="#38bdf8",
            opacity=0.85,
        ),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=components,
            y=cumulative,
            name="Variance cumulée",
            mode="lines+markers",
            line=dict(color="#34d399", width=3),
            marker=dict(size=9),
        ),
        secondary_y=True,
    )
    fig.update_yaxes(title_text="Ratio", secondary_y=False, range=[0, 1])
    fig.update_yaxes(title_text="Cumul", secondary_y=True, range=[0, 1.05])
    return _apply_layout(fig, title)


def plot_lda_2d(
    X_lda: np.ndarray,
    y,
    target_names: Sequence[str],
    title: str = "Projection LDA",
) -> go.Figure:
    """Projection LDA (1D ou 2D)."""
    n_comp = X_lda.shape[1]
    if n_comp == 1:
        df = pd.DataFrame({"LD1": X_lda[:, 0], "index": np.arange(len(X_lda))})
        df["Classe"] = [target_names[i] for i in y]
        fig = px.scatter(
            df,
            x="LD1",
            y="index",
            color="Classe",
            color_discrete_sequence=PALETTE,
        )
    else:
        df = pd.DataFrame(X_lda[:, :2], columns=["LD1", "LD2"])
        df["Classe"] = [target_names[i] for i in y]
        fig = px.scatter(
            df,
            x="LD1",
            y="LD2",
            color="Classe",
            color_discrete_sequence=PALETTE,
        )
    fig.update_traces(marker=dict(size=11))
    return _apply_layout(fig, title)


def plot_metrics_comparison(
    df: pd.DataFrame, title: str = "Comparaison des performances"
) -> go.Figure:
    """
    Graphique en barres groupées pour comparer Accuracy / Precision / Recall / F1.
    Attend des colonnes : Algorithme, Accuracy, Precision, Recall, F1-Score
    """
    melted = df.melt(
        id_vars="Algorithme",
        value_vars=["Accuracy", "Precision", "Recall", "F1-Score"],
        var_name="Métrique",
        value_name="Score",
    )
    fig = px.bar(
        melted,
        x="Algorithme",
        y="Score",
        color="Métrique",
        barmode="group",
        color_discrete_sequence=PALETTE,
        text_auto=".2f",
    )
    fig.update_traces(textposition="outside")
    fig.update_yaxes(range=[0, 1.15])
    return _apply_layout(fig, title)


def plot_decision_boundary_2d(
    model,
    X: np.ndarray,
    y: np.ndarray,
    title: str = "Frontière de décision",
    feature_names: Sequence[str] = ("Feature 1", "Feature 2"),
):
    """
    Frontière de décision 2D via Matplotlib (compatible Streamlit).
    Retourne une figure matplotlib.
    """
    fig, ax = plt.subplots(figsize=(7, 5), facecolor="#0b1220")
    ax.set_facecolor("#0f172a")

    DecisionBoundaryDisplay.from_estimator(
        model,
        X,
        response_method="predict",
        cmap="cool",
        alpha=0.35,
        ax=ax,
    )
    scatter = ax.scatter(
        X[:, 0],
        X[:, 1],
        c=y,
        cmap="cool",
        edgecolors="white",
        linewidths=0.6,
        s=45,
    )
    ax.set_xlabel(feature_names[0], color="#94a3b8")
    ax.set_ylabel(feature_names[1], color="#94a3b8")
    ax.set_title(title, color="#f8fafc", fontsize=13, pad=12)
    ax.tick_params(colors="#94a3b8")
    for spine in ax.spines.values():
        spine.set_color("#334155")
    fig.colorbar(scatter, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    return fig


def plot_feature_importance_tree(
    model, feature_names: Sequence[str], title: str = "Importance des features"
) -> go.Figure:
    """Importance des variables pour un arbre de décision."""
    importances = model.feature_importances_
    df = pd.DataFrame({"Feature": feature_names, "Importance": importances})
    df = df.sort_values("Importance", ascending=True)
    fig = px.bar(
        df,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        color_continuous_scale=["#0ea5e9", "#22d3ee"],
    )
    fig.update_layout(coloraxis_showscale=False)
    return _apply_layout(fig, title)


def plot_tree_matplotlib(model, feature_names, class_names):
    """Visualisation de l'arbre de décision (matplotlib)."""
    from sklearn.tree import plot_tree

    fig, ax = plt.subplots(figsize=(14, 8), facecolor="#0b1220")
    ax.set_facecolor("#0b1220")
    plot_tree(
        model,
        feature_names=feature_names,
        class_names=list(class_names),
        filled=True,
        rounded=True,
        fontsize=8,
        ax=ax,
        impurity=True,
    )
    ax.set_title("Arbre de décision", color="#f8fafc", fontsize=14, pad=12)
    fig.tight_layout()
    return fig
