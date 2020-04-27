#include <dht.h>


const int DHT_pin = A0;
int dht_sig = 0;
dht DHT;


void setup() {

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  dht_sig = DHT.read11(DHT_pin);
 
  Serial.println(DHT.temperature);
  delay(1000);
}
