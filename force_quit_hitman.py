import subprocess
import keyboard

process_name = "HITMAN3.exe" #Change process name here
hotkey = "alt+f4" #Change hotkey here | alt+f4 | ctrl+alt+f4 | f4 | etc

def quit_program():
    # Force close
    subprocess.run(["taskkill", "/IM", process_name, "/F"], shell=True)

def register_hotkey():
    # Register hotkey
    keyboard.add_hotkey(hotkey, quit_program)

def main():
    register_hotkey()
    print("Force quit is active")
    print(f"Press {hotkey} to force quit {process_name}")
    keyboard.wait()

if __name__ == "__main__":
    main()