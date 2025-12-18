import os
import PyPDF2
import emoji

merger = PyPDF2.PdfWriter()
## Liste des PDF à fusionner
pdf_to_merge = []

# chemin du dossier contenant les PDF
path_folder = ""
all_files = os.listdir(path_folder)

# récupère que les fichiers pdf qu'on ajoute dans pdf_to_merge
for file in all_files:
    if file.endswith(".pdf"):
        pdf_to_merge.append(path_folder + file)
print(f"Il y a {len(pdf_to_merge)} fichier pdf trouvé dans le dossier")

# fusionne les PDF dans pdf_to_merge
pdf_to_merge_sorted = pdf_to_merge.sort()

for pdf in pdf_to_merge_sorted:
    try:
        merger.append(pdf)
        print(f"👌🏾{pdf} ajouté avec succès")
    except Exception as e:
        print(f"Erreur sur le fichier {pdf} : {e} ")

with open("merged.pdf", "wb") as f:
    merger.write(f)
