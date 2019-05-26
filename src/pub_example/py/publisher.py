#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Pose2D
from graphical_client.msg import Pose2D_Array
import numpy as np
import math

#import std_msgs.msg
#std_msgs = std_msgs.msg.String()
#include <std_msgs/String.h>
from std_msgs.msg import String
msg = String
_x = []
_y = []
_theta = []

_pwmI_ardu = []
_pwmD_ardu = []


bool inicial = False
_ini = []

def callbackObs0(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard x:%s", data.x)
    rospy.loginfo(rospy.get_caller_id() + "I heard y:%s", data.y)
    rospy.loginfo(rospy.get_caller_id() + "I heard theta:%s", data.theta)
    
    _x[0] = data.x
    _y[0] = data.y
    _theta[0] = data.theta

def callbackObs1(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard x:%s", data.x)
    rospy.loginfo(rospy.get_caller_id() + "I heard y:%s", data.y)
    rospy.loginfo(rospy.get_caller_id() + "I heard theta:%s", data.theta)
    
    _x[1] = data.x
    _y[1] = data.y
    _theta[1] = data.theta

def callbackObs2(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard x:%s", data.x)
    rospy.loginfo(rospy.get_caller_id() + "I heard y:%s", data.y)
    rospy.loginfo(rospy.get_caller_id() + "I heard theta:%s", data.theta)
    
    _x[2] = data.x
    _y[2] = data.y
    _theta[2] = data.theta

def callbackObs3(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard x:%s", data.x)
    rospy.loginfo(rospy.get_caller_id() + "I heard y:%s", data.y)
    rospy.loginfo(rospy.get_caller_id() + "I heard theta:%s", data.theta)
    
    _x[3] = data.x
    _y[3] = data.y
    _theta[3] = data.theta

def callbackObs4(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard x:%s", data.x)
    rospy.loginfo(rospy.get_caller_id() + "I heard y:%s", data.y)
    rospy.loginfo(rospy.get_caller_id() + "I heard theta:%s", data.theta)
    
    _x[4] = data.x
    _y[4] = data.y
    _theta[4] = data.theta

def callbackObs5(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard x:%s", data.x)
    rospy.loginfo(rospy.get_caller_id() + "I heard y:%s", data.y)
    rospy.loginfo(rospy.get_caller_id() + "I heard theta:%s", data.theta)
    
    _x[5] = data.x
    _y[5] = data.y
    _theta[5] = data.theta

def callbackObs6(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard x:%s", data.x)
    rospy.loginfo(rospy.get_caller_id() + "I heard y:%s", data.y)
    rospy.loginfo(rospy.get_caller_id() + "I heard theta:%s", data.theta)
    
    _x[6] = data.x
    _y[6] = data.y
    _theta[6] = data.theta

def callbackObs7(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard x:%s", data.x)
    rospy.loginfo(rospy.get_caller_id() + "I heard y:%s", data.y)
    rospy.loginfo(rospy.get_caller_id() + "I heard theta:%s", data.theta)
    
    _x[7] = data.x
    _y[7] = data.y
    _theta[7] = data.theta

def callbackBall(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard x:%s", data.x)
    rospy.loginfo(rospy.get_caller_id() + "I heard y:%s", data.y)
    rospy.loginfo(rospy.get_caller_id() + "I heard theta:%s", data.theta)
    
    _x[8] = data.x
    _y[8] = data.y
    _theta[8] = data.theta

def callbackChancla(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard x:%s", data.x)
    rospy.loginfo(rospy.get_caller_id() + "I heard y:%s", data.y)
    rospy.loginfo(rospy.get_caller_id() + "I heard theta:%s", data.theta)
    
    _x[9] = data.x
    _y[9] = data.y
    _theta[9] = data.theta

def callbackArdu(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard x:%s", data.x)
    rospy.loginfo(rospy.get_caller_id() + "I heard y:%s", data.y)
    rospy.loginfo(rospy.get_caller_id() + "I heard theta:%s", data.theta)

    _x_ardu = _x_ardu + [data.x]
    _y_ardu = _y_ardu + [data.y]
    _theta_ardu = _theta_ardu + [data.theta]
    print("la data es:")
    print(_x_ardu)
    print(_y_ardu)
    print(_theta_ardu)


    if(!inicial):
        _ini = [[_x_ardu,_y_ardu]]
        inicial = !inicial




def init_pose():
    pose = Pose2D()
    pose.x = 0
    pose.y = 0
    pose.theta = 0
    return pose

def talker():
    pub = rospy.Publisher('/trajectory', Pose2D_Array, queue_size=10)
    pc = rospy.Publisher('pcPub', msg, queue_size=10)
    rospy.init_node('pc', anonymous=True)
    rospy.Subscriber("/b_r0", Pose2D, callbackBall)
    rospy.Subscriber("/b_r1", Pose2D, callbackObs0)
    rospy.Subscriber("/b_r2", Pose2D, callbackObs1)
    rospy.Subscriber("/b_r3", Pose2D, callbackObs2)
    rospy.Subscriber("/b_r4", Pose2D, callbackObs3)
    rospy.Subscriber("/b_r5", Pose2D, callbackObs4)
    rospy.Subscriber("/b_r6", Pose2D, callbackObs5)
    rospy.Subscriber("/b_r7", Pose2D, callbackObs6)
    rospy.Subscriber("/ball", Pose2D, callbackObs7)
    rospy.Subscriber("/y_r0", Pose2D, callbackChancla)
    rospy.Subscriber("ardu", msg, callbackArdu)



    rate = rospy.Rate(1) # 10hz
    aux = 1
    while not rospy.is_shutdown():
        arr = Pose2D_Array()
        for i in range(10):
            pose = init_pose()
            pose.x = 100 * ( i + 1 ) 
            pose.y = 150 * ( i + 1 ) * aux
            pose.theta +=0.7853 * i
            arr.poses.append(pose)
            aux *= -1
        print "The array is:", arr
        pub.publish(arr)
        #pub.publish(callback)
        # hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        # pub.publish(hello_str)
        rate.sleep()
	rospy.spin()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass






def rutaFacil():
    thetaChancla = _theta[9]
    xChancla = _x[9]
    yChancla = _y[9]
    xPelota = _x[8]
    yPelota = _y[8]
    anguloPelota = math.atan((yPelota-yChancla)/(xPelota-xChancla))*180/math.pi

    while(anguloPelota!= thetaChancla):
        if(anguloPelota!= thetaChancla):
            pc.publish("gD")
        else:
            pc.publish("gI")
    while(xChancla != xPelota and yChancla != yPelota):
        pc.publish("gO")



import math 

def calculaObstaculos(ini,fin,Obs, numObs):
    circulosN = []
    m = (fin[1]-ini[1])/(fin[0]-fin[0])
    b = ini[1]-m*ini[0]
    numInter = 0
    circulosN[0] = 0

    for i in range(0,numObs):
        d = abs(Obs[i][1]-m*(Obs[i][0])-b)/sqrt(m**2+1)
        #d2=abs(ini(1)-fin(1))-max(abs([ini(1)-(Obs(i,1)+4),fin(1)-(Obs(i,1)+4)]));
        d2 = abs(ini[0]-fin[0])-max(abs((ini[0]-(Obs[i][0]+4),fin[0]-(Obs[i][0]+4))))
        #d3=abs(ini(2)-fin(2))-max(abs([ini(2)-(Obs(i,2)+4),fin(2)-(Obs(i,2)+4)]));
        d3 = abs(ini[1]-fin[1])-max(abs((ini[1]-(Obs[i][2]+4),fin[1]-(Obs[i][2]+4))))

        if (d2>0 and d3>0 and d<40):
            numInter=numInter+1;
            #Arreglo que nos indica cuáles círculos del arreglo interfieren con la ruta
            circuloN[numInter]=i

    if(circuloN[0] == 0):
        d = (Obs[circuloN[0]][0]-ini[0])**2 + (Obs[circuloN[0]][1]-ini[1])**2
    for i in range(1,numInter):
        dn = (Obs[circuloN[i]][0]-ini[0])**2+(Obs[circuloN[i],[1]]-ini[1])**2
        if(dn<d):
            d = dn
            circuloN[0] = circuloN[i]

    return circulosN
    

def calculaRuta(ini,fin,Obs):

    #rutaIn=[linspace(ini(1),fin(1),100);
    #linspace(ini(2),fin(2),100);
    #ones(1,100).*atan((fin(2)-ini(2))/(fin(1)-ini(1)))]';

    numObs = len(Obs)
    m = (fin[1]-ini[1])/(fin[0]-fin[0])
    circuloN = calculaObstaculos(ini,fin,Obs, numObs)
    #Vector con los puntos a los que debe llegar
    numPuntos=1
    if(circuloN[0]==0):
        numInter = 0
    else:
        numInter = len(circuloN)

    #puntos(1,:)=[ini,atan(m)];
    puntos[0] = ini + [math.atan(m)]
    

    i=1;
    r=16;
    #figure(3)
    #visualizacion(ini,fin,Obs,rutaIn,circuloN);
    #grid on;
    #figure(1)
    numI = 1;
    while(numInter>=1 and numI <200):
        #p1=[r*sin(puntos(numPuntos,3)-pi)+Obs(circuloN(i),1),r*cos(puntos(numPuntos,3))+Obs(circuloN(i),2)];
        p1 = [r*math.sin(puntos[numPuntos][3]-math.pi)+Obs[circuloN[i][1]], r*math.cos(puntos[numPuntos][3] + Obs[circuloN[i][2]])]
        #p2=[-r*sin(puntos(numPuntos,3)+pi)+Obs(circuloN(i),1),-r*cos(puntos(numPuntos,3))+Obs(circuloN(i),2)];
        p2 = [(-1)*r*math.sin(puntos[numPuntos][3]+math.pi)+Obs[circuloN[i][1]], (-1)*r*math.cos(puntos[numPuntos][3] + Obs[circuloN[i][2]])]
        cipi=calculaObstaculos(ini,p1,Obs,numObs)
        if(cipi[0]<numInter or cipi[0]==0):
            numPuntos=1+numPuntos
            #puntos(numPuntos,:)=[p1,atan(((p1(2)-ini(2))/(p1(1)-ini(1))))];
            puntos[numPuntos] = p1 + [math.atan((p1[1]-ini[1]/(p1[0]-ini[0])))]

            ini=p1
            circuloN=calculaObstaculos(ini,fin,Obs,numObs)
            r=r+4
        else:
            cipi=calculaObstaculos(ini,p2,Obs,numObs)
            if(cipi[0]<numInter or cipi[0]==0):
                numPuntos=1+numPuntos
                #puntos(numPuntos,:)=[p2,atan(((p2(2)-ini(2))/(p2(1)-ini(1))))];
                puntos[numPuntos] = p2 + [math.atan((p2[1]-ini[1]/(p2[0]-ini[0])))]

                ini=p2
                circuloN=calculaObstaculos(ini,fin,Obs,numObs)
                r=r+4
            else:
                r=r+32
            if(circuloN(1)==0):
                numInter=0
            else:
                numInter=length(circuloN)
            numI=numI+1
        #puntos(numPuntos+1,:)=[fin,atan((fin(2)-ini(2))/(fin(1)-ini(1)))];
        puntos[numPuntos] = fin + [math.atan((fin[1]-ini[1]/(fin[0]-ini[0])))]


    ruta=puntos
    return ruta











