from python_json_config import ConfigBuilder

builder = ConfigBuilder()

config = builder.parse_config('config.json')

class Config:
    fullscreenBool = config.options.fullscreen

    screenWidth = config.screenDimensions.screenWidth
    screenHeight = config.screenDimensions.screenHeight