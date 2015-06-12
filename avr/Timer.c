

#include <avr/interrupt.h>
#include "Timer.h"



volatile uint16_t count0 = 0;

ISR(TIMER0_COMPA_vect)
{
	++count0;
	TCNT0 = 0;
}


void timer0_start(void)
{
        TIMER0_STOP();
	OCR0A = 250;
	
	// Clear Match A interrupt.
	TIFR0 = (uint8_t)(_BV(OCF0A));
	
	// Enable Match A interrupt.
	TIMSK0 = (uint8_t)(_BV(OCIE0A));
	
	TIMER0_CLK64();
    
} // End of timer0_start().

void timer0_stop(void)
{
	TIMER0_STOP();
	
	count0 = 0;
	TCNT0 = 0;
	
	// Clear Match A interrupt.
	TIFR0 = (uint8_t)(_BV(OCF0A));
	
	// Disable Match A interrupt.
	TIMSK0 = 0;
    
} // End of timer0_stop().

uint16_t getCount0(void)
{
	return count0;
    
} // End of getCount0().


