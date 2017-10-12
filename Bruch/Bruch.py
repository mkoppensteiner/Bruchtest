class Bruch(object):

    def __init__(self, *args):
        """
        :param Tupel *args: Tupel in dem ein Bruch, Zaehler und Nenner oder nur Zaehler steht
        """
        if (len(args) == 1):
            if (isinstance(args[0], Bruch)):
                self.zaehler = args[0].zaehler
                self.nenner = args[0].nenner
            else:
                self.zaehler = args[0]
                self.nenner = 1
        else:
            self.zaehler = args[0]
            self.nenner = args[1]

        if (self.nenner == 0):
            raise ZeroDivisionError("Nenner =/= 0")

        if (isinstance(self.zaehler, float)):
            raise TypeError("Zähler float")

        if (isinstance(self.nenner, float)):
            raise TypeError("Nenner float")

        if (isinstance(self.nenner, str) or isinstance(self.zaehler, str)):
            raise TypeError("Nenner/Zaehler str")

    @staticmethod
    def __makeBruch(bruch):
        """
        Ruft die init Methode mit dem Parameter bruch auf
        :param bruch: Der Bruch bzw. die Zahl
        :return: Bruch mit dem Wert bruch
        """

        return Bruch(bruch)

    def __int__(self):
        """
        Wandelt Bruch in int um
        :return: int Wert des Bruches
        """

        return int(self.zaehler/self.nenner)

    def __float__(self):
        """
        Wandelt Bruch in float um
        :return: float Wert des Bruches
        """

        return float(self.zaehler) / float(self.nenner)

    def __abs__(self):
        """
        Wandelt Bruch in absoluten Wert um
        :return: absoluter Wert des Bruches
        """

        return abs(float(self.zaehler) / float(self.nenner))

    def __neg__(self):
        """
        Negiert den Zaehler
        :return: negierter Wert des Bruches
        """

        return Bruch(-1 * self.zaehler, self.nenner)

    def __str__(self):
        """
        Wandelt Bruch in string um
        :return: der Bruch in als string
        """

        if (self.nenner == 1):
            erg = int(self.zaehler) / int(self.nenner)
            return "(%d)" % erg

        if (self.zaehler < 0):
            self.zaehler = -self.zaehler

        if (self.nenner < 0):
            self.nenner = -self.nenner

        return "(%d/%d)" % (self.zaehler, self.nenner)

    def __invert__(self):
        """
        Invertiert Bruch (vertauscht Zaehäer und Nenner)
        :return: invertierter Bruch
        """

        return Bruch(self.nenner,self.zaehler)

    def __pow__(self, power, modulo=None):
        """
        Zaehler und Nenner werden mit sich selbst multiplieziert
        :param power: wie oft mit sich selbst multipliziert wird
        :return: mit sich selbst multiplizierter Bruch
        """

        return Bruch(self.zaehler ** power, self.nenner ** power)

    def __eq__(self, other):
        """
        Überprüft ob self gleich other ist
        :param other: die zu vergleichende Zahl
        :return: True oder False
        """

        return float(self) == float(other)

    def __ne__(self, other):
        """
        Überprüft ob self ungleich other ist
        :param other: die zu vergleichende Zahl
        :return: True oder False
        """

        return float(self) != float(other)

    def __gt__(self, other):
        """
        Überprüft ob self größer als other ist
        :param other: die zu vergleichende Zahl
        :return: True oder False
        """

        return float(self) > float(other)

    def __lt__(self, other):
        """
        Ueberprueft ob self kleiner als other ist
        :param other: die zu vergleichende Zahl
        :return: True oder False
        """

        return float(self) < float(other)

    def __ge__(self, other):
        """
        Ueberprueft ob self groesser oder gleich other ist
        :param other: die zu vergleichende Zahl
        :return: True oder False
        """

        return float(self) >= float(other)

    def __le__(self, other):
        """
        Ueberprueft ob self kleiner oder gleich other ist
        :param other: die zu vergleichende Zahl
        :return: True oder False
        """

        return float(self) <= float(other)

    def __add__(self, other):
        """
        Addiert eine Zahl oder einen Bruch mit self
        :param other: Zahl oder Bruch
        :return: Ergebnis als float
        """

        if (isinstance(other, int)):
            erg = float(Bruch(self.zaehler, self.nenner)) + float(other)

        elif (isinstance(other, Bruch)):
            erg = float(Bruch(self.zaehler, self.nenner)) + float(Bruch(other.zaehler, other.nenner))
        else:
            raise TypeError
        return erg

    def __iadd__(self, other):
        """
        Addiert self mit other
        :param other: Zahl die dazugerechnet wird
        :return: Addition von self und other
        """

        return self + other

    def __radd__(self, other):
        """
        Addiert other auf self
        :param other: Zahl die dazugerechnet wird
        :return: Addition
        """

        return self + other

    def __sub__(self, other):
        """
        Subtrahiert eine Zahl oder einen Bruch mit self
        :param other: Zahl oder Bruch
        :return: Ergebnis als float
        """

        if (isinstance(other, int)):
            erg = float(Bruch(self.zaehler, self.nenner)) - float(other)

        elif (isinstance(other, Bruch)):
            erg = float(Bruch(self.zaehler, self.nenner)) - float(Bruch(other.zaehler, other.nenner))
        else:
            raise TypeError
        return erg

    def __isub__(self, other):
        """
        Subtraktion von self mit other
        :param other: die zu subtrahierende Zahl
        :return: Subtraktion von self und other
        """

        return self - other

    def __rsub__(self, other):
        """
        Subtrahiert eine Zahl mit den Bruch
        :param other: die zu subtrahierende Zahl
        :return: Subtratkion
        """

        return -self + other

    def __mul__(self, other):
        """
        Multiplikation von Bruch mit Bruch bzw. Bruch mit Zahl
        :param other: Bruch oder Zahl
        :return: Multiplikation
        """

        if (isinstance(other, int)):
            erg = float(Bruch(self.zaehler, self.nenner)) * float(other)

        elif (isinstance(other, Bruch)):
            erg = float(Bruch(self.zaehler, self.nenner)) * float(Bruch(other.zaehler, other.nenner))
        else:
            raise TypeError
        return erg

    def __imul__(self, other):
        """
        Multiplikation von self mit other
        :param other: Zahl
        :return: Multiplikation
        """

        return self * other

    def __rmul__(self, other):
        """
        Multiplikation von self mit other
        :param other: Zahl
        :return: Multiplikation
        """

        return self * other

    def __iter__(self):
        """
        Iteriert durch den Bruch
        :return: Iterator
        """

        return iter([self.zaehler, self.nenner])

    def __truediv__(self, other):
        """
        Dividiert Bruch von other
        :param other: Bruch oder Zahl
        :return: Division
        """

        if (isinstance(other, int)):
            erg = float(Bruch(self.zaehler, self.nenner)) / float(other)

        elif (isinstance(other, Bruch)):
            erg = float(Bruch(self.zaehler, self.nenner)) / float(Bruch(other.zaehler, other.nenner))
        else:
            raise TypeError
        return erg

    def __itruediv__(self, other):
        """
        Division von self durch other
        :param other: Zahl
        :return: Division
        """

        return self / other

    def __rtruediv__(self, other):
        """
        Dividiert nur wenn self oder other nicht 0 ist
        :param other: Zahl
        :return: Division
        """

        if (self == 0 or other == 0):
            raise ZeroDivisionError
        return self / other