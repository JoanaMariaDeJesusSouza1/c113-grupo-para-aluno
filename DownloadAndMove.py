import sys
import random

import os
import shutil



from_dir = ""            # Adicione o caminho da sua pasta "Downloads".
to_dir = ""              # Crie a pasta "Arquivos_Documentos" em sua área de trabalho e atualize o caminho de acordo.

#criando dicionário de extensões de arquivos.
dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Classe Gerenciadora de Eventos

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

           
                # if os.path.exists(path2):

                #     print("Diretório Existe...")
                #     print("Movendo " + file_name + "....")
                #     shutil.move(path1, path3)
                #     time.sleep(1)

                # else:
                    

# Inicialize a Classe Gerenciadora de Eventos


# Inicialize o Observer


# Agende o Observer


# Inicie o Observer
