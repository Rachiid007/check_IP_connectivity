#! python3

import subprocess
from argparse import ArgumentParser

from module import checker, pinger


def check_args() -> str:
    """Verifier les arguments de la ligne de commande

    Configuration des arguments de ligne de commande. Verifier si le nom du fichier reçu via arguments de ligne
    de commande est bien un nom de fichier.


    Returns:
            Nom du fichier (str): Si nom de fichier, retourne le nom du fichier ou erreur dans le cas échéant
    """
    parser = ArgumentParser(description='Test IP reachability from domain name or IP address',
                            epilog='Example: python3 /path/to/servers.txt --nbr_of_ping=4')
    parser.add_argument('pathname', type=checker.is_exist_pathname, help='Pathname with domain names / IP to ping')
    parser.add_argument('-c', '--number_of_ping', type=int, default=4, help='Number of ping to perform')
    args = parser.parse_args()

    print(args)

    return args.pathname


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
    test1 = pinger.Pinger()
    commande = f"{test1} {hostname}"
    try:
        output = subprocess.check_output(commande, shell=True, universal_newlines=True)

        return "0%" in output

    except subprocess.CalledProcessError:
        return False


def exec_script(list_servers: str):
    """Exécuter le script.

    Ouvrir le fichier, boucler tant qu'il y a des lignes, faire un ping() de chaque ligne grâce à la fonction ping() et
    afficher le résultat. Si ok -> UP, sinon DOWN.

    Parameters:
            list_servers (str): un nom de fichier

    Returns:
        none: Affiche le résultat du ping.
    """

    for i in list_servers:
        if ping(i):  # Linux problème ici! -> function ping() -> dis que file introuvable
            print(f"{i} UP")
        else:
            print(f"{i} DOWN")


if __name__ == '__main__':
    exec_script(check_args())
