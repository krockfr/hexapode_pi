#!/usr/bin/env python
from hexapode import *
from point import Point
import socket
import time

liste_pos = []
tab_prog = []

def analyse(trame):
    try:
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        print "TRAME RECUE " + trame
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        if trame != "":
            if trame == "dmdepose":
                print "----------------------------------------------------------------------"
                print "CLIENT : DEMANDE POSITIONS"
                print "----------------------------------------------------------------------"
                time.sleep(0.3)
                tmp = ""

                for art in mon_pode.liste_articulation :
                    tmp = tmp + '#' + str(art.get_position_courante())
                
                print tmp
                time.sleep(0.3)
                conn.send(tmp)

            elif 'code1' in trame:
                print "----------------------------------------------------------------------"
                print "CLIENT : TOUS SERVO A XX"
                print "----------------------------------------------------------------------"
                tmp = trame.split('#')
                i = 1
                for art in mon_pode.liste_articulation:
                    art.set_position_consigne(int(float(tmp[i])))
                    i = i + 1
                mon_pode.evoluer()

            elif trame == "debug":
                print "----------------------------------------------------------------------"
                print "CLIENT : DEBUG"
                print "----------------------------------------------------------------------"
                print "    - positions courantes -"
                time.sleep(0.3)

                print "B1S2 = " +  str(mon_pode.liste_articulation[2].get_position_courante()) + " | " + "B1S1 = " +  str(mon_pode.liste_articulation[1].get_position_courante()) + " | " + "B1S0 = " +  str(mon_pode.liste_articulation[0].get_position_courante())+ " | " + "B4S0 = " +  str(mon_pode.liste_articulation[9].get_position_courante()) + " | " + "B4S1 = " +  str(mon_pode.liste_articulation[10].get_position_courante()) + " | " + "B4S2 = " +  str(mon_pode.liste_articulation[11].get_position_courante())
                print "B2S5 = " +  str(mon_pode.liste_articulation[5].get_position_courante()) + " | " + "B2S4 = " +  str(mon_pode.liste_articulation[4].get_position_courante()) + " | " + "B2S3 = " +  str(mon_pode.liste_articulation[3].get_position_courante())+ " | " + "B5S3 = " +  str(mon_pode.liste_articulation[12].get_position_courante()) + " | " + "B5S4 = " +  str(mon_pode.liste_articulation[13].get_position_courante()) + " | " + "B5S5 = " +  str(mon_pode.liste_articulation[14].get_position_courante())
                print "B3S8 = " +  str(mon_pode.liste_articulation[8].get_position_courante()) + " | " + "B3S7 = " +  str(mon_pode.liste_articulation[7].get_position_courante()) + " | " + "B3S6 = " +  str(mon_pode.liste_articulation[6].get_position_courante())+ " | " + "B6S6 = " +  str(mon_pode.liste_articulation[15].get_position_courante()) + " | " + "B6S7 = " +  str(mon_pode.liste_articulation[16].get_position_courante()) + " | " + "B6S8 = " +  str(mon_pode.liste_articulation[17].get_position_courante())

            elif trame == "init":
                print "----------------------------------------------------------------------"
                print "CLIENT : DEMANDE INITIALISATION"
                print "----------------------------------------------------------------------"
                mon_pode.initialiser()
            elif 'code2' in trame :
                print "----------------------------------------------------------------------"
                print "CLIENT : DEMANDE MOUVEMENT 1 SERVO"
                print "----------------------------------------------------------------------"
                tmp, servo, angle = trame.split("#")
                print servo
                print angle
                mon_pode.bouger_servo(servo, int(float(angle)))
            elif 'code3' in trame:
                print "----------------------------------------------------------------------"
                print "CLIENT : UPPLOAD TRAJ"
                print "----------------------------------------------------------------------"
                tmp = trame.split('#')
                tab_prog.append(tmp[1])

            elif 'code4' in trame:
                print "----------------------------------------------------------------------"
                print "CLIENT : EXECUTION TRAJ"
                print "----------------------------------------------------------------------" 

                for elem in tab_prog :
                    print elem
                    tmp = elem.split('@')
                    mon_pode.liste_articulation[0].set_position_consigne(int(float(tmp[0])))
                    mon_pode.liste_articulation[1].set_position_consigne(int(float(tmp[1])))
                    mon_pode.liste_articulation[2].set_position_consigne(int(float(tmp[2])))
                    mon_pode.liste_articulation[3].set_position_consigne(int(float(tmp[3])))
                    mon_pode.liste_articulation[4].set_position_consigne(int(float(tmp[4])))
                    mon_pode.liste_articulation[5].set_position_consigne(int(float(tmp[5])))
                    mon_pode.liste_articulation[6].set_position_consigne(int(float(tmp[6])))
                    mon_pode.liste_articulation[7].set_position_consigne(int(float(tmp[7])))
                    mon_pode.liste_articulation[8].set_position_consigne(int(float(tmp[8])))
                    mon_pode.liste_articulation[9].set_position_consigne(int(float(tmp[9])))
                    mon_pode.liste_articulation[10].set_position_consigne(int(float(tmp[10])))
                    mon_pode.liste_articulation[11].set_position_consigne(int(float(tmp[11])))
                    mon_pode.liste_articulation[12].set_position_consigne(int(float(tmp[12])))
                    mon_pode.liste_articulation[13].set_position_consigne(int(float(tmp[13])))
                    mon_pode.liste_articulation[14].set_position_consigne(int(float(tmp[14])))
                    mon_pode.liste_articulation[15].set_position_consigne(int(float(tmp[15])))
                    mon_pode.liste_articulation[16].set_position_consigne(int(float(tmp[16])))
                    mon_pode.liste_articulation[17].set_position_consigne(int(float(tmp[17])))
                    mon_pode.evoluer()

            elif 'code5' in trame :
                print "----------------------------------------------------------------------"
                print "CLIENT : RAZ PROG"
                print "----------------------------------------------------------------------" 
                del(tab_prog[:])

    except:
        print "erreur analyse trame"

mon_pode = Hexapode()
mon_pode.initialiser()



TCP_IP = '192.168.1.21'
TCP_PORT = 12801
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    #print "received data:", data
    #conn.send(data)
    analyse(data)
conn.close()

