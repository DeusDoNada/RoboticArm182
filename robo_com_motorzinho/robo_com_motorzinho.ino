/*
 * Robô com Arduino
 */

#include <Servo.h> // Inclui a biblioteca Servo para controlar o motorzinho

#define POTENCIOMETRO A0
#define MOTORZINHO 6

Servo motorzinho;


void setup() {
  pinMode(MOTORZINHO, OUTPUT);
  pinMode(POTENCIOMETRO, INPUT);
  
  motorzinho.attach(MOTORZINHO);
  motorzinho.write(0);
}
 

void loop() {
  int potValue = analogRead(POTENCIOMETRO);
  int servoPos = map(potValue, 0, 1023, 0, 180);
  motorzinho.write(servoPos);
} 