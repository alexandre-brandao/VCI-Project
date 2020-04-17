/*
 * State machine code to control the heating system.
 *
 * This implementation is totally empty.
 */
 #include "heatingSM.h"
 #include "heatingsystem.h"
 #include <stdio.h>

sm_t smTempControl;

/*Temperature Threshold*/
uint16_t TThreshold1 = 150; // If this variable doesn't exist, then next variable goes to 0;??????
uint16_t TThreshold = 150;
/*timer counter*/
uint16_t tcounter = 0;

char InfoDisplay[17];

uint8_t keymap;


void sm_execute(sm_t *smp)
{
  switch( (*smp).currentstate ) {

    case Auto:               /*STATE AUTO*/

    /*
    *   **AVAILABLE OPERATIONS**
    *  +  Set heating on for 5s
    *  -  Set heating off for 5s
    */
      keymap = keyRead();

      if(tcounter == 0) // Button + was not PRESSED
      {
        /*Autoset Temperature to setpoint*/
        if(Temperature < TThreshold)
        {
          setHeatingOn(true); /*Increase Temperature*/
        }
        else {
          setHeatingOn(false); /*decrease Temperature*/
        }
      }

      /*Choose whether +/- takes priority or decrement counter*/

      if(keymap&MINUSKEYMASK) /*   -   Pressed  */
      {
        setHeatingOn(false);
        tcounter = 5;

      } else if(keymap&PLUSKEYMASK) /*   +   Pressed  */
      {
        setHeatingOn(true);
        tcounter = 5;

      } else if(tcounter != 0)  /* wait 5 seconds*/
      {
        tcounter--;
      }

      /* Display Section */
      if(keymap&TEMPKEYMASK) {
        sprintf(InfoDisplay, "ROOM TEMP=%-3d ", readTemp());
        setDisplay(InfoDisplay);
      }
      else {
        sprintf(InfoDisplay, "AUTO T=%-4d ", TThreshold);

        if(getHeatingOn() == true) {  /*Send to display HEATING ON*/
          strcat(InfoDisplay, "ON ");
        } else {
          strcat(InfoDisplay, "OFF");
        }

        setDisplay(InfoDisplay);
      }

      /* NEXT STATE */
      if(keymap&NEXTKEYMASK) {
        (*smp).currentstate = AlwaysOn;
        tcounter = 0;
      }

    break;

    case AlwaysOn:             /*STATE ALWAYS ON*/
      
      /*
      *   **AVAILABLE OPERATIONS**
      *  -  Set heating off for 5s
      */
        keymap = keyRead();

        if(tcounter == 0) // Button + was not PRESSED/released
        {
          setHeatingOn(true);

        }
        /*Choose  -  Pressed Button or decrement counter*/

        if(keymap&MINUSKEYMASK && getHeatingOn() == true) /*   -   Pressed  */
        {
          setHeatingOn(false);
          tcounter = 5;

        } else if(tcounter != 0)  /*wait 5 seconds*/
        {
          tcounter--;
        }

        /* Display Section */
        if(keymap&TEMPKEYMASK) {
          sprintf(InfoDisplay, "ROOM TEMP=%-3d ", readTemp());
          setDisplay(InfoDisplay);
        }
        else {
          strcpy(InfoDisplay, "ALWAYS_ON");
          setDisplay(InfoDisplay);
        }

      /* NEXT STATE */
      if(keymap&NEXTKEYMASK) {
        (*smp).currentstate = AlwaysOff;
        tcounter = 0;
      }
    break;

    case AlwaysOff:
      /*
      *   **AVAILABLE OPERATIONS**
      *  +  Set heating on for 5s
      */
      keymap = keyRead();

      if(tcounter == 0) // Button - was not PRESSED/released
      {
        setHeatingOn(false);

      }

      /*Choose  -  Pressed Button or decrement counter*/

      if(keymap&PLUSKEYMASK && getHeatingOn() == false) /*   -   Pressed  */
      {
        setHeatingOn(true);
        tcounter = 5;

      } else if(tcounter != 0)  /*wait 5 seconds*/
      {
        tcounter--;
      }

      /* Display Section */
      if(keymap&TEMPKEYMASK) {
        sprintf(InfoDisplay, "ROOM TEMP=%-3d ", readTemp());
        setDisplay(InfoDisplay);
      }
      else {
        strcpy(InfoDisplay, "ALWAYS_OFF");
        setDisplay(InfoDisplay);
      }


      /* NEXT STATE */
      if(keymap&NEXTKEYMASK) {
        (*smp).currentstate = TemperatureSet;
        tcounter = 0;
      }
    break;

    case TemperatureSet:           /*STATE TEMPERATURE SET*/
      /*
      *   **AVAILABLE OPERATIONS**
      *  +  Temperature increases
      *  -  Temperature decreases
      */

      /*Heating is always OFF*/
      setHeatingOn(false);

      /*Read KeyMap*/
      keymap = keyRead();

      if( (keymap&PLUSKEYMASK) && (TThreshold < 300) )
      {
        TThreshold++;
      }

      if ( (keymap&MINUSKEYMASK) && (TThreshold > 100) )
      {
        TThreshold--;
      }

      if(keymap&TEMPKEYMASK) {
        sprintf(InfoDisplay, "ROOM TEMP=%-3d ", readTemp());
        setDisplay(InfoDisplay);
      } else {
        sprintf(InfoDisplay, "TSET T=%-4d OFF ", TThreshold);
        setDisplay(InfoDisplay);
      }

      if(keymap&NEXTKEYMASK) {
        (*smp).currentstate = Auto;
      }
      setHeatingOn(false);
      /*user based temperature set*/

    break;

    default:
    break;
  }
  return;
}

/*              Get State Names            */
void getCurrentStateName(sm_t sm, char *name)
{
  if(sm.currentstate == AlwaysOn) {
    strcpy(name,"Always On");

  } else if (sm.currentstate == AlwaysOff) {
    strcpy(name,"Always Off");

  } else if (sm.currentstate == Auto) {
    strcpy(name,"Auto");

  } else {
    strcpy(name,"Temperature Set");

  }
}
