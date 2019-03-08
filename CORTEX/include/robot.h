#ifndef ROBOT_H
#define ROBOT_H

#include "main.h"
#include "driveChain.h"
#include "direction.h"

class Robot {
public:
  Robot();
  DriveChain driveChain = DriveChain(1, 2);

  void move(Direction direction, int speed);
};

#endif
