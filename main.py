import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

from configparser import Config

def add_and_load_image(image_path, parent=None):
    width, height, channels, data = dpg.load_image(image_path)

    with dpg.texture_registry() as reg_id:
        texture_id = dpg.add_static_texture(width, height, data, parent=reg_id)

    if parent is None:
        return dpg.add_image(texture_id)
    else:
        return dpg.add_image(texture_id, parent=parent)

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=Config.screenWidth, height=Config.screenHeight, decorated=False)

with dpg.window(label="Tutorial", width=Config.screenWidth, height=Config.screenHeight, tag="Primary window"):
    with dpg.viewport_menu_bar():
        with dpg.menu(label="Console"):
            dpg.add_menu_item(label="Close", callback=dpg.stop_dearpygui)
        with dpg.menu(label="Demo"):
            dpg.add_menu_item(label="Launch", callback=demo.show_demo)
        with dpg.menu(label="Projects"):
            with dpg.menu(label="SSTV"):
                with dpg.menu(label="SSTV Encoder"):
                    add_and_load_image(image_path="assets/previews/menu/projects/SSTV/Encoder/preview.jpeg")
                    dpg.add_menu_item(label="SSTV Encoder")
                    dpg.add_menu_item(label="Convert PNG to WAV with Robot36, Robot72 and other modes")
                with dpg.menu(label="SSTV Decoder"):
                    dpg.add_menu_item(label="SSTV Decoder")
                    dpg.add_menu_item(label="Convert WAV Robot36 or Robot72 to PNG images")

dpg.setup_dearpygui()
dpg.show_viewport()
if Config.fullscreenBool:
    dpg.toggle_viewport_fullscreen()
dpg.set_primary_window("Primary window", True)
dpg.start_dearpygui()
dpg.destroy_context()