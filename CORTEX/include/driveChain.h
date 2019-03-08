#ifndef DRIVECHAIN_H
#define DRIVECHAIN_H

#include "main.h"
#include "motor.h"
#include "direction.h"

class DriveChain {
public:
  Motor leftMotor;
  Motor rightMotor;

  DriveChain();
  DriveChain(int channel1, int channel2);

  void move(Direction direction, int speed);
};

#endif
