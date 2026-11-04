import numpy as np
import matplotlib.pyplot as plt
import time
plt.ion()
xdata = []
y1data = []
y2data = []
buffer_size = 200
t = 0
fig, ax = plt.subplots(figsize=(8, 4))

# Creiamo le due linee inizialmente vuote
line1, = ax.plot([], [], label="sin")
line2, = ax.plot([], [], label="cos")

# Impostiamo i limiti degli assi
ax.set_xlim(0, 200)
ax.set_ylim(-1.5, 1.5)

# Aggiungiamo titolo e legenda
ax.legend()
ax.set_title("Streaming dati sintetici - buffer 200 punti")
while True:

    # Aggiungiamo il nuovo valore temporale
    xdata.append(t)

    # Generiamo il nuovo punto del seno
    y1data.append(np.sin(t / 10))

    # Generiamo il nuovo punto del coseno
    y2data.append(np.cos(t / 10))

    # Incrementiamo il tempo
    t += 1
    # Controlliamo se abbiamo superato il limite
    if len(xdata) > buffer_size:
        # Manteniamo soltanto gli ultimi 200 punti
        xdata = xdata[-buffer_size:]
        y1data = y1data[-buffer_size:]
        y2data = y2data[-buffer_size:]
    line1.set_data(xdata, y1data)
    line2.set_data(xdata, y2data)
    ax.set_xlim(min(xdata), max(xdata) if max(xdata) > buffer_size else buffer_size)
    plt.pause(0.01)

