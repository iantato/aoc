class Colors:
    """ ANSI color codes """
    INFO = "\033[01;32m"
    WARNING = "\033[01;33m"
    ERROR = "\033[01;31m"
    DEBUG = "\033[01;36m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    BROWN = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    LIGHT_GRAY = "\033[37m"
    DARK_GRAY = "\033[30m"
    LIGHT_RED = "\033[31m"
    LIGHT_GREEN = "\033[32m"
    YELLOW = "\033[33m"
    LIGHT_BLUE = "\033[34m"
    LIGHT_PURPLE = "\033[35m"
    LIGHT_CYAN = "\033[36m"
    LIGHT_WHITE = "\033[37m"
    BOLD = "\033[01m"
    FAINT = "\033[02m"
    ITALIC = "\033[03m"
    UNDERLINE = "\033[04m"
    BLINK = "\033[05m"
    NEGATIVE = "\033[07m"
    CROSSED = "\033[09m"
    END = "\033[0m"

    @staticmethod
    def colorize(text: str, color: str) -> str:
        """ Colorize text with the given ANSI color code """
        return f"{color}{text}{Colors.END}"

def log(message: str, level: str = "INFO") -> None:
    """ Log a message with a specific level """
    color_map = {
        "INFO": Colors.INFO,
        "WARNING": Colors.WARNING,
        "ERROR": Colors.ERROR,
        "DEBUG": Colors.DEBUG
    }
    color = color_map.get(level, Colors.LIGHT_GRAY)
    print(f"[{Colors.colorize(level, color)}] {message}")