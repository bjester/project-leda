/*
 * TWI with timeout using timer 2.
 * Both TWI and Timer 2 are being polled.
 */

#include <util/twi.h>
#include "Twi.h"

#define TWI_TIMEOUT 0xFF


static inline void startTimer2(const uint8_t count);
static inline void stopTimer2(void);
static inline uint8_t timer2TimedOut(void);


void setup_twi(void)
{   
    //TWBR = 10;
	//TWBR = 12; // SCL at 400KHz.
	//TWBR = 72; // SCL at 100KHz.
	//TWBR = (F_CPU / 100000UL - 16) / 2; 
	/* initialize TWI clock: 100 kHz clock, TWPS = 0 => prescaler = 1 */
    #if defined(TWPS0)
        /* has prescaler (mega128 & newer) */
        TWSR = 2; // prescaler of 2. 100KHz.
    #endif

			//16000000
    #if F_CPU < 3600000UL
        TWBR = 10;			/* smallest TWBR value, see note [5] */
    #else
        TWBR = (F_CPU / 100000UL - 16) / 2;
    #endif

    // Setup timer 2.
    stopTimer2();   


} // End of setup_tiw().


uint8_t twi_start(void)
{

    // Start Timer 2 and set timeout time.
    startTimer2(TWI_TIMEOUT);

    // Clear interrupt.
    // Enable TWI.
    // Generate start condition.
	TWCR = (uint8_t)(_BV(TWINT) | _BV(TWEN) | _BV(TWSTA));
    
    // Wait for TWI or timer 2 to time out.
    while(bit_is_clear(TWCR, TWINT) && !timer2TimedOut())
        ;

    stopTimer2();

    if(timer2TimedOut())
    {
        // TWI failed: Clean up?

        return 1;

    } else {
        return 0;
    }
	
} // End of twi_start().

// Note: It might be safe to not timeout the stop condition for TWI.
uint8_t twi_stop(void)
{
    
    // Start Timer 2 and set timeout time.
    //startTimer2(TWI_TIMEOUT);
    
    // Clear interrupt.
    // Enable TWI.
    // Generate stop condition.
	TWCR = (uint8_t)(_BV(TWINT) | _BV(TWEN) | _BV(TWSTO));

    // Wait for TWI or timer 2 to time out.
    //while(bit_is_clear(TWCR, TWSTO) && !timer2TimedOut())
    while(bit_is_clear(TWCR, TWSTO))
        ;
        
    //stopTimer2();

    /*
    if(timer2TimedOut())
    {
        // TWI failed: Clean up?

        return 1;

    } else {
        // TWI success.
        return 0;
    }
    */
    return 0;
	
} // End of twi_stop().


uint8_t twi_readAck(uint8_t *d)
{
	
    // Start Timer 2 and set timeout time.
    startTimer2(TWI_TIMEOUT);
    
    // Clear interrupt.
    // Enable TWI.
    // Generate TWI action with ACK.
	TWCR = (uint8_t)(_BV(TWINT) | _BV(TWEA) | _BV(TWEN));

    while(bit_is_clear(TWCR, TWINT) && !timer2TimedOut())
        ;

    if(timer2TimedOut())
    {
        // TWI failed: Clean up?

        *d = 0;
        return 1;

    } else {
        // TWI success.
        
        *d = TWDR;
        return 0;
    }

} // End of twi_readAck().


uint8_t twi_readNack(uint8_t *d)
{
    // Start Timer 2 and set timeout time.
    startTimer2(TWI_TIMEOUT);
    
    // Clear interrupt.
    // Enable TWI.
    // Generate TWI action.
	TWCR = (uint8_t)(_BV(TWINT) | _BV(TWEN));

    while(bit_is_clear(TWCR, TWINT) && !timer2TimedOut())
        ;

    if(timer2TimedOut())
    {
        // TWI failed: Clean up?

        *d = 0;
        return 1;

    } else {
        // TWI success.
        
        *d = TWDR;
        return 0;
    }

} // End of twi_readNAck().



uint8_t twi_write(const uint8_t d)
{
    // Start Timer 2 and set timeout time.
    startTimer2(TWI_TIMEOUT);
    
	// Set data to clock out.
	TWDR = d;
	TWCR = (uint8_t)(_BV(TWINT) | _BV(TWEN));

    while(bit_is_clear(TWCR, TWINT) && !timer2TimedOut())
        ;

    if(timer2TimedOut())
    {
        // TWI failed: Clean up?

        return 1;

    } else {
        // TWI success.
        
        return 0;
    }

} // End of twi_write().

static inline void startTimer2(const uint8_t count)
{
    // clear all of timer 2 Reg.
    OCR2A = count;
    TCNT2 = 0;

    // Clear any interrupt flags.
    TIFR2 = (uint8_t)(_BV(OCF2B) | _BV(OCF2A) | _BV(TOV2));

    // Start the clock at F_CPU/1024
    TCCR2B = (uint8_t)(_BV(CS22) | _BV(CS21) | _BV(CS20));
}

static inline void stopTimer2(void)
{
    // Stop timer 1;
    TCCR2B = 0;
}

static inline uint8_t timer2TimedOut(void)
{
    return bit_is_set(TIFR2, OCF2B);
}


