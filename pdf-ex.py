import tabula
import pandas as pd

# Pfad zum PDF-File
pdf_path = 'race_pdf/2023_u23_wm/bw8+/bw8+_heat1.pdf'

# Auslesen der PDF
tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

# Tabellendaten ausgeben
for table in tables:
    print(table)

# Tabellendaten als CSV Speichern
