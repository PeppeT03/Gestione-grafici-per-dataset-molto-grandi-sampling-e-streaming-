import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Impostiamo il seme casuale
np.random.seed(42)

# Definiamo il numero di osservazioni
n = 5_000_000
categories = np.random.choice(
    ["A", "B", "C"],
    size=n,
    p=[0.5, 0.3, 0.2]
)
x = np.random.uniform(0, 100, size=n)
y = np.sin(x / 5) + np.random.normal(0, 0.3, size=n) + (categories == "B") * 1.5 + (categories == "C") * 3

df = pd.DataFrame({
    "Valore x" : x,
    "Valore y" : y,
    "Categorie" : categories
})

sample_random = df.sample(n=10000, random_state=1)
sample_random["Categorie"].map({
    "A": "blue",
    "B": "orange",
    "C": "green"
})

sample_stratified = df.groupby(
    "Categorie",
    group_keys=False
).apply(
    lambda gruppo: gruppo.sample(
        n=round(10000 * len(gruppo) / len(df)),
        random_state=1
    ).assign(Categorie=gruppo.name)
)
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
axes[0].scatter(
    sample_random["Valore x"],
    sample_random["Valore y"],
    c=sample_random["Categorie"].map({
        "A": "blue",
        "B": "orange",
        "C": "green"
    }),
    s=2,
    alpha=0.5
)
axes[1].scatter(
    sample_stratified["Valore x"],
    sample_stratified["Valore y"],
    c=sample_stratified["Categorie"].map({
        "A": "blue",
        "B": "orange",
        "C": "green"
    }),
    s=2,
    alpha=0.5
)
axes[0].set_title("Sampling casuale")
axes[1].set_title("Sampling stratificato")
for ax in axes:
    ax.set_xlabel("Valore x")
    ax.set_ylabel("Valore y")
plt.suptitle("Confronto tra sampling casuale e stratificato (5M punti totali)")
plt.tight_layout()
plt.savefig("esercizio1.png", dpi=300, bbox_inches="tight")
plt.show()