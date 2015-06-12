

#ifndef TIMER_H
#define TIMER_H

#include <avr/io.h>

/*
 * With 8bits. F_CPU 16000000. count=250 CLK/64, overflow=4ms,250Hz 
 */

#define TIMER0_STOP()    do { TCCR0B &= (uint8_t)~(_BV(CS02) | _BV(CS01) | _BV(CS00)); } while(0)
#define TIMER0_CLK1()    do { TCCR0B |= (uint8_t)(_BV(CS00)); } while(0)
#define TIMER0_CLK8()    do { TCCR0B |= (uint8_t)(_BV(CS01)); } while(0)
#define TIMER0_CLK64()   do { TCCR0B |= (uint8_t)(_BV(CS01) | _BV(CS00)); } while(0)
#define TIMER0_CLK256()  do { TCCR0B |= (uint8_t)(_BV(CS02)); } while(0)
#define TIMER0_CLK1024() do { TCCR0B |= (uint8_t)(_BV(CS02) | _BV(CS00)); } while(0)


// A timer that runs at 1KHz.
// Using timer0.
void timer0_start(void);
void timer0_stop(void);
uint16_t getCount0(void);


#endif /* TIMER_H */
