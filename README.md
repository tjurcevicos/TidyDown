<p align="center">
  <img src="src/assets/tidy.png" alt="TidyDown" width="200">
</p>


# 🧹 TidyDown™

An advanced, client-side automated file orchestration engine built with Python. TidyDown operates entirely within the isolated environment of your local system, parsing and routing unorganized asset arrays straight from your system directory into structuralized categorical vectors. Focus on zero-network telemetry, high-speed partition execution, and fail-safe duplicate filename avoidance layers.

Developed by **Tomislav Jurčević** (2026).


---

## ⚠️ Intellectual Property & Commercial Licensing

This project is protected under a strict **Non-Commercial License Agreement**. It is **NOT** open-source under the MIT license.

- **✅ Permitted Use**: Free for personal use, students, educators, hobbyists, and non-profit research.
- **❌ Prohibited Use**: Any deployment, modification, redistribution, or inclusion within commercial entities, for-profit businesses, ad-supported sites, or as part of a paid service/extension is strictly prohibited without a valid Commercial License.

### 💼 Commercial Licensing Inquiries
If your organization wishes to deploy TidyDown™ in a commercial environment or use its file-routing core components, you must obtain a separate commercial license from the Author. 

For custom licensing terms, pricing inquiries, or enterprise deployment, please contact the Author directly via email:  
📩 **tjurcevicos@gmail.com**

---

## Architectural Features

- **GUID Telemetry Core**: Dynamic API abstraction utilizing native Windows Registry mapping. It programmatically fetches the absolute directory path of the active host, ensuring language-independent target resolving (e.g., `Downloads`, `Preuzimanja`) without hardcoded string assumptions.
- **Fail-Safe Collision Matrix**: A recursive name-resolution layer. If a naming conflict occurs within the destination partition, the engine isolates the incoming binary array and applies incremental indexation mutations (e.g., `document_1.pdf`) to guarantee absolute data protection.
- **Garbage Isolation Layer**: Built-in exception criteria that dynamically detect and ignore unfinalized browser chunks (`.crdownload`) or transient application memory fragments (`.tmp`), blocking volatile states from cluttering active categories.
- **Channel Partition Matrix**: Multi-channel mapping arrays that decouple multi-media content, instantly driving video files and audio binaries into completely separate, dedicated directories instead of generic data folders.

---

## Categorical Routing Architecture

| Destination Partition | Encrypted File Extension Vectors |
| :--- | :--- |
| **Music_and_Audio** | `.mp3`, `.wav`, `.wma`, `.ogg`, `.flac`, `.m4a`, `.aac`, `.amr`, `.mid`, `.midi` |
| **Videos** | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`, `.webm`, `.vob`, `.mpeg`, `.3gp` |
| **Archives_and_Zip** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.iso`, `.bz2`, `.xz`, `.z`, `.pkg`, `.deb`, `.rpm` |
| **PDF_Documents** | `.pdf` |
| **Text_and_Office** | `.txt`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.csv`, `.odt`, `.rtf` |
| **Images_and_Photos** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`, `.tiff`, `.ico`, `.psd`, `.ai` |
| **Programs_and_Installers** | `.exe`, `.msi`, `.bat`, `.cmd`, `.jar` |
| **Ebooks** | `.epub`, `.mobi`, `.azw`, `.azw3`, `.djvu` |
| **Design_3D_and_CAD** | `.stl`, `.obj`, `.fbx`, `.3ds`, `.dwg`, `.dxf` |
| **Other** | Catch-all fallback directory for unmapped file signatures |

---

## 🛑 ⚠️ Antivirus Flagging (False Positive Warning)

Because **TidyDown™** is compiled into a single-file executable binary (`.exe`) via PyInstaller and operates without an expensive commercial code-signing certificate, certain active telemetry protection suites (such as **Avast**, **AVG**, or **Windows Defender**) will flag the binary as a threat upon initial download.

**This is a 100% False Positive.** The source code is entirely transparent and open for inspection on this repository. No data ever crosses the local host boundary.

### How to whitelist the binary:
1. **Avast / AVG**: Open the Avast dashboard, navigate to *Protection -> Quarantine*, locate `TidyDown.exe`, click the option menu, and select **Restore and add exception**.
2. **Windows Defender**: On the SmartScreen prompt, click *More Info*, and then select **Run Anyway**.
3. **General**: Add the directory containing your compiled `TidyDown.exe` to your antivirus exclusions panel.

---

## Core Operational Mechanics

When the executable trigger initializes within the system context:

1. **Path Mapping**: The system pulls the internal Windows GUID keys to map the absolute location of the primary download directory.
2. **Buffer Sanitization**: Files are scanned locally, and trailing empty bitstrings or formatting artifacts are stripped via text isolation workers.
3. **Vector Sorting**: The binary string compares each file's metadata extension signature against the `PRAVILA_SORTIRANJA` array.
4. **Collision Resolving**: If an matching filename exists in the target destination, the collision matrix calculates a new index path.
5. **Atomic Relocation**: System handles execute an atomic file move (`shutil.move`) to place the binary securely into its new home.

---

## Local Setup & Installation

```bash
# Clone the source environment
git clone https://github.com

# Change path context to root directory
cd tidydown

# Execute binary distribution compiler via uv shell
& "C:\Users\Samuraj\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none\Scripts\pyinstaller.exe" --onefile --name="TidyDown" --icon="TidyDown.ico" sortiranje.py
```

---
---

# 🧹 TidyDown™ (Hrvatski)

Napredan, lokalni sustav za automatiziranu orkestraciju i čišćenje datoteka izrađen u Pythonu. TidyDown radi u potpunosti unutar izoliranog okruženja vašeg lokalnog računala, analizirajući i usmjeravajući neorganizirane skupove datoteka izravno iz sustavnog direktorija u strukturirane kategorije. Fokus projekta je na potpunoj privatnosti podataka, iznimno brzom izvršavanju i ugrađenim slojevima za sprječavanje prepisivanja datoteka s istim imenom.

Razvio **Tomislav Jurčević** (2026).

---

## ⚠️ Intelektualno Vlasništvo i Komercijalno Licenciranje

Ovaj projekt je zaštićen strogim **Ugovorom o Nekomercijalnoj Licenci**. Projekt **VIŠE NIJE** licenciran pod MIT otvorenim kodom.

- **✅ Dopušteno Korištenje**: Besplatno za osobnu upotrebu, studente, edukatore, hobiste i neprofitna istraživanja.
- **❌ Zabranjeno Korištenje**: Svaka implementacija, modifikacija, redistribucija ili uključivanje unutar komercijalnih subjekata, profitnih tvrtki, stranica financiranih oglasima ili kao dio plaćene usluge/ekstenzije strogo je zabranjeno bez važeće Komercijalne Licence.

### 💼 Upiti za Komercijalno Licenciranje
Ako vaša organizacija želi implementirati TidyDown™ u komercijalnom okruženju ili koristiti komponente njegovog sustava za upravljanje datotekama, morate ishoditi zasebnu komercijalnu licencu od Autora.

Za prilagođene uvjete licenciranja, upite o cijenama ili poduzetničku implementaciju, kontaktirajte Autora izravno putem e-pošte:  
📩 **tjurcevicos@gmail.com**

---

## Arhitektonske Značajke

- **GUID Telemetrijska Jezgra**: Dinamička apstrakcija koja koristi nativno mapiranje Windows Registry baze. Programski dohvaća apsolutnu putanju trenutnog korisnika, osiguravajući točno pronalaženje bez obzira na jezik sustava (`Downloads`, `Preuzimanja`).
- **Matrica Sigurnosne Kolizije**: Sloj za rekurzivno rješavanje konflikata imena. Ako u odredišnom folderu već postoji datoteka istog naziva, sustav izolira dolaznu datoteku i dodaje joj numerički indeks (`dokument_1.pdf`) radi apsolutne zaštite podataka.
- **Sloj za Izolaciju Smeća**: Ugrađeni kriteriji iznimaka koji dinamički prepoznaju i ignoriraju nedovršena preuzimanja iz preglednika (`.crdownload`) ili privremene datoteke (`.tmp`), sprječavajući nered unutar aktivnih kategorija.
- **Matrica Particije Kanala**: Višekanalno mapiranje koje u potpunosti odvaja multimedijski sadržaj, trenutno usmjeravajući video datoteke i audio zapise u zasebne, namjenske mape umjesto u zajednički direktorij.

---

## Operativna Mehanika Sustava

Kada se izvršna datoteka pokrene unutar operativnog sustava:

1. **Mapiranje Putanje**: Sustav povlači interne Windows GUID ključeve kako bi locirao točnu adresu glavne mape za preuzimanje.
2. **Sanitizacija Sadržaja**: Datoteke se analiziraju lokalno, a prazni znakovi ili greške u nazivima nastale preuzimanjem automatski se uklanjaju.
3. **Usmjeravanje Vektora**: Sustav uspoređuje ekstenziju svake datoteke s definiranim nizom pravila unutar `PRAVILA_SORTIRANJA`.
4. **Rješavanje Kolizije**: Ako datoteka s istim imenom već postoji na odredištu, matrica izračunava novi unikatni indeks za spremanje.
5. **Atomska Relokacija**: Sustav izvršava brzo i sigurno premještanje datoteke (`shutil.move`) u njezinu novu namjensku mapu.

---

## 🛑 ⚠️ Blokiranje Antivirusa (Lažna Uzbuna / False Positive)

Budući da je **TidyDown™** zapakiran u samostalnu izvršnu `.exe` datoteku pomoću PyInstallera i ne posjeduje skupu komercijalnu licencu i digitalni potpis, određeni antivirusni programi (poput **Avasta**, **AVG-a** ili **Windows Defendera**) mogu ga označiti kao prijetnju prilikom prvog pokretanja.

**Ovdje se radi o 100% lažnoj uzbuni (False Positive).** Izvorni kod je u potpunosti javan i dostupan za pregled unutar ovog repozitorija. Program radi isključivo lokalno i ne šalje nikakve podatke s vašeg računala.

### Kako dodati program u iznimke:
1. **Avast / AVG**: Otvorite Avast sučelje, idite na *Zaštita -> Karantena*, pronađite `TidyDown.exe`, kliknite na tri točkice i odaberite **Vrati i dodaj u iznimke**.
