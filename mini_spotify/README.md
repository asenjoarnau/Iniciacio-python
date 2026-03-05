Mini-Spotify — Proyecto sencillo

Objetivo
- Crear un mini-reproductor educativo en Python, pensado para alumnos de 1r de bachillerato.

Archivos
- `main.py`: interfaz simple (interactiva) y opción `--demo`.
- `player.py`: funciones para gestionar canciones y playlists.
- `songs.json`: base de datos sencilla en JSON.

Uso rápido
Ejecuta la demo:

```bash
python3 mini_spotify/main.py --demo
```

O inicia el menú interactivo:

```bash
python3 mini_spotify/main.py
```

Notas
- La reproducción es simulada (imprime segundos y espera con `time.sleep`).
- Ideal para ampliar: integrar archivos de audio reales, GUI con `tkinter`, o una API web.
