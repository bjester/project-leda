
#include <avr/sleep.h>
#include <avr/interrupt.h>

#include "Adc.h"

// An interrupt that doesn't do shit!
// This interrupt is to wake up from CPU sleep. 
EMPTY_INTERRUPT (ADC_vect);

void setup_adc(void)
{
	//Digital Input Disable Register
	DIDR0 = (uint8_t)(_BV(ADC3D) | _BV(ADC2D) | _BV(ADC1D) | _BV(ADC0D));
	
} // End of setup_adc().

void adc_read(const uint8_t ch)
{
	// Voltage reference for ACC is AVCC.
	// ch is for ADC channel selections.
	// Note: ch ={0x9, 0xA, 0xB, 0xC, 0xD} are reserved.
	// Note: ch ={0x4, 0x5} are used by TWI/I2c.
	ADMUX = (uint8_t)(_BV(REFS0) | (0x0F & ch));
	
	// Enable the ADC.
	// Setup for ADC noise reduction mode.
	ADCSRA = (uint8_t)(_BV(ADEN) | _BV(ADIF) | _BV(ADIE) | _BV(ADPS2) | _BV(ADPS1) | _BV(ADPS0));
	set_sleep_mode(SLEEP_MODE_ADC);
	sleep_enable();
	
	// Start and wait for ADC conversion. 
	// Enter sleep mode to start. 
	sleep_cpu();
	sleep_disable();
	
	// Disable ADC to save power.
	ADCSRA = 0x00;
	// Restore the sleep mode.
	set_sleep_mode(SLEEP_MODE_IDLE);
	
} // End of adc_read().

