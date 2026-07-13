"""
Entraînement et évaluation des modèles Scikit-Learn.
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def train_knn(
    X_train,
    y_train,
    n_neighbors: int = 5,
    metric: str = "euclidean",
    weights: str = "uniform",
) -> KNeighborsClassifier:
    """Entraîne un classificateur KNN."""
    model = KNeighborsClassifier(
        n_neighbors=n_neighbors, metric=metric, weights=weights
    )
    model.fit(X_train, y_train)
    return model


def train_decision_tree(
    X_train,
    y_train,
    criterion: str = "gini",
    max_depth: Optional[int] = None,
    random_state: int = 42,
) -> DecisionTreeClassifier:
    """Entraîne un arbre de décision."""
    model = DecisionTreeClassifier(
        criterion=criterion,
        max_depth=max_depth,
        random_state=random_state,
    )
    model.fit(X_train, y_train)
    return model


def train_svm(
    X_train,
    y_train,
    kernel: str = "rbf",
    C: float = 1.0,
    gamma: str | float = "scale",
    degree: int = 3,
    random_state: int = 42,
) -> SVC:
    """Entraîne un SVM (SVC)."""
    model = SVC(
        kernel=kernel,
        C=C,
        gamma=gamma,
        degree=degree,
        random_state=random_state,
    )
    model.fit(X_train, y_train)
    return model


def train_pca(X, n_components: int = 2) -> Tuple[PCA, np.ndarray]:
    """Ajuste un PCA et retourne (modèle, données transformées)."""
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)
    return pca, X_pca


def train_lda(
    X_train,
    y_train,
    n_components: Optional[int] = None,
    as_classifier: bool = True,
) -> LinearDiscriminantAnalysis:
    """
    Entraîne un LDA.
    - as_classifier=True : utilise LDA comme classificateur
    - n_components : pour réduction de dimension supervisée
    """
    model = LinearDiscriminantAnalysis(n_components=n_components)
    model.fit(X_train, y_train)
    return model


def evaluate_classifier(
    model, X_test, y_test, target_names: Optional[list] = None
) -> Dict[str, Any]:
    """
    Évalue un classificateur et retourne un dictionnaire de métriques.
    """
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(
        y_test,
        y_pred,
        target_names=target_names,
        output_dict=True,
        zero_division=0,
    )
    report_df = pd.DataFrame(report).transpose()

    return {
        "y_pred": y_pred,
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(
            precision_score(y_test, y_pred, average="weighted", zero_division=0)
        ),
        "recall": float(
            recall_score(y_test, y_pred, average="weighted", zero_division=0)
        ),
        "f1": float(f1_score(y_test, y_pred, average="weighted", zero_division=0)),
        "confusion_matrix": cm,
        "classification_report": report_df,
    }


def compare_classifiers(
    models: Dict[str, Any], X_test, y_test
) -> pd.DataFrame:
    """
    Compare plusieurs classificateurs déjà entraînés.
    Retourne un DataFrame (accuracy, precision, recall, f1).
    """
    rows = []
    for name, model in models.items():
        metrics = evaluate_classifier(model, X_test, y_test)
        rows.append(
            {
                "Algorithme": name,
                "Accuracy": metrics["accuracy"],
                "Precision": metrics["precision"],
                "Recall": metrics["recall"],
                "F1-Score": metrics["f1"],
            }
        )
    return pd.DataFrame(rows).sort_values("Accuracy", ascending=False).reset_index(
        drop=True
    )
