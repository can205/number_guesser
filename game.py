from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button


class Game_Window(GridLayout):
#    def build(self):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       print("hi")
       self.cols = 1
       self.size_hint=(1 , 1)
       self.pos_hint = {
        "center_x": 0.5,
        "center_y": 0.5,
       }



       self.add_widget(Image(source ="./number.Guesser.drawio.png"))
       self.Title = Label(text = "Number Guesser")
       self.add_widget(self.Title)
       print("hsi")

       self.question = TextInput( 
           text= "choose your number range:",
        #    size_hint=(10),
           )
       self.add_widget(self.question)

       self.start_button = Button (
           text = "Start",
           size_hint = (1, 0.5),
           )
       self.start_button.bind(on_press = self.start_button_behavior)
       self.add_widget(self.start_button)
   def start_button_behavior(self, *args):
       print('Push button')
       self.Title.text = f"Guess Number {self.question.text}"
       return
   


class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.game_window = Game_Window()
        screen = Screen(name = "game_window")
        screen.add_widget(self.game_window)
        self.screen_manager.add_widget(screen)
        self.screen_manager.current = 'game_window'
        return self.screen_manager
   



      


if __name__ == "__main__":
  app =MyApp()
  app.run()
    
 
 


