
#include <stdint.h>
#include <stdbool.h>

extern char Display[];

#define NEXTKEYMASK   0x08
#define PLUSKEYMASK   0x04
#define MINUSKEYMASK  0x02
#define TEMPKEYMASK   0x01

extern bool NEXTKeyPressed;
extern bool PlusKeyPressed;
extern bool MinusKeyPressed;
extern bool TempKeyPressed;

extern uint16_t Temperature;

/*
 * readTemp()
 *
 * readTemp() returns the process temperature in tenths of degree Celsius
 */
uint16_t readTemp(void);

/*
 * getHeatingOn()
 *
 * Returns the status of the heating element (true == "heating is on")
 */
bool getHeatingOn(void);

/*
 * keyRead()
 *
 * Returns the key presses as a bitmap
 */
uint8_t keyRead(void);

/*
 * setDisplay()
 *
 * Writes data to the display
 */
void setDisplay(const char *displayarea);

/*
 * setHeatingOn()
 *
 * Controls switching heating on and off
 */
void setHeatingOn(bool heat);

/*
 * get_current_time
 *
 * Gets the current time
 */
uint16_t get_current_time(void);


void timeTick(void);
