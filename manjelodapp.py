# region IMPORTS....................................................................................
# IMPORTING OTHER LIBRARIES
import manjelodback as mlb
import time

# IMPORTING KIVY LIBRARIES
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

# endregion
# region WINDOWS SIZE MANAGEMENT....................................................................
screenlength = 800
aspectratio = 9/16
# manually setting in script
Window.size = (aspectratio * screenlength, screenlength) 

from kivy.clock import Clock

class MyScreenManager(ScreenManager):
    """This class is the base of the app. It is necessary because of the multiple menus that will be implemented."""
    def __init__(self):
        super(MyScreenManager, self).__init__()
    pass

# endregion
# region SCREENS....................................................................................
class HomeScreen(Screen):
    pass

class SettingScreen(Screen):
    pass

class ActivityScreen(Screen):
    pass

class StatScreen(Screen):
    pass

class TimelineScreen(Screen):
    pass

# endregion
# region BUILDING APP...............................................................................

class TimeTracker(App):
    def build(self):
        # Create the screen manager
        sm = MyScreenManager()

        # adding all the screens to the screen manager
        sm.add_widget(HomeScreen(name='menu')) # screen menu = children 0
        sm.add_widget(SettingScreen(name='settings')) # children 1
        sm.add_widget(ActivityScreen(name = 'set activity')) # children 2
        sm.add_widget(StatScreen(name = 'stats')) # children 3
        sm.add_widget(TimelineScreen(name = 'timeline')) # children 4

        # adding widgets to the screens
        # Menu Screen:
        # sm.children[0].add_widget(MyRoot()) # we set the MyRoot Boxlayout inside the "Menu" screen (we should rename Myroot)

        return sm

class Manjelodapp(App):
    def build(self):
        return

if __name__ == '__main__':
    # stating an instance of the app
    Manjelodapp().run()

####################################################################################################

# for desktop OS you can set min values
# Window.minimum_width, Window.minimum_height = (aspectratio * screenlength, screenlength)

# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button
# from kivy.uix.image import Image
# from kivy.uix.textinput import TextInput
# from kivy.uix.label import Label
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.widget import Widget
# from kivy.uix.anchorlayout import AnchorLayout

# class SpotifyCloneApp(App):
#     def build(self):
#         root = BoxLayout(orientation='vertical')
        
#         # Header Section
#         header = BoxLayout(size_hint_y=0.1, padding=[10, 10, 10, 10])
#         header.add_widget(Label(text='Spotify', font_size='24sp', bold=True, size_hint_x=0.9))
#         header.add_widget(Button(text='Profile', size_hint_x=0.1))

#         # Search Bar
#         search_bar = BoxLayout(size_hint_y=0.1, padding=[10, 10, 10, 10])
#         search_bar.add_widget(TextInput(hint_text='Search for artists, albums, or songs', size_hint_x=0.9))
#         search_bar.add_widget(Button(text='🔍', size_hint_x=0.1))

#         # Navigation Bar
#         nav_bar = BoxLayout(size_hint_y=0.1, padding=[10, 10, 10, 10])
#         nav_bar.add_widget(Button(text='Home', size_hint_x=0.33))
#         nav_bar.add_widget(Button(text='Search', size_hint_x=0.33))
#         nav_bar.add_widget(Button(text='Your Library', size_hint_x=0.33))

#         # Playlist Grid Section
#         playlist_section = ScrollView(size_hint_y=0.7)
#         grid = GridLayout(cols=3, padding=[10, 10], spacing=10, size_hint_y=None)
#         grid.bind(minimum_height=grid.setter('height'))

#         # Add some sample playlist album images to the grid
#         for i in range(12):
#             img = Image(source=f'path/to/album_cover{i % 5 + 1}.jpg', size_hint_y=None, height=200)
#             grid.add_widget(img)

#         playlist_section.add_widget(grid)

#         # Add everything to the root layout
#         root.add_widget(header)
#         root.add_widget(search_bar)
#         root.add_widget(nav_bar)
#         root.add_widget(playlist_section)

#         return root

# if __name__ == '__main__':
#     SpotifyCloneApp().run()
