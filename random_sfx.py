import time
import random
import sys
from playsound import playsound

# --- Config ---
CHANCE_PER_SECOND = 1 / 100
SOUND_FILE = "sfx.mp3"
# --------------

def main():
    sound_path = sys.argv[1] if len(sys.argv) > 1 else SOUND_FILE
    print(f"Running. Chance per second: {CHANCE_PER_SECOND:.4%} | Sound: {sound_path}")
    print("Press Ctrl+C to stop.\n")

    tick = 0
    while True:
        time.sleep(1)
        tick += 1
        roll = random.random()
        if roll < CHANCE_PER_SECOND:
            print(f"[tick {tick}] Playing sound! (rolled {roll:.4f})")
            playsound(sound_path)
        else:
            print(f"[tick {tick}] ... (rolled {roll:.4f})")

if __name__ == "__main__":
    main()
