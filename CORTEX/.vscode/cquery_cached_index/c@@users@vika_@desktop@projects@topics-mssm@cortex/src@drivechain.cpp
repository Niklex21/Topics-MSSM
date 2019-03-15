#include "main.h"
#include "driveChain.h"
#include "direction.h"

DriveChain::DriveChain(int channel1, int channel2) {
  leftMotor = Motor(channel1);
  rightMotor = Motor(channel2);
}

void DriveChain::move(Direction direction, int speed) {
  switch (direction) {
    case left:
      this->leftMotor.move(-speed);
      this->rightMotor.move(speed);
      break;
    case right:
      this->leftMotor.move(speed);
      this->rightMotor.move(-speed);
      break;
    case forward:
      this->leftMotor.move(speed);
      this->rightMotor.move(speed);
      break;
    case back:
      this->leftMotor.move(-speed);
      this->rightMotor.move(-speed);
      break;
    default:
      this->leftMotor.move(0);
      this->rightMotor.move(0);
      break;
  }
}
