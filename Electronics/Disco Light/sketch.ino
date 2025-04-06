const int led1 = 2;
const int led2 = 3;
const int led3 = 4;
const int led4 = 5;
const int sensor = A0;

void setup() {
  pinMode(led1, OUTPUT);
   pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
     pinMode(led4, OUTPUT);
  pinMode(sensor, INPUT);
  // put your setup code here, to run once:

}

void loop() {
  int rate = analogRead(sensor);
  digitalWrite(led1, HIGH);
   digitalWrite(led2, LOW);
    digitalWrite(led3, HIGH);
     digitalWrite(led4, LOW);
  delay(rate);
  digitalWrite(led1, LOW);
  digitalWrite(led2, HIGH);
  digitalWrite(led3, LOW);
  digitalWrite(led4, HIGH);
  delay(rate);
  // put your main code here, to run repeatedly:

}
