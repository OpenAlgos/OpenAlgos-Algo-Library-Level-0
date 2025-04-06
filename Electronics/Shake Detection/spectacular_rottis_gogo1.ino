const int ip = 2;
const int led1 = 5;
int prevvalue = 0;
int currentvalue = 0;
long lastmove = millis();
int shaketime = 50;

void setup() {
 pinMode(ip, INPUT_PULLUP);
 
  
  pinMode(led1, OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
  currentvalue = digitalRead(ip);
  if(currentvalue != prevvalue) 
  {
    lastmove = millis();
    prevvalue = currentvalue;
    
  }
  if(millis() - lastmove < shaketime)
  {
    digitalWrite(led1,HIGH);
  }
  else
  {
    digitalWrite(led1,LOW);
  }
  // put your main code here, to run repeatedly:

}
