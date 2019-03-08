#include "main.h"
#include "robot.h"

void Robot::move(Direction direction, int speed) {
  this->driveChain.move(direction, speed);
}
