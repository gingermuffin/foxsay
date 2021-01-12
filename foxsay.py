#!/usr/bin/env python3

import sys
import random

# Some constants.
MIN_WIDTH = 1
MAX_WIDTH = 80

GREEN = u"\u001b[32m"
ORANGE = u"\u001b[33m"
RESET = u"\u001b[0m"

BALLOON_IMAGE_PARTS = [
    ["╭", "─", "╮"],
    ["│", " ", "│"],
    ["╰", "─", "╯"],
    [" ", "v", " "],
]

FOX_IMAGE_WITHOUT_COLORS = """
     |\_|\             ,_.=-,_
  ._.@ @  ,._.-=-.,_.=`   {.-`
    '-.,_      (   .-,_ _.`
         'm`m^"-m.G    `
"""[1:-1] # Cut first and last empty lines.

# It's a fox trust me :(.
# All {} will be replaced with its colors.
FOX_IMAGE = """
     |{orange}\_{reset}|{orange}\{reset}             {orange},_.={reset}-,_
  .{orange}_.{reset}{green}@ @{reset}  {orange},._.-=-.,_.=`   {reset}{{.-`
    {orange}'-.,_      (   .-,_ _.{reset}`
         {orange}'m`m^"-m.G{reset}    {orange}`{reset}
"""[1:-1].format(green = GREEN, orange = ORANGE, reset = RESET)

WISDOM = [
    "What does the fox say?",
    "Ring-ding-ding-ding-dingeringeding!",
    "Wa-pa-pa-pa-pa-pa-pow!",
    # "Hatee-hatee-hatee-ho!",
    # "Joff-tchoff-tchoffo-tchoffo-tchoff!",
    # "Jacha-chacha-chacha-chow!",
    # "Fraka-kaka-kaka-kaka-kow!",
    # "A-hee-ahee ha-hee!",
    # "A-oo-oo-oo-ooo!"
    "Eating one cooked chicken restores six hunger",
]

# Wisdom functions.
def get_random_wisdom():
    return random.choice(WISDOM)

# Draw functions.
def split_text_by_lines(text, line_width):
    lines = []

    for i in range(0, len(text), line_width):
        lines.append(text[i:i+line_width])

    return lines

def draw_balloon(text = None):
    # We get a random text if we don't have one.
    if text is None or text == "":
        text = get_random_wisdom()

    # Reserve 2 symbols for borders and 2 symbols for gaps.
    line_width = max(MIN_WIDTH, min(MAX_WIDTH - 4, len(text)))
    lines = split_text_by_lines(text, line_width)

    result = ""

    # Draw top line.
    result += BALLOON_IMAGE_PARTS[0][0] +\
              BALLOON_IMAGE_PARTS[0][1] * (line_width + 2) +\
              BALLOON_IMAGE_PARTS[0][2] +\
              "\n"

    # Draw an empty line.
    result += BALLOON_IMAGE_PARTS[1][0] +\
              BALLOON_IMAGE_PARTS[1][1] * (line_width + 2) +\
              BALLOON_IMAGE_PARTS[1][2] +\
              "\n"

    for line in lines:
        extra_space = line_width - len(line)

        result += BALLOON_IMAGE_PARTS[1][0] +\
                  BALLOON_IMAGE_PARTS[1][1] +\
                  line +\
                  BALLOON_IMAGE_PARTS[1][1] * extra_space +\
                  BALLOON_IMAGE_PARTS[1][1] +\
                  BALLOON_IMAGE_PARTS[1][2] +\
                  "\n"

    # Draw an empty line.
    result += BALLOON_IMAGE_PARTS[1][0] +\
              BALLOON_IMAGE_PARTS[1][1] * (line_width + 2) +\
              BALLOON_IMAGE_PARTS[1][2] +\
              "\n"

    # Draw bottom line.
    result += BALLOON_IMAGE_PARTS[2][0] +\
              BALLOON_IMAGE_PARTS[2][1] +\
              BALLOON_IMAGE_PARTS[3][1] +\
              BALLOON_IMAGE_PARTS[2][1] * (line_width) +\
              BALLOON_IMAGE_PARTS[2][2] +\
              "\n"

    print(result)


def draw_fox():
    print(FOX_IMAGE)

# Main.
def main():
    text = None

    # Get text from the input.
    if not sys.stdin.isatty():
        text = ""
        for line in sys.stdin:
            text += line
        text = text.replace("\n", "")

    # Otherwise from the arguments.
    if text is None and len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])

    draw_balloon(text)
    draw_fox()

if __name__ == "__main__":
    main()
