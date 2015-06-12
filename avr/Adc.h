
#ifndef ADC_H
#define ADC_H

#include <avr/io.h>



void setup_adc(void);


// Note: get the data from ADC.
void adc_read(const uint8_t); 


#endif /* ADC_H */
