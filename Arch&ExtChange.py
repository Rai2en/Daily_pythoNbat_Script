
import os
import shutil

def main():
    # Parcourir tous les dossiers dans le répertoire courant
    for item in os.listdir('.'):
        if os.path.isdir(item):
            # Créer une archive ZIP pour chaque dossier
            shutil.make_archive(item, 'zip', item)
            # Renommer l'extension de .zip à .cbz
            os.rename(f"{item}.zip", f"{item}.cbz")
            print(f"{item} a été archivé en {item}.cbz")

if __name__ == "__main__":
    main()

#import os
#import shutil

#def archive_folders():
    # Parcourir tous les dossiers dans le répertoire courant
    #for item in os.listdir('.'):
      #  if os.path.isdir(item):
            # Créer une archive ZIP pour chaque dossier
        #    shutil.make_archive(item, 'zip', item)

#def change_extension_to_cbz():
    # Parcourir tous les fichiers dans le répertoire courant
 #   for filename in os.listdir('.'):
    # Vérifier si le fichier est une archive ZIP et changer le nom avec l'extension '.cbz'
 #       if filename.endswith('.zip'):
       #     new_name = filename.replace('.zip', '.cbz')
              # Renommer le fichier
        #      os.rename(filename, new_name)
        #    print(f"{filename} a été renommé en {new_name}")
#
#def main():
    #archive_folders()
    #change_extension_to_cbz()

#if __name__ == "__main__":
   # main()
