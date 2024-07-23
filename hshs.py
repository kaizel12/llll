import time
import sys

lyrics = [
    ("I won't question why so many have died", 0.04),
    ("My prayers have made it through yeah", 0.04),
    ("'Cause with all these things we do", 0.04),
    ("It don't matter when I'm coming home to you", 0.04),
    ("I've always been true", 0.04),
    ("I've waited so long just to come hold you", 0.04),
    ("I'm making it through", 0.04),
    ("It's been far too long, we've proven our", 0.04),
    ("love over time's so strong, in all that we do", 0.04),
    ("The stars in the night, they lend me their light", 0.04),
    ("to bring me closer to heaven with you", 0.04),
    ("But with all that we've been through", 0.04),
    ("After all this time I'm coming home to you", 0.04)
]

# Use a shorter delay between lines to match the faster tempo
delays = [0.4] * len(lyrics)

def animate_text(text, char_delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    for i, (text, char_delay) in enumerate(lyrics):
        animate_text(text, char_delay)
        if i < len(lyrics) - 1:
            next_line_delay = max(0, delays[i] - len(text) * char_delay)
            time.sleep(next_line_delay)

if __name__ == "__main__":
    main()
