

#ifndef TWI_H
#define TWI_H

#include <avr/io.h>
#include <util/twi.h>



void setup_twi(void);

uint8_t twi_start(void);
uint8_t twi_stop(void);

uint8_t twi_readAck(uint8_t *);
uint8_t twi_readNack(uint8_t *);

uint8_t twi_write(const uint8_t);

#endif /* TWI_H */
