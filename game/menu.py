# menu.py

import arcade
from arcade.gui import UIManager
from menu_button import MenuButton
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Menu(arcade.View):
    def __init__(self, game_window):
        super().__init__()
        self.background_colors = [arcade.color.AMAZON, arcade.color.UA_BLUE, arcade.color.ENGLISH_VIOLET, arcade.color.BLACK_BEAN]
        self.current_bg_color = 0
        self.show_menu = False
        self.color_change_in_progress = False

        # Load textures for the menu button
        self.button_textures = {
            "normal": arcade.load_texture(":resources:gui_basic_assets/red_button_normal.png"),
            "pressed": arcade.load_texture(":resources:gui_basic_assets/red_button_press.png")
        }
        
        # Create buttons for changing background color
        self.bg_color_next_button = MenuButton("Next (N)", SCREEN_WIDTH / 2 + 175, SCREEN_HEIGHT / 2 + 25, 175, 50, theme=self,
                                            button_textures=self.button_textures)
        self.bg_color_prev_button = MenuButton("Previous (P)", SCREEN_WIDTH / 2 - 175, SCREEN_HEIGHT / 2 + 25, 175, 50, theme=self, 
                                            button_textures=self.button_textures)

        # Add buttons to the UI manager
        self.ui_manager = UIManager(self.window)
        self.ui_manager.add(self.bg_color_next_button)
        self.ui_manager.add(self.bg_color_prev_button)

        # Create a menu button
        self.menu_button = MenuButton("Menu (M)", SCREEN_WIDTH - 100, SCREEN_HEIGHT - 720, 150, 50, theme=self,
                                      button_textures=self.button_textures)

        # Set the theme attribute for the menu button
        self.ui_manager.add(self.menu_button)

        self.header_text = "Toggle the buttons to change color theme!"
        self.footer_text = "Press \"R\" to refresh the game & \"Esc\" to exit"

    def set_game_window(self, game_window):
        self.game_window = game_window

    def next_bg_color(self):
        if not self.color_change_in_progress:
            self.color_change_in_progress = True
            self.current_bg_color = (self.current_bg_color + 1) % len(self.background_colors)
            arcade.set_background_color(self.background_colors[self.current_bg_color])
            arcade.schedule(self.reset_color_change_flag, 0.5) 

    def prev_bg_color(self):
        if not self.color_change_in_progress:
            self.color_change_in_progress = True
            self.current_bg_color = (self.current_bg_color - 1) % len(self.background_colors)
            arcade.set_background_color(self.background_colors[self.current_bg_color])
            arcade.schedule(self.reset_color_change_flag, 0.5) 

    def reset_color_change_flag(self, _):
        self.color_change_in_progress = False

    def draw(self):
        if self.show_menu:
            arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 35, SCREEN_WIDTH / 2 + 75, SCREEN_HEIGHT / 2 - 125, arcade.color.DARK_SLATE_GRAY + (250,))

            # Draw the background color change buttons
            self.bg_color_next_button.on_draw()
            self.bg_color_prev_button.on_draw()

            # Draw the menu button with the current texture
            self.menu_button.current_texture = self.menu_button.press_texture if self.menu_button.pressed else self.menu_button.normal_texture
            self.menu_button.on_draw()

            # Draw the header text
            arcade.draw_text(
                self.header_text,
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 + 100,
                arcade.color.WHITE,
                18,
                anchor_x="center",
            )

               # Draw the header text
            arcade.draw_text(
                self.footer_text,
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 50,
                arcade.color.WHITE,
                18,
                anchor_x="center",
            )

            # Draw text to display current background and mat colors
            arcade.draw_text(
                f"Color Theme",
                439,
                SCREEN_HEIGHT / 2 + 20,
                arcade.color.WHITE,
                18,
            )

    def set_game_window(self, game_window):
        self.game_window = game_window