# menu_button.py

import arcade
from typing import Union, Tuple

class MenuButton():
    def __init__(self, text: str, center_x, center_y, width, height, theme=None,
                font_size=18, font_face: Union[str, Tuple[str, ...]] = "Arial", font_color=arcade.color.BLACK,
                face_color=arcade.color.LIGHT_GRAY, highlight_color=arcade.color.WHITE,
                shadow_color=arcade.color.GRAY, button_height=2, button_textures=None):

        super().__init__()

        self.text = text
        self.theme = theme  # Add this line

        self.center_x = center_x
        self.center_y = center_y

        self.width = width
        self.height = height

        self.font_size = font_size
        self.font_face = font_face
        self.font_color = font_color

        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color

        self.button_height = button_height
        self.pressed = False

        # Initialize textures to None
        self.normal_texture = None
        self.press_texture = None

        if button_textures:
            self.set_textures(button_textures)

    def on_click(self):
        if self.text == "Next (N)":
            self.theme.next_bg_color()
        elif self.text == "Previous (P)":
            self.theme.prev_bg_color()
        else:
            # Toggle the menu visibility when clicking the menu button
            self.theme.show_menu = not self.theme.show_menu
        self.pressed = not self.pressed
        self.current_texture = self.press_texture

    def on_release(self):
        # Handle button release event
        # Reset the button's texture to normal when released
        self.current_texture = self.normal_texture
                    
    def hover_point(self, hover_x: float, hover_y: float) -> bool:
        if hover_x > self.center_x + self.width / 2:
            return False
        if hover_x < self.center_x - self.width / 2:
            return False
        if hover_y > self.center_y + self.height / 2:
            return False
        if hover_y < self.center_y - self.height / 2:
            return False

        return True

    def draw_color_theme(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

    def set_textures(self, button_textures):
        """Set the button textures."""
        self.normal_texture = button_textures.get("normal")
        self.press_texture = button_textures.get("pressed")
        self.current_texture = self.normal_texture

    def draw_texture_theme(self):
        if self.pressed:
            arcade.draw_texture_rectangle(self.center_x, self.center_y, self.width, self.height, self.press_texture)
        else:
            arcade.draw_texture_rectangle(self.center_x, self.center_y, self.width, self.height, self.normal_texture)

    def on_draw(self):
        """ Draw the button """
        if self.theme:
            self.draw_texture_theme()
        else:
            self.draw_color_theme()

        arcade.draw_text(self.text, self.center_x, self.center_y,
                         self.font_color, font_size=self.font_size,
                         font_name=self.font_face,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")
