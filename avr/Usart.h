#ifndef USART_H
#define USART_H

#include <avr/io.h>

void setup_usart(void);

void usart_clearRxBuf(void);

uint8_t usart_isData(void);
uint8_t usart_readData(void);

void usart_writeData(uint8_t);

int usart_putchar(char, FILE *);


#endif /* USART_H */
