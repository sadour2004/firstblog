# ML Academy Library

Bibliothèque interactive de Machine Learning construite avec **Streamlit**.
Présente de façon pédagogique les algorithmes étudiés en semestre :

- **KNN** — K-Nearest Neighbors
- **Decision Tree** — Arbre de décision
- **SVM** — Support Vector Machine
- **PCA** — Analyse en Composantes Principales
- **LDA** — Analyse Discriminante Linéaire

Le site propose pour chaque algorithme : introduction, formules, principe logique,
exemple mathématique, code Scikit-Learn, démonstration interactive et visualisations.

## Structure

```
ML_Library/
├── app.py                  # Page d'accueil premium
├── requirements.txt
├── README.md
├── pages/
│   ├── 1_Accueil.py
│   ├── 2_KNN.py
│   ├── 3_Decision_Tree.py
│   ├── 4_SVM.py
│   ├── 5_PCA.py
│   ├── 6_LDA.py
│   └── 7_Comparaison.py
├── utils/
│   ├── style.py            # CSS global + composants HTML
│   ├── data_loader.py
│   ├── model_utils.py
│   └── plots.py
└── assets/
    └── images/
```

## Installation

```bash
cd ML_Library
python -m venv .venv
source .venv/bin/activate   # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

## Lancement

**Important :** lancez l'application depuis le dossier `ML_Library` :

```bash
cd ML_Library
streamlit run app.py
```

L'application s'ouvre dans le navigateur (généralement http://localhost:8501).

### Pages disponibles (menu latéral)

1. **ML Academy Library** — page d'accueil premium
2. **Introduction ML** — fondamentaux du Machine Learning
3. **KNN** · **Decision Tree** · **SVM** · **PCA** · **LDA**
4. **Comparaison** — synthèse des performances

## Fonctionnalités

- Design premium (glassmorphism, gradients, cards, sidebar stylée)
- Explications pédagogiques et formules
- Démos interactives (sliders, choix de paramètres)
- Dataset Iris (classification & réduction de dimension)
- Métriques : accuracy, precision, recall, F1, matrice de confusion
- Graphiques interactifs Plotly
- Page de comparaison des performances

## Stack

| Bibliothèque   | Rôle                          |
|----------------|-------------------------------|
| streamlit      | Interface web interactive     |
| pandas         | Manipulation de données       |
| numpy          | Calcul numérique              |
| scikit-learn   | Modèles Machine Learning      |
| matplotlib     | Visualisations (arbres, etc.) |
| plotly         | Graphiques interactifs        |

## Auteur

Projet académique — ML Academy Library
