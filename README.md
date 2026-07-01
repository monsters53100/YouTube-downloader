# YouTube Downloader (MP3, FLAC, MP4)

Un potente script in Python che permette di scaricare video singoli o intere playlist (come album musicali) da YouTube. Lo script estrae l'audio o il video nella massima qualità possibile, integra automaticamente le copertine originali dei brani e organizza le playlist numerandole in ordine.

## 🚀 Caratteristiche

- Scarica video singoli o intere playlist/album con un solo link.
- **Formati supportati**:
  - `mp3`: Solo audio (formato standard compresso, qualità consigliata 192kbps).
  - `flac`: Solo audio (alta qualità lossless, non compresso).
  - `mp4`: Video + Audio uniti alla massima risoluzione.
- Download automatico e incorporamento della copertina direttamente nel file finale (tramite i tag ID3 per gli MP3/FLAC e metadati per gli MP4).
- Numerazione automatica delle tracce se si scarica una playlist.

---

## 🛠️ Requisiti e Installazione dei Componenti

Per far funzionare correttamente lo script, è necessario installare sul computer tre componenti fondamentali. Scegli la procedura in base al tuo sistema operativo.

### 🪟 1. Guida per Windows

#### A. Installare Node.js (Richiesto come JavaScript Runtime per YouTube)
1. Scarica l'installer ufficiale dal sito [nodejs.org](https://nodejs.org/) (scegli la versione **LTS**).
2. Avvia l'installazione, clicca sempre su "Avanti" assicurandoti che la spunta **"Add to PATH"** sia attiva.
3. Al termine, apri un nuovo terminale e verifica con:
```bash
node -v
```

#### B. Installare FFmpeg (Richiesto per convertire e unire audio/video)
Apri il Prompt dei Comandi o PowerShell come amministratore e digita:
```bash
winget install -e --id Gyan.FFmpeg
```
Dopo l'installazione, apri un nuovo terminale e verifica con:
```bash
ffmpeg -version
```

In alternativa, scarica l'eseguibile dal sito ufficiale di FFmpeg e aggiungilo manualmente alle Variabili d'Ambiente del sistema.

### 🍏 2. Guida per macOS

#### A. Installare Node.js
Scarica e avvia l'installer `.pkg` per Mac dal sito ufficiale [nodejs.org](https://nodejs.org/) (versione LTS). Verifica poi con:
```bash
node -v
```

#### B. Installare FFmpeg
Il modo più veloce è usare [Homebrew](https://brew.sh/). Apri il Terminale e digita:

```bash
brew install ffmpeg
```
Verifica l'installazione con:
```bash
ffmpeg -version
```

### 🐧 3. Guida per Linux (Ubuntu/Debian e derivati)

Apri il terminale e installa tutti i requisiti con il gestore dei pacchetti:

```bash
# Aggiorna i pacchetti
sudo apt update

# Installa FFmpeg
sudo apt install ffmpeg

# Installa Node.js
sudo apt install nodejs npm
```
Verifica poi con:
```bash
ffmpeg -version
node -v
```

## 📦 Installazione delle Dipendenze Python

Una volta configurato il sistema operativo con i programmi sopra elencati, apri il terminale all'interno della cartella del progetto (o usa il terminale integrato di PyCharm) e installa le librerie Python necessarie eseguendo:

```bash
pip install yt-dlp mutagen
```

A cosa servono?

* `yt-dlp`: Gestisce la connessione con YouTube, l'estrazione dei flussi multimediali e il download.
* `mutagen`: Permette a `yt-dlp` di inserire le immagini di copertina (thumbnail) all'interno dei file musicali scaricati.

## 💻 Come avviare lo script

1. Apri il terminale nella cartella del progetto.
2. Avvia lo script con il comando:

```bash
python downloader.py
```

3. Segui le istruzioni a schermo:
   * Incolla il link del video o della playlist.
   * Scegli il formato digitando `mp3`, `flac` o `mp4`.
   * Il file verrà salvato direttamente nella cartella da cui hai avviato lo script.

## 🔍 Risoluzione dei Problemi

Se durante il download riscontri l'avviso giallo relativo alla mancanza di un JavaScript runtime (`No supported JavaScript runtime could be found`), assicurati di aver installato Node.js e di aver riavviato il terminale o l'IDE (PyCharm) per applicare le modifiche.

Se l'errore persiste, è possibile forzare il percorso di Node.js modificando nel codice la riga del dizionario delle opzioni:

```python
# Esempio su Windows
'js_runtimes': {'node': {'path': 'C:/Program Files/nodejs/node.exe'}},
```