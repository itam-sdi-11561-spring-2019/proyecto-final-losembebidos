#include <ros.h>
#include <std_msgs/Empty.h>
#include <std_msgs/String.h>

ros::NodeHandle nh;
std_msgs::String str_msg;
String mensage = "";

void messageCb( const std_msgs::str_msg, & toggle_msg){
  digitalWrite(13, HIGH-digitalRead(13));   // blink the led
  mensage = toggle_msg;
}

ros::Subscriber<std_msgs::Empty> sub("pcPub", &messageCb );
ros::Publisher chatter("ardu", &str_msg);

unsigned char hello[] = "Hello from Node 1!";

void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(chatter);
}
/*
void loop()
{
  str_msg.data = hello;
  chatter.publish( &str_msg );
  nh.spinOnce();
  delay(1);
}
*/




#include <SoftwareSerial.h>
int TX = 50;
int RX = 51;
//SoftwareSerial xbee(RX, TX);

//Tiempo Muestreo
int tm=250 ;

//Tiempo actual
long ta=0;
//Izquierda
int pin30 = 30;
int pin32 = 32;
int pinvelI= 2;

//Derecha
int pin40 = 40;
int pin42 = 42;
int pinvelD= 3;

//Counters
int numSlotDer=0;
int numSlotIzq=0;

//Sensores de velocidad
//izq
int pin4 = 4;
//der
int pin5 = 5;

//Velocidad de las ruedas deseada
int velIzq=50;
int velDer=50;

//Velocidad de las ruedas real
int velRI=0;
int velRD=0;

//Velocidad de las ruedas entrada
int velDE=0;
int velIE=0;

double errTI;
double errTD;

double eD;
double eI;

//Direccion
int dirD=0;
int dirI=0;

double PIDIzq(double e){
 double ki;
 double kp;
 double kd;
 double u;
 double integ;
 double di;
 //double d0;
 
 ki=0.8;
 kp=2.3;
 kd=.7;
 errTI=errTI+e;
 integ=errTI;
 di=e-eI;
 eI=e;
 u=kp*e+ki*integ+kd*di;
 di=u/10;
 //Serial.println(di);
 //Serial.println(" Der ");
 //Serial.println( u);
 return u;
 }
 
 double PIDDer(double e){
 double ki;
 double kp;
 double kd;
 double u;
 double integ;
 double di;
 //double d0;
 
 ki=.9;
 kp=1.5;
 kd=.5;
 errTD=errTD+e;
 integ=errTD;
 di=e-eD;
 eD=e;
 u=kp*e+ki*integ+kd*di;
 di=u/10;
 
 
 return u;
 }
 
void setup()
{
  Serial.begin(9600);
  // xbee.begin(9600);
  //motor derecho
  pinMode(pin30, OUTPUT);
  pinMode(pin32, OUTPUT);
  pinMode(pinvelD, OUTPUT);
  //motor izquierda
  pinMode(pin40, OUTPUT);
  pinMode(pin42, OUTPUT);
  pinMode(pinvelI, OUTPUT);
  
  pinMode(pin5, INPUT);
  pinMode(pin4, INPUT);
  
  ta=millis();
  errTD = 0;
  errTI = 0;
}

byte pprI = 18 ; // slots izquierda
byte pprD=18 ;   //slots derecha

boolean eSD; //Estado actual del sensor derecho
boolean eAD; //Estado anterior del sensor derecho


boolean eSI; //Estado actual del sensor izquierdo
boolean eAI; //Estado anterior del sensor izquierdo
void calcMotorSpeedActual()
{
  //Derecha
  eSD = digitalRead(pin5);
  if ((eSD != eAD) && eSD == HIGH) //changed and HIGH means just got interrupted
  {
    numSlotDer=numSlotDer+1;
  }
   
  eAD = eSD;
  
  //Izquierda
  eSI = digitalRead(pin4);
  if ((eSI != eAI) && eSI == HIGH) //changed and HIGH means just got interrupted
  {
    numSlotIzq=numSlotIzq+1;
  }

  eAI = eSI;
}// calcMotorSpeedActual

void loop()
{


  str_msg.data = hello;
  chatter.publish( &str_msg );
  nh.spinOnce();
  delay(1);




  
  calcMotorSpeedActual();
  
  if(millis()>=ta+tm){
    velRD=(1000/tm)*numSlotDer;
    velRI=(1000/tm)*numSlotIzq;
    velDE=PIDDer(velDer-velRD);
    velIE=PIDIzq(velIzq-velRI);
    //
    //Serial.print(velDer);
    if(velDer>0 ){
        digitalWrite(pin30, HIGH);
        digitalWrite(pin32, LOW);
    
    }
    else{
      
        digitalWrite(pin30, LOW);
        digitalWrite(pin32, HIGH);
      
       
    }
    if(velIzq>0 ){
        digitalWrite(pin40, HIGH);
        digitalWrite(pin42,LOW);
    
    }
    else{
        digitalWrite(pin40, LOW);
        digitalWrite(pin42,HIGH);
    
    }
    analogWrite(pinvelD,min(abs(velDE),255));
  
    analogWrite(pinvelI,min(abs(velIE),255));



  if(mensage == "gO"){
    digitalWrite(pin30, HIGH);
    digitalWrite(pin32, LOW);
    digitalWrite(pin40, HIGH);
    digitalWrite(pin42, LOW);
  }

  if(mensage == "gD"){
    digitalWrite(pin30, HIGH);
    digitalWrite(pin32, LOW);
    digitalWrite(pin40, LOW);
    digitalWrite(pin42, HIGH);
  }

  if(mensage == "gI"){
    digitalWrite(pin30, LOW);
    digitalWrite(pin32, HIGH);
    digitalWrite(pin40, HIGH);
    digitalWrite(pin42, LOW);
  }

  



    
    ta=millis();
    numSlotIzq=0;   
    numSlotDer=0;
  }
  
  //if(xbee.available()>0){
   //   velDer=xbee.read();
    //  Serial.println(velDer);
    //  dirD=xbee.read()==0?1:-1;
      
    //  velIzq=(int)xbee.read();
    //  dirI=xbee.read()==0?1:-1;
      
    //  velDer=(int(velDer))*dirD;
    //  velIzq=velIzq*dirI;
      
  
      //Serial.println(velDer);
      //Serial.println(velIzq);
  //}
}

























