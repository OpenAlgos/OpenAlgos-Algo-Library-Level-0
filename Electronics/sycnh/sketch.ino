const int leds[] = {2, 3, 4, 5};
const int sensor = A0;

void setup() {
  for (int i = 0; i < 4; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

void loop() {
  int rate = analogRead(sensor);
  rate = constrain(rate, 100, 800); // optional: keep it fun speed

  for (int i = 0; i < 4; i++) {
    digitalWrite(leds[i], HIGH);
    delay(rate);
    digitalWrite(leds[i], LOW);
  }
}
