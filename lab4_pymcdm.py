"""
Lab 4 – Wprowadzenie do biblioteki pymcdm
Autor: (Kacper Gatkowski)
"""

import numpy as np
import pandas as pd

# Metody decyzyjne
from pymcdm.methods import TOPSIS, SPOTIS


# =========================
# 1. Dane decyzyjne
# =========================

# Alternatywy (np. warianty inwestycyjne)
alternatives = ['A1', 'A2', 'A3', 'A4']

# Kryteria:
# C1 – koszt (min)
# C2 – zysk (max)
# C3 – ryzyko (min)
# C4 – czas realizacji (min)

decision_matrix = np.array([
    [50000, 8000, 7, 12],
    [60000, 9000, 6, 10],
    [55000, 8500, 5, 11],
    [52000, 8200, 6, 9]
])

# Wagi kryteriów (suma = 1)
weights = np.array([0.35, 0.30, 0.20, 0.15])

# Typy kryteriów: 1 = max, -1 = min
criteria_types = np.array([-1, 1, -1, -1])


# =========================
# 2. Metoda TOPSIS
# =========================

topsis = TOPSIS()
topsis_scores = topsis(decision_matrix, weights, criteria_types)


# =========================
# 3. Metoda SPOTIS
# =========================

# Zakresy kryteriów (min, max) – wymagane przez SPOTIS
bounds = np.array([
    [45000, 65000],  # koszt
    [7500, 9500],    # zysk
    [4, 8],          # ryzyko
    [8, 14]          # czas
])

spotis = SPOTIS(bounds)
spotis_scores = spotis(decision_matrix, weights, criteria_types)

# =========================
# 4. Wyniki i ranking
# =========================

results = pd.DataFrame({
    'Alternatywa': alternatives,
    'TOPSIS': topsis_scores,
    'SPOTIS': spotis_scores
})

# Rankingi
results['Ranking_TOPSIS'] = results['TOPSIS'].rank(ascending=False)
results['Ranking_SPOTIS'] = results['SPOTIS'].rank(ascending=True)

print("\nWyniki analiz MCDM:\n")
print(results)

# =========================
# 6. Wnioski (konsola)
# =========================

best_topsis = results.loc[results['TOPSIS'].idxmax(), 'Alternatywa']
best_spotis = results.loc[results['SPOTIS'].idxmin(), 'Alternatywa']

print("\nNajlepsza alternatywa wg TOPSIS:", best_topsis)
print("Najlepsza alternatywa wg SPOTIS:", best_spotis)
