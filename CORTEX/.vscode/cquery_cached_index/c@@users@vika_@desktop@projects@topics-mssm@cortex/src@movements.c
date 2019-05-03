#include "main.h"
#include "movements.h"
#include "constants.h"

void turnRight(int speed) {
  motorSet(rightMotor, -speed);
  motorSet(leftMotor, speed);
}
void turnLeft(int speed) {
  motorSet(rightMotor, speed);
  motorSet(leftMotor, -speed);
}
void moveForward(int speed) {
  motorSet(rightMotor, speed);
  motorSet(leftMotor, speed);
}
void moveBack(int speed) {
  motorSet(rightMotor, -speed);
  motorSet(leftMotor, -speed);
}
