import sys

# ANSI escape codes for neon background colors
NEON_COLORS = {
    'black': '\033[40;38;5;82m',
    'red': '\033[41;38;5;198m',
    'green': '\033[42;38;5;118m',
    'yellow': '\033[43;38;5;226m',
    'blue': '\033[44;38;5;81m',
    'magenta': '\033[45;38;5;201m',
    'cyan': '\033[46;38;5;51m',
    'white': '\033[47;38;5;231m',
}

# Neon text color
NEON_TEXT_COLOR = '\033[38;5;16m'

def print_neon(text, neon_color='white', text_color='blue'):
    neon_code = NEON_COLORS.get(neon_color, NEON_COLORS['white'])
    text_color_code = NEON_COLORS.get(text_color, NEON_COLORS['blue'])
    reset_code = '\033[0m'
    print(neon_code + text_color_code + text + reset_code)

# Example usage
if __name__ == "__main__":
    text = "Neon Background"
    print_neon(text)
