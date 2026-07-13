"""
Chargement et préparation des datasets pour ML Academy Library.
"""

from __future__ import annotations

import pandas as pd
from sklearn.datasets import load_iris, make_classification, make_blobs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_iris_data(as_dataframe: bool = True):
    """
    Charge le dataset Iris classique.

    Returns
    -------
    Si as_dataframe=True :
        X (DataFrame), y (Series), feature_names, target_names, df (DataFrame complet)
    Sinon :
        X (ndarray), y (ndarray), feature_names, target_names
    """
    iris = load_iris()
    feature_names = list(iris.feature_names)
    target_names = list(iris.target_names)

    if as_dataframe:
        X = pd.DataFrame(iris.data, columns=feature_names)
        y = pd.Series(iris.target, name="target")
        df = X.copy()
        df["target"] = y
        df["species"] = df["target"].map(dict(enumerate(target_names)))
        return X, y, feature_names, target_names, df

    return iris.data, iris.target, feature_names, target_names


def split_data(X, y, test_size: float = 0.3, random_state: int = 42, stratify: bool = True):
    """Découpe train/test, avec stratification optionnelle."""
    strat = y if stratify else None
    return train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )


def standardize(X_train, X_test=None):
    """
    Standardise les features (moyenne 0, écart-type 1).
    Fit uniquement sur le train pour éviter le data leakage.
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    if X_test is None:
        return X_train_scaled, scaler
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler


def get_iris_overview() -> pd.DataFrame:
    """Retourne un aperçu tabulaire du dataset Iris."""
    _, _, _, _, df = load_iris_data(as_dataframe=True)
    return df


def make_2d_classification(n_samples: int = 200, random_state: int = 42):
    """Génère un dataset 2D synthétique pour visualisations SVM / frontières."""
    X, y = make_classification(
        n_samples=n_samples,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        n_clusters_per_class=1,
        n_classes=2,
        class_sep=1.2,
        random_state=random_state,
    )
    return X, y


def make_2d_blobs(n_samples: int = 200, centers: int = 3, random_state: int = 42):
    """Génère des blobs 2D pour illustrations pédagogiques."""
    X, y = make_blobs(
        n_samples=n_samples,
        centers=centers,
        n_features=2,
        cluster_std=1.1,
        random_state=random_state,
    )
    return X, y
