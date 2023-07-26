import os
import tabula
import pandas as pd

def extract_and_save_as_csv(pdf_path):
    # Mit tabula-py die Tabellendaten auslesen
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

    # Angenommen, die gewünschten Tabellendaten sind im ersten DataFrame (Index 0) gespeichert
    df = tables[0]

    # Den Dateinamen der PDF-Datei ohne Erweiterung extrahieren
    pdf_filename = os.path.splitext(os.path.basename(pdf_path))[0]

    # Den CSV-Dateinamen zusammenstellen
    csv_filename = f"{pdf_filename}.csv"

    # Den Pfad zum übergeordneten Verzeichnis der PDF-Datei extrahieren
    parent_folder = os.path.dirname(pdf_path)

    # Den Pfad zum Ordner erstellen, in dem die CSV-Datei gespeichert werden soll
    csv_folder = os.path.join(parent_folder, 'csv_output')

    # Falls der Ordner noch nicht existiert, erstelle ihn
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

    # Den vollständigen Pfad zur CSV-Datei erstellen
    csv_path = os.path.join(csv_folder, csv_filename)

    # Überprüfen, ob die CSV-Datei bereits vorhanden ist
    if os.path.exists(csv_path):
        print(f"{csv_filename} existiert bereits. Überspringe den Speichervorgang.")
        return

    # Die extrahierte Tabelle als CSV speichern
    df.to_csv(csv_path, index=False)  # 'index=False' verhindert, dass der DataFrame-Index in die CSV geschrieben wird

    print(f"Die Daten wurden als CSV in '{csv_path}' gespeichert.")


def process_pdfs_in_folder(folder_path):
    # Alle Dateien und Verzeichnisse im Hauptordner durchgehen
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".pdf"):
                # Den vollständigen Pfad zur PDF-Datei erstellen
                pdf_path = os.path.join(root, file)
                # PDF extrahieren und als CSV speichern
                extract_and_save_as_csv(pdf_path)


if __name__ == "__main__":
    # Pfad zum Hauptordner, der alle PDF-Dateien enthält
    main_folder = 'race_pdf/2023_u23_wm/'
    process_pdfs_in_folder(main_folder)
