#ifndef MOTOR_H
#define MOTOR_H

#include "main.h"

class Motor {
private:
  int channel;
public:
  // Constructors
  Motor();
  Motor(int channel_);

  // Functions
  void move(int speed);
};

#endif
