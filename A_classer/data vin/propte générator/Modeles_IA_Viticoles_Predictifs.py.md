# 🧪 Modèles IA Prédictifs pour la Viticulture (Exemples Python)

Ce document présente les structures de modèles IA pour répondre aux problématiques de rendement, de maturité et de pression sanitaire.

## 1. Modèle de Prédiction de Rendement (Yield Predictor)
*Algorithme : Random Forest Regressor*
*Données : Vigueur (NDVI), Météo (Pluviométrie, Degrés jours), Historique parcelles.*

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Simulation de données : NDVI (Vigueur), Rainfall (mm), GDD (Growing Degree Days)
data = {
    'ndvi_mean': [0.65, 0.72, 0.58, 0.81, 0.69, 0.75],
    'rainfall_spring': [120, 150, 90, 200, 130, 160],
    'gdd_accumulation': [1200, 1350, 1100, 1450, 1250, 1380],
    'historical_yield_hl_ha': [45, 52, 38, 58, 48, 54] # Target (Cible)
}

df = pd.DataFrame(data)
X = df[['ndvi_mean', 'rainfall_spring', 'gdd_accumulation']]
y = df['historical_yield_hl_ha']

# Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Prediction pour une nouvelle parcelle
new_parcel = [[0.70, 140, 1300]]
predicted_yield = model.predict(new_parcel)
print(f"Rendement prédit : {predicted_yield[0]:.2f} hl/ha")
```

## 2. Modèle de Prédiction de Date de Vendange (Harvest Date)
*Algorithme : Séries Temporelles (Linear Trend / Polynomial)*
*Données : Somme des températures depuis le débourrement.*

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Jours après le 1er Janvier pour la récolte sur 5 ans
years = np.array([2020, 2021, 2022, 2023, 2024]).reshape(-1, 1)
harvest_day_of_year = np.array([255, 258, 248, 245, 242]) # Tendance précoce (changement climatique)

model = LinearRegression()
model.fit(years, harvest_day_of_year)

# Projection 2030
future_year = np.array([[2030]])
projected_day = model.predict(future_year)
print(f"Date de vendange estimée pour 2030 (Jour de l'année) : {int(projected_day[0])}")
```

## 3. Détection de Maladies (Deep Learning Concept)
*Algorithme : Convolutional Neural Network (CNN)*
*Données : Photos de feuilles (Mildiou vs Sain).*

```python
# Note : Nécessite TensorFlow/Keras ou PyTorch
# Ce bloc montre la structure d'un classifieur pour smartphone
"""
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid') # 1 = Mildiou détecté, 0 = Sain
])
"""
```

## Problématiques & Solutions Digitales (Synthèse)

| Problématique | Solution Digitale | Modèle IA Pertinent |
| :--- | :--- | :--- |
| **Gel Printanier** | Stations météo connectées + Alertes SMS | Modèle de prédiction locale (Gradient Boosting) |
| **Stress Hydrique** | Sondes capacitives & Imagerie Thermique | Estimation de l'ETP (Évapotranspiration) |
| **Taille & Main d'œuvre** | Robots de taille autonomes (Vision IA) | Segmentation d'image (YOLOv8) pour le bois |
| **Valorisation Bouteille** | Plateforme Blockchain de traçabilité | Smart Contracts pour authenticité |
| **Optimisation Traitement** | Pulvérisation ciblée (Smart Spraying) | Détection de canopée en temps réel |
