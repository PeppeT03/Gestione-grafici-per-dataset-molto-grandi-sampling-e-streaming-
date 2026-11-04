
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Attiva la modalità interattiva di Matplotlib
plt.ion()

# Creazione della figura e dell'asse principale
fig, ax = plt.subplots(figsize=(8, 4))

# Lascia spazio nella parte inferiore per lo slider
fig.subplots_adjust(bottom=0.25)

# Liste che conterranno i dati
xdata = []
y1data = []
y2data = []

# Creazione delle due linee inizialmente vuote
line1, = ax.plot([], [], label="sin")
line2, = ax.plot([], [], label="cos")

# Impostazione dell'asse verticale
ax.set_ylim(-1.5, 1.5)

# Legenda e titolo
ax.legend()
ax.set_title("Streaming con buffer interattivo")

# Creazione dello spazio dedicato allo slider
slider_ax = fig.add_axes([0.2, 0.08, 0.65, 0.03])

# Creazione dello slider
buffer_slider = Slider(
    slider_ax,
    "Buffer",
    valmin=50,    # Valore minimo
    valmax=1000,  # Valore massimo
    valinit=200,  # Valore iniziale
    valstep=50    # Incremento di 50
)

# Numero massimo di punti da conservare nelle liste
max_buffer = 1000

# Variabile che rappresenta il tempo
t = 0

# Mostra la finestra senza bloccare il programma
plt.show(block=False)

# Ciclo che genera e visualizza i dati in tempo reale
# Si interrompe automaticamente quando chiudiamo la finestra
while plt.fignum_exists(fig.number):

    # Aggiunta di un nuovo punto
    xdata.append(t)
    y1data.append(np.sin(t / 10))
    y2data.append(np.cos(t / 10))

    # Conserva soltanto gli ultimi 1000 punti
    if len(xdata) > max_buffer:
        xdata = xdata[-max_buffer:]
        y1data = y1data[-max_buffer:]
        y2data = y2data[-max_buffer:]

    # Legge il valore attualmente selezionato nello slider
    buffer_size = int(buffer_slider.val)

    # Aggiorna le due linee mostrando solo gli ultimi punti selezionati
    line1.set_data(xdata[-buffer_size:], y1data[-buffer_size:])
    line2.set_data(xdata[-buffer_size:], y2data[-buffer_size:])

    # Aggiorna l'asse X in base al buffer selezionato
    if len(xdata) < buffer_size:
        ax.set_xlim(0, buffer_size)
    else:
        ax.set_xlim(xdata[-buffer_size], xdata[-1])

    # Aggiorna materialmente la finestra del grafico
    plt.pause(0.01)

    # Incrementa il tempo
    t += 1
