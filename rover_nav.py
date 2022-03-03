import socket

host = '192.168.1.27'
port = 5544

def conn():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.connect((host,port))
    return sk
    

def rover_forward():
    rover_conn = conn()
    rover_conn.send('w'.encode('utf-8'))
    print("forward")
    rover_conn.close()

def rover_backward():
    rover_conn = conn()
    rover_conn.send('s'.encode('utf-8'))
    print("backward")
    rover_conn.close()

def rover_left_rotation():
    rover_conn = conn()
    rover_conn.send('a'.encode('utf-8'))
    print("left")
    rover_conn.close()

def rover_right_rotation():
    rover_conn = conn()
    rover_conn.send('d'.encode('utf-8'))
    print("right")
    rover_conn.close()

def rover_halt():
    rover_conn = conn()
    rover_conn.send('h'.encode('utf-8'))
    print("halt")
    rover_conn.close()

def rover_speed(x):
    rover_conn = conn()
    rover_conn.send(x.encode('utf-8'))
    print("speed : "+x)
    rover_conn.close()


def arm_instructions(x,y):
    rover_conn = conn()
    rover_conn.send(x.encode('utf-8'))
    print(x+" : "+y)
    rover_conn.close()

