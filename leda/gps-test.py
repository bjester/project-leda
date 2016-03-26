from gps3 import gps3

gps_connection = gps3.GPSDSocket(host='127.0.0.1', port='2947')
gps_fix = gps3.Fix()
new_data = None
for new_data in gps_connection:
    if new_data:
        gps_fix.refresh(new_data)
        if gps_fix.TPV['alt'] != 'n/a':
            print('Altitude = ',gps_fix.TPV['alt'])
            print('Latitude = ',gps_fix.TPV['lat'])

