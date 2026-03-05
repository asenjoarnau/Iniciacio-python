import argparse
from player import list_songs, add_song, play_song, create_playlist, add_to_playlist, list_playlists, play_playlist


def interactive():
    while True:
        print("\nMini-Spotify — Menú")
        print("1) Listar canciones")
        print("2) Añadir canción")
        print("3) Reproducir canción")
        print("4) Crear playlist")
        print("5) Añadir a playlist")
        print("6) Listar playlists")
        print("7) Reproducir playlist")
        print("0) Salir")
        try:
            opt = input("Elige opción: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSaliendo...")
            break
        if opt == '1':
            songs = list_songs()
            if not songs:
                print("No hay canciones.")
            for s in songs:
                print(f"{s['id']}. {s['title']} — {s['artist']} ({s['duration']}s)")
        elif opt == '2':
            title = input("Título: ").strip()
            artist = input("Artista: ").strip()
            duration = input("Duración en segundos (ej: 5): ").strip()
            try:
                duration = int(duration)
            except ValueError:
                duration = 5
            song = add_song(title, artist, duration)
            print(f"Añadida: {song['id']}. {song['title']}")
        elif opt == '3':
            sid = input("ID canción: ").strip()
            try:
                sid = int(sid)
            except ValueError:
                print("ID inválido")
                continue
            play_song(sid)
        elif opt == '4':
            name = input("Nombre playlist: ").strip()
            ok = create_playlist(name)
            print("Creada." if ok else "Ya existe.")
        elif opt == '5':
            name = input("Nombre playlist: ").strip()
            sid = input("ID canción: ").strip()
            try:
                sid = int(sid)
            except ValueError:
                print("ID inválido")
                continue
            ok = add_to_playlist(name, sid)
            print("Añadida." if ok else "Error (playlist o canción no encontrada)")
        elif opt == '6':
            pls = list_playlists()
            if not pls:
                print("No hay playlists.")
            for name, ids in pls.items():
                print(f"{name}: {ids}")
        elif opt == '7':
            name = input("Nombre playlist: ").strip()
            play_playlist(name)
        elif opt == '0':
            print("Adiós")
            break
        else:
            print("Opción inválida")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mini-Spotify educativo')
    parser.add_argument('--demo', action='store_true', help='Ejecuta una demo rápida')
    args = parser.parse_args()
    if args.demo:
        print('Demo: añadir dos canciones y reproducir la primera durante 3s')
        # Añadir canciones si no existen
        songs = list_songs()
        if not songs:
            add_song('Canción de ejemplo', 'Alumno', 5)
            add_song('Segunda canción', 'Alumno', 4)
            songs = list_songs()
        for s in songs:
            print(f"{s['id']}. {s['title']} — {s['artist']} ({s['duration']}s)")
        first = songs[0]['id']
        play_song(first, max_seconds=3)
    else:
        interactive()
