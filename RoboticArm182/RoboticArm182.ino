/*
 * Robô com Arduino
 */

#include <Servo.h> // Inclui a biblioteca Servo para controlar o motorzinho

#define POTENCIOMETRO A0
#define SERVO_GARRA 3
#define SERVO_ROT 5
#define SERVO_ATAQUE 6
#define SERVO_ALTURA 9

Servo servoGarra;
Servo servoRot;
Servo servoAtaque;
Servo servoAltura;


void setup() {
  Serial.begin(9600);
  
  pinMode(POTENCIOMETRO, INPUT);
  
  servoGarra.attach(SERVO_GARRA);
  servoRot.attach(SERVO_ROT);
  servoAtaque.attach(SERVO_ATAQUE);
  servoAltura.attach(SERVO_ALTURA);

  servoGarra.write(90);
  servoRot.write(90);
  servoAtaque.write(90);
  servoAltura.write(90);
 


}


void loop() {

  if (Serial.available() >= 4) {

    int garra = Serial.read();
    int rot = Serial.read();
    int ataque = Serial.read();
    int altura = Serial.read();

    servoGarra.write(garra);
    servoRot.write(rot);
    servoAtaque.write(ataque);
    servoAltura.write(altura);

  }

  //int potValue = analogRead(POTENCIOMETRO);
  //int servoPos = map(potValue, 0, 1023, 0, 180);
  //motorzinho.write(servoPos);
} 