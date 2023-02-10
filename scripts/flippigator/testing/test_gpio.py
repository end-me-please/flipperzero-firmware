import os
import time

import pytest
from termcolor import colored

from flippigator.case import BaseCase

os.system("color")


@pytest.mark.gpio
class TestGpio(BaseCase):
    def test_gpio_menu_negative(self, nav):
        nav.gpio.go_into()
        menu = nav.get_menu_list()
        menu_ref = [
            "USB-UART Bridge",
            "GPIO Manual Control",
            "5V on GPIO",
        ]
        assert menu == menu_ref, "GPIO menu list is wrong"
        nav.go_to_main_screen()