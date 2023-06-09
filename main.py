def on_button_pressed_a():
    basic.show_number(2006)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(20)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("SHIHANA!")
basic.show_icon(IconNames.HEART)
basic.show_leds("""
    # . . . #
        # . . . #
        # # # # #
        # . . . #
        # . . . #
""")