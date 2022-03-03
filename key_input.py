from pynput import keyboard
import rover_nav
def on_press(x):
    try:
        print('alphanumeric key {0} pressed'.format(x.char))
        key = format(x.char)

        if(key == 'w'):
            rover_nav.rover_forward()
        elif(key == "s"):
            rover_nav.rover_backward()
        elif(key == "a"):
            rover_nav.rover_left_rotation()
        elif(key == "d"):
            rover_nav.rover_right_rotation()
        elif(key == "h"):
            rover_nav.rover_halt()
        elif(key == "1"):
            rover_nav.rover_speed(key)
        elif(key == "2"):
            rover_nav.rover_speed(key)
        elif(key == "3"):
            rover_nav.rover_speed(key)
        elif(key == "r"):
            rover_nav.arm_instructions(key,"base_left")
        elif(key == "f"):
            rover_nav.arm_instructions(key,"base_right")
        elif(key == "t"):
            rover_nav.arm_instructions(key,"first_actuator_up")
        elif(key == "g"):
            rover_nav.arm_instructions(key,"first_actuator_down")
        elif(key == "y"):
            rover_nav.arm_instructions(key,"second_actuator_up")
        elif(key == "h"):
            rover_nav.arm_instructions(key,"second_actuator_down")
        elif(key == "u"):
            rover_nav.arm_instructions(key,"third_actuator_up")
        elif(key == "j"):
            rover_nav.arm_instructions(key,"third_actuator_down")
        elif(key == "i"):
            rover_nav.arm_instructions(key,"claw_close")
        elif(key == "k"):
            rover_nav.arm_instructions(key,"claw_open")
        elif(key == "o"):
            rover_nav.arm_instructions(key,"claw_right_rotate")
        elif(key == "l"):
            rover_nav.arm_instructions(key,"claw_left_rotate")
        elif(key == "v"):
            rover_nav.arm_instructions(key,"arm halted")

    except AttributeError:
        print('special key {0} pressed'.format(x))
        key = format(x)
        if key == "Key.up":
            rover_nav.rover_forward()
        elif(key == "Key.down"):
            rover_nav.rover_backward()
        elif(key == "Key.left"):
            rover_nav.rover_left_rotation()
        elif(key == "Key.right"):
            rover_nav.rover_right_rotation()
       
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
