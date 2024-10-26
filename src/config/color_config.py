import json
import os

class ColorConfig:
    DEFAULT_PRIMARY_COLOR = "#4C721D"  
    DEFAULT_SECONDARY_COLOR = "#FFFFFF"  

    def __init__(self):
        self.primary_color = self.DEFAULT_PRIMARY_COLOR
        self.secondary_color = self.DEFAULT_SECONDARY_COLOR
        self.config_path = os.path.join(os.path.dirname(__file__), "color_settings.json")
        
        self.load_config()

    def load_config(self):
        """Loads color settings from color_settings.json if it exists"""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as file:
                    config = json.load(file)
                    self.primary_color = config.get("primary_color", self.primary_color)
                    self.secondary_color = config.get("secondary_color", self.secondary_color)
            except json.JSONDecodeError:
                self.save_config()
        else:
            self.save_config()

    def save_config(self):
        """Saves settings to color_settings.json"""
        with open(self.config_path, 'w') as file:
            json.dump({
                "primary_color": self.primary_color,
                "secondary_color": self.secondary_color
            }, file, indent=4)

    def revert_to_defaults(self):
        """Reverts colors to default UVU green and white, then saves"""
        self.primary_color = self.DEFAULT_PRIMARY_COLOR
        self.secondary_color = self.DEFAULT_SECONDARY_COLOR
        self.save_config()
