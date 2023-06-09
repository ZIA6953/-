basic.showString("SHIHANA!")
basic.showIcon(IconNames.Heart)
basic.showLeds(`
. # # # .
# . . . .
 . # . . .
 . . # . .
  # # # . .
`)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(2006)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showNumber(17)
})
