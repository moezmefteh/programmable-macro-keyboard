//#include <configuration.h>
#include <Keypad.h>
#include <HIDKeyboard.h>

HIDKeyboard keyboard; 

//Keypad Inputs
const byte ROWS = 2; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  };
byte rowPins[ROWS] = {3, 4}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {5, 6, 7}; //connect to the column pinouts of the keypad
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

// Rotary Encoder Inputs
#define Clock 9   //Clock pin connected to D9
#define Data 8    //Data pin connected to D8
#define Push 10   //Push button pin connected to D10

int counter = 0;                    //Use this variable to store "steps"
int currentStateClock;              //Store the status of the clock pin (HIGH or LOW)
int lastStateClock;                 //Store the PREVIOUS status of the clock pin (HIGH or LOW)
String currentDir ="";              //Use this to print text 
unsigned long lastButtonPress = 0;  //Use this to store if the push button was pressed or not




//-----------------------------------------------------------------------------------------------------------------------------
void setup(){
  Serial.begin(9600);
  keyboard.begin();
  pinMode(Clock,INPUT_PULLUP);
  pinMode(Data,INPUT_PULLUP);
  pinMode(Push, INPUT_PULLUP);
  lastStateClock = digitalRead(Clock);
//  parser( first, second,third );
}
//-----------------------------------------------------------------------------------------------------------------------------
/*int nb_occ(char keyConfig[])
{
  int i, occ = 0;
   for(i = 0; sizeof(keyConfig)/sizeof(keyConfig[0]); ++i)
   {
       if(keyConfig[i] == '+')
           ++occ;
   }
   return occ;}*/

//-----------------------------------------------------------------------------------------------------------------
 /*void splitKeyConfig1(char keyConfig[],uint8_t* first ,uint8_t* second)
{char parsedString[10][2];
  char* piece =strtok(keyConfig,"+");
  strncpy(parsedString[0] ,piece,sizeof(parsedString));
  *first=(uint8_t)(parsedString[0]);
  piece=strtok(NULL,"+");
  strncpy(parsedString[1] ,piece,sizeof(parsedString));
  *first=(uint8_t)(parsedString[1])};*/

//---------------------------------------------------------------------------------------------------------
/*void parser(uint8_t* first,uint8_t* second ){
    if (nb_occ(key1)==0)
    
      {first=key1;}
        else if (nb_occ(key1)==1)
          {splitKeyConfig1(key1, &first , &second);}
          //else if (nb_occ(key1)==2)
              //{splitKeyConfig2(key1, &first , &second,&third);}*/
//---------------------------------------------------------------------------------------------------
void keyPressTypeVerif(uint8_t first,uint8_t second ,uint8_t third,int token)
{switch (token){
                      case 0 :{if (first>=0x28 and first<=0x52) keyboard.pressSpecialKey(first);
                                    else keyboard.pressKey(first);break;}
                      case 1 :{if (second >=0x28 and second<=0x52)  keyboard.pressSpecialKey(first,second);
                                    else keyboard.pressKey (first,second);break;}
                      case 2 :{if (third >=0x28 and third <=0x52) keyboard.pressSpecialKey((first | second),third);
                                    else keyboard.pressKey ((first | second),third);break;}}}


void loop(){
    
MacroKeyBoard();
RotaryEncoder();

  
}
void MacroKeyBoard(){
    char key = keypad.getKey();


  if (key ){
   
      switch (key) {
      case '1': keyPressTypeVerif(first_1,second_1,third_1,token_1);  
  break;
      case '2': keyPressTypeVerif(first_2,second_2,third_2,token_2);    
  break;
      case '3': keyPressTypeVerif(first_3,second_3,third_3,token_3);     
  break;
      case '4': keyboard.pressKey((ctrl | SHIFT), 'N');    
  break;
      case '5': keyboard.pressKey((ctrl | SHIFT), 'N');    
  break;
      case '6': keyboard.pressKey((ctrl | SHIFT), 'N');
  break;

    }
    delay(100);
    keyboard.releaseKey();
   
  }

}


void RotaryEncoder(){
    currentStateClock = digitalRead(Clock);

  if (currentStateClock != lastStateClock  && currentStateClock == 1){

    if (digitalRead(Data) != currentStateClock) {
      counter --;
      currentDir ="Counterclockwise";
      keyboard.pressSpecialKey(ctrl,KEYPADMINUS);
      keyboard.releaseKey();
    } else {
      counter ++;
      currentDir ="Clockwise";
      keyboard.pressSpecialKey(ctrl,KEYPADPLUS);
      keyboard.releaseKey();
    }
  }
  lastStateClock = currentStateClock;

  int btnState = digitalRead(Push);

  if (btnState == LOW) {
    //if 50ms have passed since last LOW pulse, it means that the
    //button has been pressed, released and pressed again
    if (millis() - lastButtonPress > 50) {
      keyboard.pressKey(VOLUMEMUTE);
      keyboard.releaseKey();
    }
    lastButtonPress = millis();
  }
  delay(1);}


 /*void splitKeyConfig2(char keyConfig[],uint8_t* first,uint8_t* second,uint8_t* third  )
{
  char* piece =strtok(keyConfig,"+");
  *first  = atoi (piece.substring(1, 3).c_str ());  
  //*first=piece;
  piece=strtok(NULL,"+");
    *second  = atoi (piece.substring(1, 3).c_str ());  
  //*second=uint8_t(piece);
  piece=strtok(NULL,"+");
    *third  = atoi (piece.substring(1, 3).c_str ());  

  //*third=uint8_t(piece);
  
  
}*/

  
