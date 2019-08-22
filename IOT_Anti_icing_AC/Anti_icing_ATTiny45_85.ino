#include<DHT.h>
#include <SoftwareSerial.h>
#define DHTPIN 2
#define DHTTYPE DHT11
#define lm35 A3
#define relay 4
SoftwareSerial mySerial(0, 1);
int acstatus=1;
char manoverride='0';
DHT dht(DHTPIN,DHTTYPE);
int  actemp,t,h;

void setup(){
   mySerial.begin(9600);
   mySerial.println("MICROProject\n");
pinMode(relay,OUTPUT);
//pinMode(lm35,INPUT);
//Serial.begin(9600);
dht.begin();
}

void loop(){
 if(mySerial.available()>0)
  {
    manoverride=mySerial.read();
    }
 actemp= (analogRead(lm35)/1024.0)*5.0*100.0; //analog read and then conversion of the value to degree C
 h=dht.readHumidity();
t=dht.readTemperature();
if(isnan(h)||isnan(t))
{
  return;
}
String a="";
a+=t;
a+=',';
a+=actemp;
/*a+=',';
a+=h;
a+=',';
a+=acstatus;*/
a+=';';
mySerial.print(a);
mySerial.print("\n");
if(manoverride=='0')
{
  if(t>22.0&&actemp>5.0)
    {
      digitalWrite(relay,HIGH);
      acstatus=1;
      return;
    }
 else
    {
      digitalWrite(relay,LOW);
      acstatus=0;
    }

}
else if(manoverride=='1'||actemp<5.0)
{
  digitalWrite(relay,LOW);
  acstatus=0;
  return;
  }
  
}
