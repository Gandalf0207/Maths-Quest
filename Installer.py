# votre_script.py
import subprocess


def installateur():
    # on recupère le jeu
    subprocess.run("git clone https://github.com/Gandalf0207/Projet-Ouvert-Jeu-.git", shell=True, text=True)

    #Installation de pytohn 3.12.3 (dernière version (modif name ?))
    python_installer = "python-3.12.3-amd64.exe"
    subprocess.call(python_installer, shell=True)
    # Installer pip
    subprocess.run(["python", "-m", "ensurepip"], shell=True)
    # Installer les bibliothèques requises
    subprocess.run(["pip", "install", "matplotlib"], shell=True)

    # Installation miktek : compilateur latex
    subprocess.run("basic-miktex-24.1-x64.exe", shell=True)
    # Ajoutez d'autres bibliothèques au besoin
    subprocess.run(["mpm", "--install", "type1cm"], shell=True)
    subprocess.run(["mpm", "--install", "cm-super"], shell=True)
    subprocess.run(["mpm", "--install", "geometry"], shell=True)
    subprocess.run(["mpm", "--install", "underscore"], shell=True)
    subprocess.run(["mpm", "--install", "zhmetrics"], shell=True)


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
    installateur()
    print("Pip et les bibliothèques requises ont été installés avec succès !")