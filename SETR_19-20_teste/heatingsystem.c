#include "heatingsystem.h"
#include <string.h>

uint16_t timeElapsed;

/* User keys */
bool NEXTKeyPressed = false;
bool PlusKeyPressed = false;
bool MinusKeyPressed = false;
bool TempKeyPressed = false;

/* Heating */
bool HeatingOn = false;

/* Temperature */
uint16_t Temperature = 200;

/* Storage area for the display */
char Display[16]="                ";

/*
 * readTemp()
 *
 * readTemp() returns the process temperature in tenths of degree Celsius
 */
uint16_t readTemp(void)
{
  return Temperature;
}

/*
 * getHeatingOn()
 *
 * Returns the status of the heating element (true == "heating is on")
 */
bool getHeatingOn(void)
{
  return HeatingOn;
}

/*
 * keyRead()
 *
 * Returns the key presses as a bitmap
 */
uint8_t keyRead(void)
{
  uint8_t keyMap = 0;

  if (TempKeyPressed){
    keyMap |= TEMPKEYMASK;
  }

  if (MinusKeyPressed){
    keyMap |= MINUSKEYMASK;
  }

  if (PlusKeyPressed){
    keyMap |= PLUSKEYMASK;
  }

  if( NEXTKeyPressed){
    keyMap |= NEXTKEYMASK;
  }

  return keyMap;
}


/*
 * setDisplay()
 *
 * Writes data to the display
 */
void setDisplay(const char *displayarea)
{
  strcpy(Display, displayarea);
  return;
}

/*
 * setHeatingOn()
 *
 * Controls switching heating on and off
 */
void setHeatingOn(bool heat)
{
  HeatingOn = heat;
  return;
}

uint16_t get_current_time(void)
{
  return timeElapsed;
}


void timeTick(void)
{
	timeElapsed++;
	return;
}
