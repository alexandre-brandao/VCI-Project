/*
 * State machine code to control the heating system.
 *
 * This implementation is totally empty. You should provide the required
 * definitions, protocols and code in the adequate locations.
 *
 */
#include <string.h>
#include <stdint.h>
/*
*   State Machine states declaration
*   Auto: Switches the heating ON/OFF when the temperature is below or
*   above a certain threshold
*   Always ON: forces heating always on, no matter the temperature
*   Always OFF: forces heating always off,no matter the temperature
*   Temperature set: allows for setting the temperature threshold. In this mode
*   heating is always off.  The temperature is set in a range from 10-30 ºC
*/
typedef enum {
  Auto,
  AlwaysOn,
  AlwaysOff,
  TemperatureSet
} OperationState_t;

/*State Machine Structure definition*/
typedef struct {
  OperationState_t currentstate;
  OperationState_t initialstate;
} sm_t;

extern sm_t smTempControl;

/*Temperature Threshold*/
extern uint16_t TThreshold;
/*time counter*/
extern uint16_t tcounter;

void sm_execute(sm_t *smp);

/*
 * getCurrentStateName writes a string with the state name in name
 */
void getCurrentStateName(sm_t sm, char *name);
