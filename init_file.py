from tkinter import Tk

from Tkinter.new_tkinter.create_main_window import set_title, get_screen_result, set_geometry_main_window, main_loop


def init_function():
    root = Tk()
    width_screen_resolution, height_screen_resolution = get_screen_result(root)

    set_title(root)
    set_geometry_main_window(root, width_screen_resolution, height_screen_resolution)
    main_loop(root)


init_function()
