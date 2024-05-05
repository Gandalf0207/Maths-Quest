# votre_script.py
import subprocess


def installer_pip_et_bibliotheques():
    # Installer pip
    subprocess.run(["python", "-m", "ensurepip"])

    # Installer les bibliothèques requises
    subprocess.run(["pip", "install", "matplotlib"])
    # Ajoutez d'autres bibliothèques au besoin
    subprocess.run(["mpm", "--install", "type1cm"])
    subprocess.run(["mpm", "--install", "cm-super"])
    subprocess.run(["mpm", "--install", "geometry"])
    subprocess.run(["mpm", "--install", "underscore"])
    subprocess.run(["mpm", "--install", "zhmetrics"])

# type1cm.sty
# type1cm

# type1ec.sty
# cm-super

# geometry.sty
# geometry

# underscore.sty
# underscore

# ttfonts.map
# zhmetrics






if __name__ == "__main__":
    installer_pip_et_bibliotheques()
    print("Pip et les bibliothèques requises ont été installés avec succès !")