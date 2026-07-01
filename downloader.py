import yt_dlp
import sys
import re
import os


def mostra_benvenuto():
    print("=" * 60)
    print("🎵 BENVENUTO NEL TUO YOUTUBE DOWNLOADER! 🎵")
    print("Puoi scaricare singoli video o intere playlist.")
    print("I formati supportati sono: MP3, FLAC e MP4.")
    print("=" * 60 + "\n")


def valida_url_youtube(url):
    """Verifica se l'URL è un link YouTube valido."""
    youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie|m\.youtube)\.(com|be)/'
    return re.match(youtube_regex, url) is not None


def ottieni_opzioni_formato(scelta_formato):
    """Restituisce il dizionario di configurazione di yt-dlp in base al formato."""

    # Configurazione di base per il nome del file in output
    # playlist_index serve per numerare i video nelle playlist
    outtmpl = '%(playlist_index)s - %(title)s.%(ext)s'

    if scelta_formato == 'mp3':
        return {
            'format': 'bestaudio/best',
            'writethumbnail': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',  # Qualità audio a 192kbps (puoi alzarla a 320)
            },
            {
                'key': 'EmbedThumbnail',
            }
        ],
            'outtmpl': outtmpl,
            'quiet': False,
            'no_warnings': False,
        }
    elif scelta_formato == 'flac':
        return {
            'format': 'bestaudio/best',
            'writethumbnail': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'flac',
            },
            {
                'key': 'EmbedThumbnail',
            }
        ],
            'outtmpl': outtmpl,
            'quiet': False,
            'no_warnings': False,
        }
    elif scelta_formato == 'mp4':
        return {
            # Scarica il miglior video e il miglior audio e li unisce
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'writethumbnail': True,
            'postprocessors': [{
                'key': 'EmbedThumbnail',
            }],
            'outtmpl': outtmpl,
            'quiet': False,
            'no_warnings': False,
        }
    else:
        return None


def main():
    mostra_benvenuto()

    # 1. Chiedi il link all'utente
    url = input("Incolla qui il link del video o della playlist di YouTube:\n> ").strip()

    if not url:
        print("❌ Errore: Non hai inserito nessun link!")
        sys.exit(1)

    # Valida che sia un URL YouTube
    if not valida_url_youtube(url):
        print("❌ Errore: L'URL non sembra essere un link YouTube valido!")
        print("   Verifica di aver incollato correttamente il link.")
        sys.exit(1)

    # 2. Chiedi il formato
    print("\nIn quale formato vuoi scaricare?")
    print("- mp3  (Solo audio, formato standard)")
    print("- flac (Solo audio, alta qualità lossless)")
    print("- mp4  (Video e audio uniti)")

    scelta = input("\nScrivi il formato scelto (mp3, flac, mp4): ").strip().lower()

    # 3. Ottieni la configurazione corretta
    ydl_opts = ottieni_opzioni_formato(scelta)

    if not ydl_opts:
        print("❌ Errore: Formato non valido!")
        print("   Riavvia lo script e scegli tra: mp3, flac, mp4")
        sys.exit(1)

    print(f"\n⏳ Inizio il download in formato {scelta.upper()}...")
    print(f"   I file verranno salvati nella cartella: {os.getcwd()}")
    print("   (Se hai inserito una playlist grande, potrebbe volerci del tempo!)\n")

    # 4. Avvia il download
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Download completato con successo!")
    except yt_dlp.utils.DownloadError as e:
        print(f"\n❌ Errore di download: {e}")
        print("   Verifica che il link sia corretto e il video/playlist sia disponibile.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Si è verificato un errore inaspettato: {type(e).__name__}")
        print(f"   Dettagli: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()