import pyautogui
import time
import os
from datetime import datetime

# Définir le chemin de sauvegarde
chemin_sauvegarde = "W:\\CapturesEcran"

# Crée le dossier s'il n'existe pas
os.makedirs(chemin_sauvegarde, exist_ok=True)

# Capture toutes les 5 secondes (5 captures au total)
for i in range(5):
    horodatage = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    chemin_fichier = os.path.join(chemin_sauvegarde, f"screenshot_{i + 1}_{horodatage}.png")

    # Capture d'écran
    screenshot = pyautogui.screenshot()
    screenshot.save(chemin_fichier)

    print(f"✅ Capture {i + 1} enregistrée dans : {chemin_fichier}")
    time.sleep(5)

print("\n🚀 Toutes les captures ont été enregistrées avec succès !")



