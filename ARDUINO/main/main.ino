void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(1, OUTPUT);
  pinMode(0, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  Serial.println("f");
  delay(1000);
}
