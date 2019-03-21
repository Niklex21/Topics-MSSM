void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(1, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.write(1);
  delay(1000);
  Serial.write(2);
  delay(1000);
  Serial.write(3);
  delay(1000);
  Serial.write(4);
  delay(1000);
  Serial.write(5);
  delay(1000);
}
