import os
import shutil
import winreg

def dohvati_univerzalni_downloads_folder():
    try:
        kljuc_putanja = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
        guid_za_downloads = "{7D1D3A04-DEBB-4115-95C0-2F35929BEC04}"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, kljuc_putanja) as kljuc:
            putanja, _ = winreg.QueryValueEx(kljuc, guid_za_downloads)
            return os.path.expandvars(putanja)
    except Exception:
        return os.path.join(os.path.expanduser("~"), "Downloads")

FOLDER_ZA_CISCENJE = dohvati_univerzalni_downloads_folder()

PRAVILA_SORTIRANJA = {
    "Music_and_Audio": [".mp3", ".wav", ".wma", ".ogg", ".flac", ".m4a", ".aac", ".amr", ".mid", ".midi"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".vob", ".mpeg", ".3gp"],
    "Archives_and_Zip": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso", ".bz2", ".xz", ".z", ".pkg", ".deb", ".rpm"],
    "PDF_Documents": [".pdf"],
    "Text_and_Office": [".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".odt", ".rtf"],
    "Images_and_Photos": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico", ".psd", ".ai"],
    "Programs_and_Installers": [".exe", ".msi", ".bat", ".cmd", ".sh", ".com", ".jar"],
    "Ebooks": [".epub", ".mobi", ".azw", ".azw3", ".djvu"],
    "Design_3D_and_CAD": [".stl", ".obj", ".fbx", ".3ds", ".dwg", ".dxf"]
}

def osiguraj_unikatno_ime(odredisni_folder, ime_datoteke):
    ime, ekstenzija = os.path.splitext(ime_datoteke)
    nova_putanja = os.path.join(odredisni_folder, ime_datoteke)
    brojac = 1
    while os.path.exists(nova_putanja):
        novo_ime = f"{ime}_{brojac}{ekstenzija}"
        nova_putanja = os.path.join(odredisni_folder, novo_ime)
        brojac += 1
    return nova_putanja

def sortiraj_folder():
    if not os.path.exists(FOLDER_ZA_CISCENJE):
        print(f"Error: Folder {FOLDER_ZA_CISCENJE} does not exist!")
        return

    print("TidyDown is running...")
    brojac = 0

    for datoteka in os.listdir(FOLDER_ZA_CISCENJE):
        datoteka_cisto = datoteka.strip()
        putanja_datoteke = os.path.join(FOLDER_ZA_CISCENJE, datoteka)

        if os.path.isdir(putanja_datoteke) or datoteka_cisto.lower() == "desktop.ini":
            continue

        # Ovdje je ispravljeno: dodan je [1] na kraj da uzme samo ekstenziju
        ekstenzija = os.path.splitext(datoteka_cisto)[1].lower()

        if ekstenzija in [".crdownload", ".tmp"]:
            continue

        nadjen_folder = False
        for naziv_foldera, ekstenzije in PRAVILA_SORTIRANJA.items():
            if ekstenzija in ekstenzije:
                odredisni_folder = os.path.join(FOLDER_ZA_CISCENJE, naziv_foldera)
                if not os.path.exists(odredisni_folder):
                    os.makedirs(odredisni_folder)

                nova_putanja = osiguraj_unikatno_ime(odredisni_folder, datoteka_cisto)
                shutil.move(putanja_datoteke, nova_putanja)
                print(f"Moved: {datoteka_cisto} -> {nav_foldera}" if 'nav_foldera' in locals() else f"Moved: {datoteka_cisto} -> {naziv_foldera}")
                brojac += 1
                nadjen_folder = True
                break
        
        if not nadjen_folder and ekstenzija != "":
            odredisni_folder = os.path.join(FOLDER_ZA_CISCENJE, "Other")
            if not os.path.exists(odredisni_folder):
                os.makedirs(odredisni_folder)
                
            nova_putanja = osiguraj_unikatno_ime(odredisni_folder, datoteka_cisto)
            shutil.move(putanja_datoteke, nova_putanja)
            print(f"Moved: {datoteka_cisto} -> Other")
            brojac += 1

    print(f"Done! Total files sorted: {brojac}")

if __name__ == "__main__":
    sortiraj_folder()
