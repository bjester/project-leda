Project Leda
============

A high-altitude balloon (HAB) project which was founded by students of Palomar Community College and carried on by students of Cal State San Marcos.  For more information, please visit http://projectleda.org/ or contact the students involved.


Current Development:
- Log object              -- implemented, needs integration testing
- Scheduler (Leda object) -- using zope.event (asyncio requires python 3.4+ but our serial driver needs 2.7)
                          -- Camera takes a very long time to capture.  May be largest bottleneck.
- Daughter Board          -- Sensor data capture by AVR daughter board, spec being built by Julian and Doug
- UART object             -- skeletal, needs Daughter Board spec
- Post-capture Decoder    -- reads Log files, converts raw data from sensors into useful data 
- Integration testing     

No longer being developed:
- GPS object              -- Opting for self-contained, proprietary solution
- Radio object            -- Proprietary GPS recommends against this

