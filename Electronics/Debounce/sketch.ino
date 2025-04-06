const int ledPin = 10;
const int inputPin =2;
const int bouncedelay =10;

boolean debounce(int pin)
{
  boolean state;
  boolean prevstate;
prevstate = digitalRead(pin);
for(int count=0; count<bouncedelay; count++)
{
  delay(10);
  state =  digitalRead(pin);
  if(state!=prevstate)
  {
    count =0;
    prevstate = state;
  }
}
return state;

}

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(inputPin, INPUT);
  // put your setup code here, to run once:

}

void loop() {
  if(debounce(inputPin) == true)
  {
    digitalWrite(ledPin, HIGH);
  }
  else{
    digitalWrite(ledPin, LOW);
  }
  // put your main code here, to run repeatedly:

}
