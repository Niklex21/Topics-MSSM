#include "main.h"
#include "motor.h"

Motor::Motor(int channel_) {
  this->channel = channel_;
}

void Motor::move(int speed) {
  motorSet(this->channel, speed);
}
