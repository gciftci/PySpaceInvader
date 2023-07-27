class Config:
    __globals = {
        # Global
        "WIDTH": 800,
        "HEIGHT": 600,
        "FPS": 60,
        "BACKGROUND": (0, 0, 0),
        "DEBUG": True,

        # Colors
        "colors": {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "GREEN": (0, 255, 0),
            "DARK_GREEN": (0, 155, 0),
            "BLUE": (0, 0, 100),
            "DARK_BLUE": (0, 0, 100),
            "CYAN": (0, 255, 255)
        },
	}

    @staticmethod
    def conf(name, sub=None):
        if sub:
            return Config.__globals[name][sub]
        else:
            return Config.__globals[name]