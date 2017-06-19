"""
Classe Hexapode
"""

from __future__ import division
import time
import Adafruit_PCA9685
from articulation import Articulation


class Hexapode(object):
	"""
	Collection d'articulation
	"""

	def __init__(self):
		print "SERVEUR : CREATION HEXAPODE"
		self.pwm = Adafruit_PCA9685.PCA9685()
		self.pwm2 = Adafruit_PCA9685.PCA9685(address=0x41, busnum=1)
		self.pwm.set_pwm_freq(60)
		self.pwm2.set_pwm_freq(60)
		
		self.offset_femur = 0
		self.offset_tibia = 0
		
		self.liste_articulation = [
			# patte 1 
			Articulation(90, 0, 0),
			Articulation(103 + self.offset_femur, 1, 0),
			Articulation(91 + self.offset_tibia, 2, 0),
			# patte 2
			Articulation(90, 3, 0),
			Articulation(112 + self.offset_femur, 4, 0),
			Articulation(101 + self.offset_tibia, 5, 0),
			# patte 3
			Articulation(90, 6, 0),
			Articulation(111 + self.offset_femur, 7, 0),
			Articulation(109 + self.offset_tibia, 8, 0),
			# patte 4
			Articulation(90, 0, 1),
			Articulation(111 - self.offset_femur, 1, 1),
			Articulation(94 - self.offset_tibia, 2, 1),
			# patte 5
			Articulation(90, 3, 1),
			Articulation(112 - self.offset_femur, 4, 1),
			Articulation(119 - self.offset_tibia, 5, 1),
			# patte 6
			Articulation(90, 6, 1),
			Articulation(109 - self.offset_femur, 7, 1),
			Articulation(120 - self.offset_tibia, 8, 1)
		]

	def initialiser(self):
		"""
		Initialise la position des servos a leurs points milieu
		"""
		print "SERVEUR : INITIALISATION HEXAPODE"
		for art in self.liste_articulation:
			art.set_position_courante(art.get_point_milieu())
			if art.get_carte_adafruit() == 0:
				self.pwm.set_pwm(art.get_pin_adafruit(), 0, self.arduino_map(
					art.get_point_milieu(), 0, 180, art.get_servomin(), art.get_servomax()))
			elif art.get_carte_adafruit() == 1:
				self.pwm2.set_pwm(art.get_pin_adafruit(), 0, self.arduino_map(
					art.get_point_milieu(), 0, 180, art.get_servomin(), art.get_servomax()))
			else:
				print "ERREUR DANS liste_articulation"

	def arduino_map(self, x, in_min, in_max, out_min, out_max):
		"""
		Initialise la position des servos a leurs points milieu
		"""
		result = (x - in_min) * (out_max -
								 out_min) // (in_max - in_min) + out_min
		return result

	def test_position_servos(self):
		"""
		retourne TRUE si tous les servos ont atteint la position de consigne
		"""
		retour = True
		for art in self.liste_articulation:
			if art.get_position_courante() != art.get_position_consigne():
				retour = False
		return retour

	def evoluer(self):
		"""
		bla
		"""
		
		while self.test_position_servos() == False:
			
			for art in self.liste_articulation:                
				if art.get_position_courante() < art.get_position_consigne():
					
					art.set_position_courante(art.get_position_courante() + 1)
					if art.get_carte_adafruit() == 0:
						self.pwm.set_pwm(art.get_pin_adafruit(), 0, self.arduino_map(art.get_position_courante(), 0, 180, art.get_servomin(), art.get_servomax()))
					elif art.get_carte_adafruit() == 1:
						self.pwm2.set_pwm(art.get_pin_adafruit(), 0, self.arduino_map(art.get_position_courante(), 0, 180, art.get_servomin(), art.get_servomax()))
				if art.get_position_courante() > art.get_position_consigne():
					art.set_position_courante(art.get_position_courante() - 1)
					if art.get_carte_adafruit() == 0:
						self.pwm.set_pwm(art.get_pin_adafruit(), 0, self.arduino_map(art.get_position_courante(), 0, 180, art.get_servomin(), art.get_servomax()))
					elif art.get_carte_adafruit() == 1:
						self.pwm2.set_pwm(art.get_pin_adafruit(), 0, self.arduino_map(art.get_position_courante(), 0, 180, art.get_servomin(), art.get_servomax()))
				time.sleep(0.001)
				


	def bouger_servo(self, servo, angle):
		if servo == "b1s0":
			self.pwm.set_pwm(0, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[0].get_servomin(), self.liste_articulation[0].get_servomax()))
			self.liste_articulation[0].set_position_courante(angle)

		if servo == "b1s1":
			self.pwm.set_pwm(1, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[1].get_servomin(), self.liste_articulation[1].get_servomax()))
			self.liste_articulation[1].set_position_courante(angle)

		if servo == "b1s2":
			self.pwm.set_pwm(2, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[2].get_servomin(), self.liste_articulation[2].get_servomax()))
			self.liste_articulation[2].set_position_courante(angle)

		if servo == "b2s3":
			self.pwm.set_pwm(3, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[3].get_servomin(), self.liste_articulation[3].get_servomax()))
			self.liste_articulation[3].set_position_courante(angle)

		if servo == "b2s4":
			self.pwm.set_pwm(4, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[4].get_servomin(), self.liste_articulation[4].get_servomax()))
			self.liste_articulation[4].set_position_courante(angle)

		if servo == "b2s5":
			self.pwm.set_pwm(5, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[5].get_servomin(), self.liste_articulation[5].get_servomax()))
			self.liste_articulation[5].set_position_courante(angle)

		if servo == "b3s6":
			self.pwm.set_pwm(6, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[6].get_servomin(), self.liste_articulation[6].get_servomax()))
			self.liste_articulation[6].set_position_courante(angle)

		if servo == "b3s7":
			self.pwm.set_pwm(7, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[7].get_servomin(), self.liste_articulation[7].get_servomax()))
			self.liste_articulation[7].set_position_courante(angle)

		if servo == "b3s8":
			self.pwm.set_pwm(8, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[8].get_servomin(), self.liste_articulation[8].get_servomax()))
			self.liste_articulation[8].set_position_courante(angle)

		if servo == "b4s0":
			self.pwm2.set_pwm(0, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[9].get_servomin(), self.liste_articulation[9].get_servomax()))
			self.liste_articulation[9].set_position_courante(angle)

		if servo == "b4s1":
			self.pwm2.set_pwm(1, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[10].get_servomin(), self.liste_articulation[10].get_servomax()))
			self.liste_articulation[10].set_position_courante(angle)

		if servo == "b4s2":
			self.pwm2.set_pwm(2, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[11].get_servomin(), self.liste_articulation[11].get_servomax()))
			self.liste_articulation[11].set_position_courante(angle)

		if servo == "b5s3":
			self.pwm2.set_pwm(3, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[12].get_servomin(), self.liste_articulation[12].get_servomax()))
			self.liste_articulation[12].set_position_courante(angle)

		if servo == "b5s4":
			self.pwm2.set_pwm(4, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[13].get_servomin(), self.liste_articulation[13].get_servomax()))
			self.liste_articulation[13].set_position_courante(angle)

		if servo == "b5s5":
			self.pwm2.set_pwm(5, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[14].get_servomin(), self.liste_articulation[14].get_servomax()))
			self.liste_articulation[14].set_position_courante(angle)

		if servo == "b6s6":
			self.pwm2.set_pwm(6, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[15].get_servomin(), self.liste_articulation[15].get_servomax()))
			self.liste_articulation[15].set_position_courante(angle)

		if servo == "b6s7":
			self.pwm2.set_pwm(7, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[16].get_servomin(), self.liste_articulation[16].get_servomax()))
			self.liste_articulation[16].set_position_courante(angle)

		if servo == "b6s8":
			self.pwm2.set_pwm(8, 0, self.arduino_map(angle, 0, 180,self.liste_articulation[17].get_servomin(), self.liste_articulation[17].get_servomax()))
			self.liste_articulation[17].set_position_courante(angle)


	def avancer(self):

		angle_haut = 40
		angle_avant = 40
		angle_arriere = 40

		#1 - 4 - 16 => en haut 
		self.liste_articulation[1].set_position_consigne(self.liste_articulation[1].get_point_milieu() + angle_haut)
		self.liste_articulation[4].set_position_consigne(self.liste_articulation[4].get_point_milieu() + angle_haut)
		self.liste_articulation[16].set_position_consigne(self.liste_articulation[16].get_point_milieu() + angle_haut)

		#0 - 3 - 15 => avant
		self.liste_articulation[0].set_position_consigne(self.liste_articulation[0].get_point_milieu() + angle_avant)
		self.liste_articulation[3].set_position_consigne(self.liste_articulation[3].get_point_milieu() + angle_avant)
		self.liste_articulation[15].set_position_consigne(self.liste_articulation[15].get_point_milieu() + angle_avant)

		self.evoluer()

		#1 - 4 - 16 => pt milieu
		self.liste_articulation[1].set_position_consigne(self.liste_articulation[1].get_point_milieu())
		self.liste_articulation[4].set_position_consigne(self.liste_articulation[4].get_point_milieu())
		self.liste_articulation[16].set_position_consigne(self.liste_articulation[16].get_point_milieu())

		self.evoluer()

		#7 - 10 - 13 => en haut 
		self.liste_articulation[7].set_position_consigne(self.liste_articulation[7].get_point_milieu() + angle_haut)
		self.liste_articulation[10].set_position_consigne(self.liste_articulation[10].get_point_milieu() + angle_haut)
		self.liste_articulation[13].set_position_consigne(self.liste_articulation[13].get_point_milieu() + angle_haut)

		#6 - 9 - 12 => avant
		self.liste_articulation[6].set_position_consigne(self.liste_articulation[6].get_point_milieu() + angle_avant)
		self.liste_articulation[9].set_position_consigne(self.liste_articulation[9].get_point_milieu() + angle_avant)
		self.liste_articulation[12].set_position_consigne(self.liste_articulation[15].get_point_milieu() + angle_avant)

		self.evoluer()

		#0 - 3 - 15 => arriere
		self.liste_articulation[0].set_position_consigne(self.liste_articulation[0].get_point_milieu() + angle_arriere)
		self.liste_articulation[3].set_position_consigne(self.liste_articulation[3].get_point_milieu() + angle_arriere)
		self.liste_articulation[15].set_position_consigne(self.liste_articulation[15].get_point_milieu() + angle_arriere)

		self.evoluer()

