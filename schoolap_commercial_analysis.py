# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 23:53:44 2026


@author: kienoub
"""
# ================================================
# Schoolap-Inspired Commercial Dashboard
# EdTech Data Analysis in West Africa
# Author: Bezo Franck Darel Salomon Kienou
# Country Commercial Director - Schoolap
# Université Thomas Sankara - Applied Mathematics
# ================================================
# NOTE: All data is simulated and fictional.
# It does not represent real Schoolap data.
# Created for educational and portfolio purposes.
# ================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np

# ── 1. DATASET "MENSUEL PAR PAYS" ──────────────────
# Revenus mensuels simulés en FCFA (millions)
# 4 pays où Schoolap opère : BF, CI, BN, ML
# 12 mois de janvier à décembre 2025

mois = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun',
        'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']

# Chaque liste = revenus mensuels en millions FCFA
revenus = {
    'Mois': mois,
    'Burkina Faso': [12.5, 13.2, 14.8, 15.1, 16.3,
                     17.2, 15.8, 14.9, 18.2, 19.5,
                     21.3, 23.7],
    'Cote Ivoire':  [18.3, 19.1, 21.5, 22.8, 24.1,
                     25.6, 23.4, 22.1, 26.8, 28.3,
                     30.5, 33.2],
    'Benin':        [8.2, 8.7, 9.5, 10.1, 10.8,
                     11.4, 10.6, 9.8, 12.3, 13.1,
                     14.2, 15.8],
    'Mali':         [9.8, 10.3, 11.2, 11.9, 12.5,
                     13.1, 12.2, 11.5, 13.8, 14.6,
                     15.9, 17.4]
}

df = pd.DataFrame(revenus)

# ── 2. DATASET TYPES DE CLIENTS ──────────────────
# Répartition du portefeuille clients par catégorie
types_clients = {
    'Type': ['Écoles Primaires', 'Lycées',
             'Universités', 'Admin. Éducatives',
             'Centres de Formation'],
    'Nombre': [145, 98, 42, 28, 67]
}
df_clients = pd.DataFrame(types_clients)

# ── 3. AFFICHAGE DES DONNÉES ──────────────────────
pays = ['Burkina Faso', 'Cote Ivoire', 'Benin', 'Mali']

print("=" * 60)
print("SCHOOLAP — EDTECH COMMERCIAL PERFORMANCE 2025")
print("West Africa | Simulated Data")
print("=" * 60)
print(df.to_string(index=False))
print()

# ── 4. CALCUL DES KPIs ───────────────────────────
print("=" * 60)
print("KEY PERFORMANCE INDICATORS (KPIs) — 2025")
print("=" * 60)

total_annuel = {}
for p in pays:
    total = df[p].sum()
    total_annuel[p] = total
    croissance = ((df[p].iloc[-1] - df[p].iloc[0])
                  / df[p].iloc[0] * 100)
    moy = df[p].mean()
    print(f"\n{p}:")
    print(f"  Revenu total 2025    : "
          f"{total:.1f}M FCFA")
    print(f"  Revenu moyen/mois   : "
          f"{moy:.1f}M FCFA")
    print(f"  Croissance Jan→Déc  : "
          f"+{croissance:.1f}%")

print()
print(f"Revenu total 4 pays  : "
      f"{sum(total_annuel.values()):.1f}M FCFA")
print()

# ── 5. GRAPHIQUE 1 — ÉVOLUTION REVENUS ───────────
# Ce graphique montre la tendance mensuelle
# pour chaque pays sur 12 mois
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(
    'Schoolap — EdTech Commercial Performance 2025\n'
    'West Africa Regional Analysis',
    fontsize=15, fontweight='bold', y=1.02)

colors = ['#E63946', '#457B9D', '#2A9D8F', '#E9C46A']

# Graphique 1 — Courbes d'évolution
ax1 = axes[0, 0]
for i, p in enumerate(pays):
    ax1.plot(df['Mois'], df[p],
             marker='o', linewidth=2.5,
             label=p, color=colors[i])
ax1.set_title('Monthly Revenue Evolution (2025)',
              fontweight='bold')
ax1.set_xlabel('Month')
ax1.set_ylabel('Revenue (Millions FCFA)')
ax1.legend(fontsize=8)
ax1.tick_params(axis='x', rotation=45)
sns.despine(ax=ax1)

# Graphique 2 — Barres comparaison annuelle
ax2 = axes[0, 1]
totaux = [total_annuel[p] for p in pays]
bars = ax2.bar(pays, totaux,
               color=colors,
               edgecolor='white',
               linewidth=1.5)
for bar, val in zip(bars, totaux):
    ax2.text(
        bar.get_x() + bar.get_width() / 2.,
        bar.get_height() + 0.5,
        f'{val:.0f}M',
        ha='center', va='bottom',
        fontweight='bold', fontsize=9)
ax2.set_title('Total Annual Revenue by Country',
              fontweight='bold')
ax2.set_ylabel('Revenue (Millions FCFA)')
ax2.tick_params(axis='x', rotation=15)
sns.despine(ax=ax2)

# Graphique 3 — Camembert types de clients
ax3 = axes[1, 0]
colors_pie = ['#264653', '#2A9D8F', '#E9C46A',
              '#F4A261', '#E63946']
wedges, texts, autotexts = ax3.pie(
    df_clients['Nombre'],
    labels=df_clients['Type'],
    colors=colors_pie,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85)
for text in texts:
    text.set_fontsize(8)
ax3.set_title('Client Portfolio Distribution',
              fontweight='bold')

# Graphique 4 — Heatmap mensuelle
ax4 = axes[1, 1]
df_heat = df.set_index('Mois')[pays].T
sns.heatmap(df_heat,
            annot=True, fmt='.0f',
            cmap='YlOrRd',
            linewidths=0.5,
            ax=ax4,
            cbar_kws={
                'label': 'Revenue (M FCFA)'
            })
ax4.set_title('Revenue Heatmap by Country & Month',
              fontweight='bold')
ax4.set_xlabel('Month')
ax4.set_ylabel('Country')

plt.tight_layout()
plt.savefig('commercial_dashboard.png',
            dpi=150, bbox_inches='tight')
plt.show()
print("Dashboard genere OK ✅")

# ── 6. GRAPHIQUE 5 — KPIs VISUELS ────────────────
fig2, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')

# Calcul des KPIs finaux
croissances = []
for p in pays:
    c = ((df[p].iloc[-1] - df[p].iloc[0])
         / df[p].iloc[0] * 100)
    croissances.append(c)

# Tableau récapitulatif des KPIs
kpi_data = []
for i, p in enumerate(pays):
    kpi_data.append([
        p,
        f"{total_annuel[p]:.0f}M FCFA",
        f"{df[p].mean():.1f}M FCFA",
        f"+{croissances[i]:.1f}%"
    ])

table = ax.table(
    cellText=kpi_data,
    colLabels=['Country', 'Total Revenue',
               'Avg/Month', 'Growth'],
    cellLoc='center',
    loc='center',
    bbox=[0, 0, 1, 1])

table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1, 2)

# Couleurs du tableau
for j in range(4):
    table[0, j].set_facecolor('#264653')
    table[0, j].set_text_props(color='white',
                                fontweight='bold')
for i in range(1, 5):
    for j in range(4):
        if i % 2 == 0:
            table[i, j].set_facecolor('#f0f0f0')

ax.set_title(
    'KPI Summary — Schoolap West Africa 2025\n'
    'Simulated Data for Portfolio Purposes',
    fontsize=13, fontweight='bold', pad=20)

plt.savefig('kpi_summary.png',
            dpi=150, bbox_inches='tight')
plt.show()
print("KPI Summary genere OK ✅")

print()
print("=" * 60)
print("ANALYSE COMPLETE — 5 visualisations generees ✅")
print("=" * 60)