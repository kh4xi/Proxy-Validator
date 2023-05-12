class MyColors:
    r_color = '\033[91m'
    g_color = '\033[32m'
    y_color = '\033[33m'
    n_color = '\033[0m'
    w_color = '\033[37m'

    @staticmethod
    def colorize_text(text, color_code):
        return f"{color_code}{text}{MyColors.n_color}"
