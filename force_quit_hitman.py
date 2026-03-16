import subprocess
import keyboard

def quit_program():
    # Force close
    process_name = "HITMAN3.exe"
    subprocess.run(["taskkill", "/IM", process_name, "/F"], shell=True)

def register_hotkey():
    # Register hotkey
    keyboard.add_hotkey("alt+f4", quit_program) #Change hotkey here

def main():
    register_hotkey()
    print("AltF4_Hitman is currently active")
    keyboard.wait()

if __name__ == "__main__":
    main()