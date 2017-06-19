"""
qsdf
"""
class Articulation(object):
    """
        objet articulation
    """
    def __init__(self, pt_milieu, pin, carte):
        """
            pt_milieu => double
            pin_carte_adafruit => int
            carte_adafruit => int
        """
        self.pt_milieu = pt_milieu
        self.pin_carte_adafruit = pin
        self.carte_adafruit = carte
        self.position_consigne = pt_milieu

        self.servomin = 150
        self.servomax = 600

        self.position_courante = pt_milieu

    def get_point_milieu(self):
        return self.pt_milieu
        
    def set_position_courante(self, angle):
        """
            angle => double
        """
        self.position_courante = angle

    def get_position_courante(self):
        """
            retourne la position courante
        """
        return self.position_courante

    def set_position_consigne(self, angle):
        """
            angle => double
        """
        self.position_consigne = angle
    def get_position_consigne(self):
        """
            retourne la positon de consigne
        """
        return self.position_consigne

    def get_servomin(self):
        """
            retourne la position min du servo pour etalonnage
        """
        return self.servomin

    def get_servomax(self):
        """
            retourne la position max du servo pour etalonnage
        """
        return self.servomax

    def get_carte_adafruit(self):
        """
            retourne le numero de la carte sur laquelle est branche le servo
            0 => pwm
            1 => pwm2
        """
        return self.carte_adafruit

    def get_pin_adafruit(self):
        """
            retourne le numero du pin sur lequel est branche le servo
        """
        return self.pin_carte_adafruit
        