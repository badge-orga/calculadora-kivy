from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.utils import platform
from kivy.core.window import Window
from kivy.clock import Clock


class x(Screen):
    pass
class Navigator(Screen):
    pass

class SplashScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class Calculator(Screen):
    def on_press(self, button):
        current_text = self.ids.display.text
        new_text = current_text + button
        self.ids.display.text = new_text

    def calculate(self):
        try:
            expression = str(eval(self.ids.display.text))
            self.ids.display.text = expression
        except Exception as e:
            self.ids.display.text = 'Error'

    def clear(self):
        self.ids.display.text = ''

class CalculatorApp(MDApp):

    sm = ScreenManager()
    sm.add_widget(Calculator(name='Calculadora'))
    sm.add_widget(SplashScreen(name='splashscreen'))
    sm.add_widget(AboutScreen(name='about'))

    def build(self):
        Window.size = (290,500)
        screen = Builder.load_file('kv.kv')
        return screen


    def on_start(self):
        Clock.schedule_once(self.splash, 5)

    def splash(self,*args):
        self.root.current  = "firstscreen"


if __name__ == '__main__':
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    CalculatorApp().run()
