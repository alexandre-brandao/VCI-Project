/*
 * Tester program for the state machine exercise
 *
 * Embedded and Real-Time Systems
 * 2019-20
 * pf@ua.pt
 */

#include <stdio.h>
#include <string.h>

#include "heatingsystem.h"
#include "heatingSM.h"

/* Undefine DEMO for your submission code! */


#define TEMPERATUREDELTACOOLING 1
#define TEMPERATUREDELTAHEATING 10

void printSystemStatus(char c);
void InitScreen(void);
void SystemInit();
void systemSimulation(void);

int main(int argc, char const *argv[]) {

  bool running = true;

  SystemInit();
  InitScreen();


#ifdef DEMO
  /* This is an example of a call to setDisplay() */
  char DisplayData[17];
  strcpy(DisplayData,"0123456789ABCDEF");
  setDisplay(DisplayData);
#endif

  while (running) {
    char c;
    bool show_state = true;

    c = getchar();

    switch (c) {

      case '.':
      case ' ':
      /* simulate passing of time and run state machine */
      timeTick();
      systemSimulation();
      /* The call to your state machine implementation should be added here */
      sm_execute(&smTempControl);
      break;

      /* Interactions with system */


      /* User input handling */
      case '+':
      PlusKeyPressed = true;
      break;

      case '*':
      PlusKeyPressed = false;
      break;

      case '-':
      MinusKeyPressed =  true;
      break;

      case '_':
      MinusKeyPressed =  false;
      break;

      case 'N':
      NEXTKeyPressed = true;
      break;

      case 'n':
      NEXTKeyPressed = false;
      break;

      case 'T':
      TempKeyPressed = true;
      break;

      case 't':
      TempKeyPressed = false;
      break;

      /* Help */
      case '?':
      case 'h':
      InitScreen();
      break;

      /* Leave */
      case 'x':
      case EOF:
      running = false;
      break;

      /* Avoid displaying status line for all keys that are not relevant */
      default:
      show_state = false;
      break;
    }


    if (show_state && running) {
      printSystemStatus(c);
    }

  }
  return 0;
}

void InitScreen(void)
{
  printf("Interaction:\n\n");
  printf("+/* to press/release '+' button.\n");
  printf("-/_ to press/release '-' button.\n");
  printf("T/t to press/release TEMP button.\n");
  printf("N/n to press/release NEXT button.\n");
	printf("Space or '.' to execute the state machine and show system state.\n");
	printf("x to leave.\n");
  printf("(In the terminal, requires Enter to read the input.)\n");
	printf("----------------------------------------------------------------\n");
	printf(" : Time	: N + - T    Temp   | Display        | State \n");
	printf("----------------------------------------------------------------\n");
}

void printSystemStatus(char c)
{
  uint8_t keymap;
  char currentStateName[16];

  keymap = keyRead();

  printf("%c: ",c);
  printf("%4d : ",get_current_time());
  printf("%c ",(keymap&NEXTKEYMASK)?'N':' ');
  printf("%c ",(keymap&PLUSKEYMASK)?'+':' ');
  printf("%c ",(keymap&MINUSKEYMASK)?'-':' ');
  printf("%c ",(keymap&TEMPKEYMASK)?'T':' ');
  printf("   %4d", readTemp());
  printf("   |%16s|  ", Display);
  getCurrentStateName(smTempControl, currentStateName);
  printf("%s\n",currentStateName);
}

void SystemInit(void)
{
  smTempControl.initialstate = TemperatureSet;
  smTempControl.currentstate = smTempControl.initialstate;
}

void systemSimulation(void)
{
  if(getHeatingOn()){
    Temperature += TEMPERATUREDELTAHEATING;
  }
  else{
    if(Temperature >= TEMPERATUREDELTACOOLING){
      Temperature -= TEMPERATUREDELTACOOLING;
    }
  }
}
