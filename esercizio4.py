
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CREAZIONE DEL DATASET

# Numero totale di punti
n = 3_000_000

# Genera 3 milioni di valori equidistanti tra 0 e 1000
x = np.linspace(0, 1000, n)

# Crea un andamento sinusoidale e aggiunge rumore casuale
y = np.sin(x / 20) + np.random.normal(0, 0.3, size=n)

# Costruisce il DataFrame con le colonne x e y
df = pd.DataFrame({
    "x": x,
    "y": y
})

# SAMPLING CASUALE

# Estrae casualmente 20.000 righe dal DataFrame
sample = df.sample(n=20000, random_state=1)

# CALCOLO DELLA MEDIA MOBILE

# Calcola la media mobile utilizzando finestre di 5000 valori
df["y_mean"] = df["y"].rolling(5000).mean()

# RIDUZIONE DEL DATASET

# Seleziona una riga ogni 5000, mantenendo tutte le colonne
df_down = df.iloc[::5000, :]

# CREAZIONE DEI DUE GRAFICI

# Crea una figura con 1 riga e 2 colonne
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# PRIMO GRAFICO: PUNTI SINGOLI

# Rappresenta i 20.000 punti del campione casuale
axes[0].scatter(
    sample["x"],
    sample["y"],
    s=2,
    alpha=0.5,
    label="Punti singoli"
)

# Imposta titolo ed etichette degli assi
axes[0].set_title("Punti singoli (sample 20k)")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")

# Mostra la legenda
axes[0].legend()

# SECONDO GRAFICO: MEDIA MOBILE

# Rappresenta la media mobile con una linea rossa
axes[1].plot(
    df_down["x"],
    df_down["y_mean"],
    color="red",
    linewidth=2,
    label="Media mobile"
)

# Imposta titolo ed etichette degli assi
axes[1].set_title("Media mobile (5000 punti)")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y_mean")

# Mostra la legenda
axes[1].legend()

# Aggiunge un titolo generale alla figura
plt.suptitle("Confronto: punti singoli vs media mobile")

# Sistema gli spazi tra i grafici
plt.tight_layout()

# Salva la figura in formato PNG con alta risoluzione
plt.savefig("esercizio4.png", dpi=300)

# Mostra la figura
plt.show()
