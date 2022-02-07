#! python3
# coding: utf-8
from platform import system
import sys


class Pinger:
    """Une classe pour représenter un Ping.

    Args:
       system_now (str): système d'exploitation actuel.
        count (int): nombre de ping (par défaut 4).
        nbr_second (int): nombre de seconde pour chaque ping (par défaut 4).

    Attributes:
        __system_now (str): système d'exploitation actuel.
        __count (int): nombre de ping (par défaut 4).
        __nbr_second (int): nombre de seconde pour chaque ping (par défaut 4).

    Returns:
        str: La commande ping avec la version du système d'exploitation actuel.
    """

    def __init__(self, system_now=system().lower(), count=4, nbr_second=4):
        self.__system_now = system_now

        if isinstance(count, int):
            self.__count = count
        else:
            sys.exit("Pas un entier !")

        if isinstance(count, int):
            self.__nbr_second = nbr_second
        else:
            sys.exit("Pas un entier !")

    def number_of_ping(self) -> str:
        """nombre de seconde pour chaque ping.
            Returns:
                str: Le nombre de ping demandé pour la version du système d'exploitation actuel.
        """
        if self.__system_now == "windows":
            return f"-n {self.__count}"
        else:
            return f"-c {self.__count}"

    def timeout(self) -> str:
        """timeout pour chaque ping.
            Returns:
                str: Le nombre de timeout pour chaque ping avec la version du système d'exploitation actuel.
        """
        if self.__system_now == "windows":
            return f"-w {(self.__nbr_second * 1000)}"
        else:
            return f"-w {self.__nbr_second}"

    def __str__(self):
        return f"ping {self.number_of_ping()} {self.timeout()}"
