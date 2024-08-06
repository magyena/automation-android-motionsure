class HandlerRemote:

    def __init__(self, driver):
        self.driver = driver

    def navigateUp(self):
        self.driver.press_keycode(19)

    def navigateDown(self):
        self.driver.press_keycode(20)

    def navigateLeft(self):
        self.driver.press_keycode(21)

    def navigateRight(self):
        self.driver.press_keycode(22)

    def navigateEnter(self):
        self.driver.press_keycode(66)

    def navigateOK(self):
        self.driver.press_keycode(23)