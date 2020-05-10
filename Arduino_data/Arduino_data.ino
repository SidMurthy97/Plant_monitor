#include <dht.h>

const int DHT_pin = A0;
const int soil_moisture_pin = A1;
const int soil_moisture_trigger = 8;
int soil_moisture = 0;

unsigned long ms_per_s = 1000L;
unsigned long minutes = 30;
unsigned long sampling_time = minutes * ms_per_s * 60;

int dht_sig = 0;
int soil_moisture_sig = 0;
dht DHT;


void setup() {
  pinMode(soil_moisture_pin,INPUT);
  pinMode(soil_moisture_trigger,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  dht_sig = DHT.read11(DHT_pin);
  
//  digitalWrite(soil_moisture_trigger,HIGH);
//  delay(10);
//  soil_moisture_sig = analogRead(soil_moisture_pin);
//  digitalWrite(soil_moisture_trigger,LOW);
//  soil_moisture = map(soil_moisture_sig,168,0,0,100);
  
  Serial.print(DHT.temperature);
  Serial.print(DHT.humidity);
  Serial.print(soil_moisture);
  delay(3000);
}
