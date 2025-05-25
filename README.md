# Capture d'Écran Automatisée

Ce projet est un script Python qui utilise la bibliothèque `pyautogui` pour prendre des captures d'écran automatiquement à intervalles réguliers. Les captures sont sauvegardées dans un dossier spécifié.

## Fonctionnalités

- **Captures d'écran automatiques** : Prend des captures toutes les 5 secondes.
- **Nom de fichier horodaté** : Les fichiers sont nommés avec un horodatage pour éviter les collisions.
- **Dossier de sauvegarde** : Crée un dossier pour stocker les captures si celui-ci n'existe pas.

## Prérequis

- Python 3.x
- Bibliothèque `pyautogui`

## Installation

1. Assurez-vous d'avoir Python installé sur votre machine.
2. Installez `pyautogui` :
   ```bash
   pip install pyautogui


CORRECTION ERREURs POSSIBLEs:
➡️ 1. Installe Pillow
Installe Pillow directement dans ton environnement virtuel :

bash
Copier
Modifier
pip install pillow
➡️ 2. Mets à jour pyautogui, pyscreeze et pillow
Il est possible que la version de Pillow soit trop ancienne ou incompatible. Mets tout à jour :

bash
Copier
Modifier
pip install --upgrade pyautogui pyscreeze pillow
➡️ 3. Vérifie la compatibilité entre Python, Pillow et PyAutoGUI
Certaines versions de Python ne sont pas compatibles avec la dernière version de Pillow. Vérifie ta version de Python :

bash
Copier
Modifier
python --version
✅ Si tu utilises Python 3.12+, il se peut que Pillow ne soit pas encore totalement compatible avec ta version → Essaye de passer à Python 3.10 ou 3.11.

➡️ 4. Test rapide après correction
Relance le script après l'installation :

python
Copier
Modifier
import pyautogui

screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

print("✅ Capture d'écran réussie !")
🔎 👉 Si le problème persiste :
Essaie d'importer directement Pillow pour voir si le problème vient bien de là :

python
Copier
Modifier
from PIL import Image
➡️ Si cette commande lève une erreur → le problème vient de l'installation de Pillow.

Si pyautogui est toujours cassé → Désinstalle et réinstalle-le complètement :

bash
Copier
Modifier
pip uninstall pyautogui pyscreeze pillow
pip install pyautogui

