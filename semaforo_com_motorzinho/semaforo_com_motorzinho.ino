/*
 * Semáforo com arduino 
 * Pino 13 LED vermelho
 * Pino 12 LED amarelo
 * Pino 11 LED verde
 */

#include <Servo.h> // Inclui a biblioteca Servo para controlar o motorzinho

// #define LED_VERMELHO 13
// #define LED_AMARELO 12
// #define LED_VERDE 11
#define POTENCIOMETRO A0
#define MOTORZINHO 6

Servo motorzinho;


void setup() {
  // pinMode(LED_VERMELHO, OUTPUT);
  // pinMode(LED_AMARELO, OUTPUT);
  // pinMode(LED_VERDE, OUTPUT);
  pinMode(MOTORZINHO, OUTPUT);
  pinMode(POTENCIOMETRO, INPUT);
  
  motorzinho.attach(MOTORZINHO);
  motorzinho.write(0);
}
 

void loop() {
  int potValue = analogRead(POTENCIOMETRO);
  int servoPos = map(potValue, 0, 1023, 0, 180);
  motorzinho.write(servoPos);
  
  // digitalWrite(LED_VERDE, 0);
  // digitalWrite(LED_VERMELHO, 1);
  // delay(2000);
  
  // digitalWrite(LED_VERMELHO, 0);
  // digitalWrite(LED_AMARELO, 1);
  // delay(1000);
  
  // digitalWrite(LED_AMARELO, 0);
  // digitalWrite(LED_VERDE, 1);
  // delay(2000);
} 