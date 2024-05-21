// LIBRERY   
#include <LiquidCrystal_I2C.h>
#include <IRremote.h>  //version  :
// PIN OUTPUT AND INPUT 
#define RECV_PIN  11
#define bt_next  4
#define bt_back 6
#define bt_ok 2
#define OUT_PI  13 
// REMOTE CONTROL SETUP BUTTON HEX(DEFAULT =  EELEGOO REMOTE CONTROL )
#define B0 0xFF6897
#define B1 0xFF30CF
#define B2 0xFF18E7
#define B3 0xFF7A85
#define B4 0xFF10EF
#define B5 0xFF38C7
#define B6 0xFF5AA5
#define B7 0xFF42BD
#define B8 0xFF4AB5
#define VOL0 0xFFA857  // VOL -
#define VOL1 0xFF629D  // VOL + 

int val_up;
int val_ok;
int PI_Val = 0 ;

// INIT IR
IRrecv irrecv(RECV_PIN);
decode_results results;
// PIN BUZZER 
const int buzzer = 3;
// DISPLAY CONFIGURE
LiquidCrystal_I2C lcd(0x27,16,2);


void setup() {
  lcd.init();
  lcd.clear();
  lcd.backlight();
  lcd.setCursor(3,0);
  lcd.print("WELCOME");
  lcd.setCursor(0,1);
  lcd.print("ver:0.1-RED");

  Serial.begin(9600);

  pinMode(bt_next,INPUT_PULLUP);
  pinMode(bt_back,INPUT_PULLUP);
  pinMode(bt_ok,INPUT_PULLUP);
  pinMode(OUT_PI,OUTPUT);
  pinMode(buzzer,OUTPUT);
  irrecv.enableIRIn();
  pinMode(7,OUTPUT);

}
void func1(){
    Serial.println('3');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("F1");
    lcd.setCursor(0,1);
    val_up = 0;
    setup();
}
void func2(){
    Serial.println('4');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("F2");
    lcd.setCursor(0,1);
    val_up = 0;
    setup();
}
void func3(){
    Serial.println('5');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("F3");
    lcd.setCursor(0,1);
    val_up = 0;
}
void func4(){
    Serial.println('6');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("F4");
    lcd.setCursor(0,1);
    val_up = 0;

}


void func5(){
    Serial.println('7');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("F5");
    lcd.setCursor(0,1);
    val_up = 0;
}
void func6(){
    Serial.println('9');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("F6");
    lcd.setCursor(0,1);
    val_up = 0;

}
void func7(){
    Serial.println('3');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("F7");
    lcd.setCursor(0,1);
    val_up = 0;

}
void IP(){

    Serial.println('0');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("IP IS:");
    lcd.setCursor(0,1);
    lcd.print(Serial.readString());
    val_up = 0;
   
}
void HOST(){
    Serial.println('1');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("HOST IS:");
    lcd.setCursor(0,1);
    lcd.print(Serial.readString());
    val_up = 0;

}
void SYS_REBOOT(){
    Serial.println('2');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("SYS REBOOT:");
    lcd.setCursor(0,1);
    lcd.print(Serial.readString());
    val_up = 0;
}
void CLOSE(){
 
    Serial.println('e');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("SOFT REBOOT:");
    lcd.setCursor(0,1);
    lcd.print(Serial.readString());
    val_up = 0;
}
void CPU_FREQ(){
    Serial.println('f');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("CPU-FREQ:");
    lcd.setCursor(0,1);
    lcd.print(Serial.readString());
    val_up = 0;
}
void CPU_PERC(){
    Serial.println('p');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("CPU-PERC:");
    lcd.setCursor(0,1);
    lcd.print(Serial.readString());
    val_up = 0;
}

void CPU_COUNT(){
    Serial.println('c');
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("CPU-COUNT:");
    lcd.setCursor(0,1);
    lcd.print(Serial.readString());
    val_up = 0;
}

void Pi_on(){    // Rasberry Pi on and off 
          
  PI_Val = 1;
  if(PI_Val == 1 ){
    
    digitalWrite(OUT_PI,HIGH);
        
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("ON");
    val_up = 0;
    


  }
  else{
    
    digitalWrite(OUT_PI,LOW);
            
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("OFF");
    val_up = 0;
  }

}
void Pi_off(){
          
  PI_Val = 0;
  if(PI_Val == 0 ){
   
    digitalWrite(OUT_PI,LOW);
        
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("OFF");
    val_up = 0;
    


  }
  else{
   
    digitalWrite(OUT_PI,LOW);
            
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("OFF");
    val_up = 0;
  }

}

void loop() {
   if (irrecv.decode(&results)){
          
        
          if(results.value == B0 ){
      
           IP();
          }

          if(results.value == B1 ){
            HOST();
          }
          if(results.value == B2  ){
             SYS_REBOOT();
  
          }

          if(results.value == B3 ){
             Serial.println('3');
             lcd.clear();
             lcd.setCursor(3,0);

             lcd.print(Serial.readString());
  
          }
        
          
          if(results.value == B4){
            Serial.println('4');
            lcd.clear();
            lcd.setCursor(3, 0);
            lcd.print("");
          }
          if(results.value ==B5){
            Serial.println('5');
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("Start Visual code");
          }
          if(results.value == B6){
            Serial.println('6');
            lcd.clear();
            lcd.setCursor(3, 0);
            lcd.print("Start Game");
          }
          if(results.value == VOL1){
       
            Serial.println('+');
            lcd.clear();
            lcd.setCursor(0, 0);
            
            lcd.print(Serial.readString());
            if(Serial.readString()== "STOP"){
               digitalWrite(buzzer,HIGH);
                delay(900);
                digitalWrite(buzzer,LOW);
                delay(900);

            }
          
          }
          if(results.value == VOL0){
       
            Serial.println('-');
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print(Serial.readString());
            if(Serial.readString()== "STOP"){
              digitalWrite(buzzer,HIGH);
              delay(900);
              digitalWrite(buzzer,LOW);
              delay(900);

            }
         
          }
          if (results.value == B7){
            Serial.println('7');
          }
          if (results.value == B8){
            Serial.println('8');
            delay(900);
            lcd.clear();
            lcd.setCursor(0,0);
            lcd.print(Serial.readString());
          }
          IrReceiver.resume();
    }
  if(digitalRead(bt_next) == 0){

    delay(500);
    val_up = val_up+1 ;
    if(val_up>16){
      val_up = 0;
      setup() ;
    }

   }
  if(digitalRead(bt_back) == 0){
    delay(500);
    val_up = val_up -1;
    if (val_up < 1 ){
      
       val_up = 0;
       setup();
    }

   }
  if(digitalRead(bt_ok)==0){
  
    if (val_ok == 1){
      IP();
    }
    if(val_ok == 2){
      HOST();
    }
    if(val_ok == 3){
      SYS_REBOOT();
    }
    if(val_ok == 4){
      CLOSE();
    }
    if(val_ok ==5){
      CPU_COUNT();
    }
    if(val_ok ==6){
      CPU_FREQ();
    }
    if(val_ok ==7){
      CPU_PERC();
    }
    if(val_ok == 8){
      Pi_on();
    }
    
    if(val_ok == 9){
      Pi_off();
    }
  // function command       
    if(val_ok == 10){
      func1();
    }
        
    if(val_ok == 11){
      func2();
    }
        
    if(val_ok == 12){
      func3();
    }
        
    if(val_ok == 13){
      func4();
    }
            
    if(val_ok == 14){
      func5();
    }
        
    if(val_ok == 15){
      func6();
    }
        
    if(val_ok == 16){
      func7();
    }

   
    




  }

  if (val_up == 1){
    delay(100);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("IP INFO [OK]");
    val_ok =1;
    
    

  }
  if (val_up == 2){
    delay(100);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("HOST INFO [OK]");
    val_ok =2;
    

  }
  if (val_up == 3){
    delay(100);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("REBOOTSYS [OK]");
    val_ok =3;
    

  }
  if (val_up == 4){
    delay(100);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("EXIT SOFT [OK]");
    val_ok =4;
    

  }
  if(val_up == 5 ){
    delay(100);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("CPU-COUNT [OK]");
    val_ok=5;
  }
    if(val_up == 6 ){
    delay(100);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("CPU-FREQ [OK]");
    val_ok=6;
  }
    if(val_up == 7 ){
    delay(100);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("CPU-PERCENT [OK]");
    val_ok=7;
  }
  if(val_up == 8){
    delay(100);        
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("RASBERRY ON  [OK]");
    val_ok = 8;
  }

  if(val_up == 9){
    delay(100);        
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("RASBERRY OFF [OK]");
    val_ok = 9;
  }
  if(val_up == 10){
    delay(100);        
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Function1   [OK]");
    val_ok = 10;
  }
  
  if(val_up == 11){
    delay(100);        
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Function2   [OK]");
    val_ok = 11;
  }
  if(val_up == 12){
    delay(100);        
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Function3   [OK]");
    val_ok = 12;
  }
  if(val_up == 13){
    delay(100);        
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Function4   [OK]");
    val_ok = 13;
  }
    
  if(val_up == 14){
    delay(100);        
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Function5   [OK]");
    val_ok = 14;
  }
  if(val_up == 15){
    delay(100);        
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Function6   [OK]");
    val_ok = 15;
  }
  if(val_up == 16){
    delay(100);        
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Function7   [OK]");
    val_ok = 16;
  }
    

}