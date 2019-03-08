#include "main.h"
#include "driveChain.h"
#include "motor.h"

void driveChain::turnLeft(int speed) {
  leftMotor.move(-speed);
  rightMotor.move(speed);
}

void driveChain::turnRight(int speed) {
  leftMotor.move(speed);
  rightMotor.move(-speed);
}

void driveChain::driveFwd(int speed) {
  leftMotor.move(speed);
  rightMotor.move(speed);
}

void driveChain::driveBack(int speed) {
  leftMotor.move(-speed);
  rightMotor.move(-speed);
}
