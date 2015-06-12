

#include <avr/io.h>
#include <stdio.h>  
#include <avr/interrupt.h>
#include <util/atomic.h>

#include "CircularBuffer.h"
#include "Usart.h"



static /*volatile*/ CircularBuffer rx_cb;

ISR(USART_RX_vect)
{
	cb_write(&rx_cb, (UDR0));
	
} // End of ISR(USART_RX_vect).



void setup_usart()
{
	UCSR0B = (uint8_t)(_BV(RXCIE0) | _BV(RXEN0) | _BV(TXEN0));
	UCSR0C = (uint8_t)(_BV(UCSZ00) | _BV(UCSZ01));
	
	// Baud 38400.
	UBRR0L = 25;
	
	// Baud 2400
	//UBRR0 = 416;
	
	setup_cb(&rx_cb);
	
} // End of setup_usart().

void usart_clearRxBuf(void)
{
	ATOMIC_BLOCK(ATOMIC_RESTORESTATE)
	{
		setup_cb(&rx_cb);
	}
	
} // End of usart_clearRxBuf().

uint8_t usart_isData(void)
{
	ATOMIC_BLOCK(ATOMIC_RESTORESTATE)
	{
		return !cb_isEmpty(&rx_cb);
	}
	
} // End of usart_isData()

uint8_t usart_readData(void)
{
	ATOMIC_BLOCK(ATOMIC_RESTORESTATE)
	{
		return cb_read(&rx_cb);
	}
	
} // End of usart_readData().

void usart_writeData(uint8_t data)
{
	// Wait for a clear TX buffer.
	loop_until_bit_is_set(UCSR0A, UDRE0);
	UDR0 = data;
	
} // End of usart_writeData().


int usart_putchar(char c, FILE *stream)
{
    /*
    if (c == '\n')
        usart_putchar('\r', stream);
    */
    loop_until_bit_is_set(UCSR0A, UDRE0);
    UDR0 = c;
    return 0;
}



