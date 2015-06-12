

#ifndef LEDA_H
#define LEDA_H

#include <avr/io.h>

#define MPX5100_ADC_CH   0x00
#define MPXV4115V_ADC_CH 0x01

#define AVR_TEMP_ADC_CH 0x08
#define AVR_11V_ADC_CH 0x0E
#define AVR_GND_ADC_CH 0x0F

#define MMA7455_I2C_ADDR (0x1D << 1)

#define DS1631_I2C_ADDR (0x48 << 1)

#define HIH8120_12C_ADDR (0x27 << 1)


void leda_setup(void);

void leda_pollAll(void);
void leda_getAll(void);

#endif /* LEDA_H */
