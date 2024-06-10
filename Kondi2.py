import network
import socket
import machine
import time
from machine import Pin, PWM

def play_sound(time_seconds):
    #turn on sound
    sound.on()
    #wait 0.5 seconds
    time.sleep(time_seconds)
    #turn off sound
    sound.off()

#function to reset start position for every motor
def homing():
    #start z homing
    print('z homing',end='')
    while stop_z.value() == 0:
        #move table to z_stop button
        move.write('G21G91G1Z-0.1F100') #$J=G21G91Y-1F100
        move.write('\n')
        time.sleep(0.1)
        print('.',end='')
    print('z homed')
    play_sound(0.5)
    #start x homing
    print('x homing',end='')
    while stop_x.value() == 0:
        #move table to x_stop button
        move.write('G21G91G1X-0.1F100')
        move.write('\n')
        #wait 0.1 second
        time.sleep(0.1)
        print('.',end='')
    print('x homed')
    play_sound(0.5)
    #start y homing
    print('y homing',end='')
    while stop_y.value() == 0:
        #move drawer to y_stop button
        move.write('G21G91G1Y0.1F100')
        move.write('\n')
        time.sleep(0.1)
        print('.',end='')
    print('y homed')
    play_sound(0.5)
    # COMMAND TO RESET ZERO
    move.write('G10 P0 L20 X0 Y0 Z0')
    move.write('\n')
    print('k2 homing',end='')
    while stop_k2.value() == 0:
        #move table to z_stop button
        keep.write('G21G91G1Y0.1F100')
        keep.write('\n')
        time.sleep(0.1)
        print('.',end='')
    print('k2 homed')
    play_sound(0.5)
    print('k1 homing',end='')
    while stop_k1.value() == 0:
        #move table to z_stop button
        keep.write('G21G91G1Z0.1F100')
        keep.write('\n')
        time.sleep(0.1)
        print('.',end='')
    print('k1 homed')
    for _ in range(3):
        play_sound(0.5)
        time.sleep(0.5)
    

#function to throw cake from right keeper
def throwR():
    #start position for servo
    angle0 = 132
    #throwing position for servo
    angle1 = 95
    #rotate servo to start position
    r_pwm.duty(angle0)
    time.sleep(0.5)
    print('k2 homing',end='')
    #lift up right table while cake does not touch button
    while stop_k2.value() == 0:
        keep.write('G21G91G1Y0.1F100')
        keep.write('\n')
        time.sleep(0.1)
        print('.',end='')
    print('k2 homed')
    keep.write('G21G91G1Y-0.4F100')
    keep.write('\n')
    time.sleep(1)
    #rotate servo to throwing position
    r_pwm.duty(angle1)
    time.sleep(0.5)
    #rotate servo to start position
    r_pwm.duty(angle0)
    time.sleep(0.5)

#function to throw cake from left keeper
def throwL():
    angle0 = 21
    angle1 = 55
    l_pwm.duty(angle0)
    time.sleep(0.5)
    print('k1 homing',end='')
    while stop_k1.value() == 0:
        keep.write('G21G91G1Z0.1F100')
        keep.write('\n')
        time.sleep(0.1)
        print('.',end='')
    print('k1 homed')
    keep.write('G21G91G1Z-0.4F100')
    keep.write('\n')
    time.sleep(1)
    l_pwm.duty(angle1)
    time.sleep(0.5)
    l_pwm.duty(angle0)
    time.sleep(0.5)

#function to fill chocolate
def fillChoco():
    #turn on chocolate pomp
    choco_fill1.on()
    choco_fill2.off()
    #wait 10 seconds
    time.sleep(10)
    #turn off chocolate pomp
    choco_fill1.off()
    choco_fill2.on()
    time.sleep(0.5)
    choco_fill1.off()
    choco_fill2.off()

#function to fill cherry
def fillCherry():
    #turn on cherry pomp
    cherry_fill1.on()
    cherry_fill2.off()
    #wait 10 seconds
    time.sleep(10)
    #turn off cherry pomp
    cherry_fill1.off()
    cherry_fill2.on()
    time.sleep(0.5)
    cherry_fill1.off()
    cherry_fill2.off()
    
#function to draw pictures
def drawer(drawing):
    if drawing == "Lab":
        print("drawing labirint")
        move.write('G21G91G1X0.8F100')
        move.write('\n')
        move.write('G21G91G1Y-0.8F100')
        move.write('\n')
        move.write('G21G91G1X-0.7F100')
        move.write('\n')
        move.write('G21G91G1Y0.7F100')
        move.write('\n')
        move.write('G21G91G1X0.6F100')
        move.write('\n')
        move.write('G21G91G1Y-0.6F100')
        move.write('\n')
        move.write('G21G91G1X-0.5F100')
        move.write('\n')
        move.write('G21G91G1Y0.5F100')
        move.write('\n')
        move.write('G21G91G1X0.4F100')
        move.write('\n')
        move.write('G21G91G1Y-0.4F100')
        move.write('\n')
        move.write('G21G91G1X-0.3F100')
        move.write('\n')
        move.write('G21G91G1Y0.3F100')
        move.write('\n')
        move.write('G21G91G1X0.2F100')
        move.write('\n')
        move.write('G21G91G1Y-0.2F100')
        move.write('\n')
    elif drawing == "Smile":
        print("drawing smile")
        move.write('G21G91G1Z-4F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y-0.3F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Z4F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y-0.2F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y-0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X0.2F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X-0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y-0.2F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y-0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X0.2F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y0.2F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X-0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X-0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X-0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X-0.2F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y-0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X-0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y-0.2F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X-0.2F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y-0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X-0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Z-4F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X0.6F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Z4F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y-0.2F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X-0.1Y-0.1F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Z-4F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Y0.2F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1Z4F100')
        move.write('\n')
        time.sleep(0.5)
        move.write('G21G91G1X-0.1F100')
        move.write('\n')
    elif drawing == "DR":
        print("drawing DR")
    elif drawing == "Square":
        print("drawing square")
        move.write('G21G91G1X0.8F100')
        move.write('\n')
        move.write('G21G91G1Y-0.8F100')
        move.write('\n')
        move.write('G21G91G1X-0.8F100')
        move.write('\n')
        move.write('G21G91G1Y0.8F100')
        move.write('\n')

#function to create cake with order received from UDP
def create(layers, choco, cherry, drawing):
    homing()
    print('_____________')
    time.sleep(1)
    move.write('G21G91G1Z14.5F100')#Z DISTANCE from home to funnel
    move.write('\n')
    print('rising table')
    time.sleep(9)
    print('table near funnel')
    print('_____________')
    for i in range(layers-1):
        print(i+1, 'layer')
        print('throwing left')
        throwL()
        time.sleep(2)
        print('throwed left')
        print('_____________')
        move.write('G21G91G1Z-1.5F100')#Z DISTANCE from funnel down
        move.write('\n')
        move.write('G21G91G1X1.8F100')#X DISTANCE from funnel to shower
        move.write('\n')
        print('moving table to shower')
        time.sleep(3)
        print('table under shower')
        print('_____________')
        print('filling jam')
        if choco > 0:
            my_spr.fill_first()
            choco -= 1
            print('filled chocolate')
            print('_____________')
        else:
            my_spr.fill_second()
            print('filled cherry')
            print('_____________')
        move.write('G21G91G1X-1.8F100')#X DISTANCE from shower to funnel
        move.write('\n')
        print('moving table to funnel')
        time.sleep(2)
        print('table under funnel')
        print('_____________')
    throwR()
    print('throwing right')
    time.sleep(2)
    print('throwed right')
    print('_____________')
    move.write('G21G91G1Z-8F100')
    move.write('\n')
    move.write('G21G91G1X3.6F100')#X DISTANCE from funnel to drawer
    move.write('\n')
    move.write('G21G91G1Y-0.7F100')#Y DISTANCE for drawer to cake
    move.write('\n')
    move.write('G21G91G1Z2.5F100')#Z DISTANCE up to drawer
    move.write('\n')
    print('moved main drawer')
    print('_____________')
    time.sleep(5)
    print('moving drawer layers')
    for _ in range(layers):
        move.write('G21G91G1Z0.7F100')#Z DISTANCE up to drawer
        move.write('\n')
        time.sleep(1)
    print('table under drawer')
    drawer(drawing) #calling drawing function
    time.sleep(5)
    for _ in range(layers):#Z DISTANCE down from drawer
        move.write('G21G91G1Z-0.5F100')
        move.write('\n')
        time.sleep(1)
    move.write('G21G91G1Z-2F100')#Z DISTANCE down from drawer
    move.write('\n')
    move.write('G21G91G1X2F100')#X DISTANCE from drawer to finish
    move.write('\n')
    move.write('G21G91G1Z6F100')#Z DISTANCE up to finish
    move.write('\n')
    print('finished')
    
def start_work():
    print('Starting grbl')
    move.write('?')
    move.write('\n')
    response = move.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    keep.write('?')
    keep.write('\n')
    response = keep.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    move.write('$I')
    move.write('\n')
    response = move.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    keep.write('$I')
    keep.write('\n')
    response = keep.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    move.write('$$')
    move.write('\n')
    response = move.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    keep.write('$$')
    keep.write('\n')
    response = keep.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    move.write('$G')
    move.write('\n')
    response = move.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    keep.write('$G')
    keep.write('\n')
    response = keep.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    keep.write('$100=400')
    keep.write('\n')
    response = keep.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    keep.write('$101=400')
    keep.write('\n')
    response = keep.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    keep.write('$102=400')
    keep.write('\n')
    response = keep.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    move.write('$100=400')
    move.write('\n')
    response = move.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    move.write('$101=400')
    move.write('\n')
    response = move.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    move.write('$102=400')
    move.write('\n')
    response = move.read()
    if response:
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])
    time.sleep(1)
    print("Necessary commands sent. Ready to work")
    for _ in range(3):
        play_sound(0.5)
        time.sleep(0.5)

# Connect to WiFi
wifi_ap = network.WLAN(network.AP_IF)
wifi_ap.active(True)
wifi_ap.config(essid='Bakery', authmode=network.AUTH_WPA_WPA2_PSK, password='12345678') #Set access point name and password

# Create UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('0.0.0.0', 80))
# Configure UARTs

move = machine.UART(1, baudrate=115200, tx=4, rx=5)  #mover is connected to tx1 and rx1
keep = machine.UART(2, baudrate=115200, tx=17, rx=16)  #keeper is connected to tx2 and rx2

#set all pins
stop_x = machine.Pin(19, Pin.IN)
stop_y = machine.Pin(21, Pin.IN)
stop_z = machine.Pin(22, Pin.IN)
stop_k1 = machine.Pin(23, Pin.IN)
stop_k2 = machine.Pin(18, Pin.IN)
l_servo = 25
r_servo = 26
l_pwm = PWM(Pin(l_servo), freq=50)
r_pwm = PWM(Pin(r_servo), freq=50)
choco_fill1 = machine.Pin(27, machine.Pin.OUT)
cherry_fill1 = machine.Pin(33, machine.Pin.OUT)
choco_fill2 = machine.Pin(14, machine.Pin.OUT)
cherry_fill2 = machine.Pin(15, machine.Pin.OUT)
sound = machine.Pin(2, machine.Pin.OUT)

response = 0

#start GRBL
start_work()

#Main loop
while True:
    data, addr = udp_socket.recvfrom(1024)  #Receive data from UDP
    command = data.decode('utf-8')
    print(command)
    if command.startswith('M'):
        letter = command[1]
        qual = command[2:]
        print('before:', command)
        command = f"G21G91G1{letter}{qual}F100" #
        print(command)
        move.write(command)
        move.write('\n') #Send command to move without the first letter
        response = move.read()
        print('for mover')
    elif command.startswith('K'):
        letter = command[1]
        qual = command[2:]
        print('before:', command)
        command = f"G21G91G1{letter}{qual}F100" #
        print(command)
        keep.write(command)
        keep.write('\n') #Send command to move without the first letter
        response = move.read()
        print('for mover')
    elif command.startswith('H'):
        homing();#Start homing
    elif command.startswith('T'):
        if command[1] == "L":
            throwL()
        else:
            throwR()
    elif command.startswith('F'):
        if command[1] == "L":
            my_spr.fill_second()
        else:
            my_spr.fill_first()
    elif command.startswith("S"):
        if command[1] == "K":
            keep.write(command[2:])
            keep.write('\n') #Send command to move without the first letter
            response = move.read()
            print('for keeper')
        elif command[1] == "M":
            move.write(command[2:])
            move.write('\n') #Send command to move without the first letter
            response = move.read()
            print('for mover')
    else:
        play_sound(2)
        layers = int(command[0])
        choco = int(command[2])
        cherry = int(command[4])
        drawing = command[6:]
        print("layers:", layers, "choco:", choco,"cherry:",cherry,"drawing:",drawing)
        create(layers, choco, cherry, drawing) #Start creating cake
    
    if response:
        udp_socket.sendto(response, addr)  # Send response back to the client
        response = response.decode('utf-8')
        li = list(response.split('\r\n'))
        for i in range(len(li)):
            print(li[i])

