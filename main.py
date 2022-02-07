#! python3
# coding: utf-8

from argparse import ArgumentParser
from module.pinger import Pinger
from re import match
import subprocess
import sys


class NomFichierNonValide(Exception):
    pass


def check_filename(filename: str) -> bool:
    """Verifier si le nom du fichier est correct.

    Verifier si le nom du fichier est correct (retourne True ou sinon False).

    PRE : filename est un nom de fichier valide
    POST : Retourne True si le nom du fichier est valide, sinon False
    RAISES : NomFichierNonValide si filename != regex

    Parameters:
            filename (str): un nom de fichier

    Returns:
            boolean (bool): Booléen si le nom du fichier est valide ou non
    """
    regex = r'\b[A-Za-z0-9._+-]+\.[A-Z|a-z]{2,6}\b'

    if not match(regex, filename):
        raise NomFichierNonValide("Le paramètre dois être un nom de fichier !")
    else:
        return True


def check_args() -> str:
    """Verifier les arguments de la ligne de commande

    Configuration des arguments de ligne de commande. Verifier si le nom du fichier reçu via arguments de ligne
    de commande est bien un nom de fichier.


    Returns:
            Nom du fichier (str): Si nom de fichier, retourne le nom du fichier ou erreur dans le cas échéant
    """
    parser = ArgumentParser(prog="Ping hostname", description="Tester la joignabilité d'un site.")
    parser.add_argument('filename', type=str, help='Le nom du fichier contenant la liste des noms des sites.')
    args = parser.parse_args()

    if check_filename(args.filename):
        return args.filename
    else:
        sys.exit("Le paramètre dois être un nom de fichier !")

def ping(hostname: str) -> bool:
    """Effectuer la commande ping sur les sites.

    Instancier un objet Pinger(), le concatener avec le hostname qu'on souhaite faire le ping()
    dessus. Passer la commande à subprocess.check_output() et on test si la valeur de retour contient la sous-chaine
    "0%" (aucune pertes de paquets)


    Parameters:
            hostname (str): un nom de fichier

    Returns:
            boolean (bool): Booléen si la commande ping() n'a subi aucune pertes.
    """
    test1 = Pinger()
    commande = f"{test1} {hostname}"
    try:
        output = subprocess.check_output(commande, shell=True, universal_newlines=True)

        return "0%" in output

    except subprocess.CalledProcessError:
        return False


def exec_script(filename: str):
    """Exécuter le script.

    Ouvrir le fichier, boucler tant qu'il y a des lignes, faire un ping() de chaque ligne grâce à la fonction ping() et
    afficher le résultat. Si ok -> UP, sinon DOWN.

    Parameters:
            filename (str): un nom de fichier

    Returns:
        none: Affiche le résultat du ping.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            for line in file:
                if ping(line.rstrip()):  # Linux problème ici! -> function ping() -> dis que file introuvable
                    print(f"{line.rstrip()} UP")
                else:
                    print(f"{line.rstrip()} DOWN")

    except FileNotFoundError:
        sys.exit("Fichier introuvable !")
    except IOError:
        sys.exit("Erreur IO !")


if __name__ == '__main__':
    exec_script(check_args())
