

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """Kivy program to display names as different widgets."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Donald" , "Huey" , "Deuy" , "leuy" , "Scrooge" , "Daisy"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.names_box.add_widget(name_label)
        return self.root

    def create_name_label(self):
        name = self.root.ids.name_input.text
        self.root.ids.names_box.add_widget(Label(text=name))
        self.root.ids.name_input.text = ""



DynamicLabels().run()