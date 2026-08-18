from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Optional: Set a dark background theme
Window.clearcolor = (0.1, 0.1, 0.12, 1)

class JarvisApp(App):
    def build(self):
        self.title = "J.A.R.V.I.S."
        
        # Main Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title Label
        self.title_label = Label(
            text="[b]J.A.R.V.I.S. AI SYSTEM[/b]",
            markup=True,
            font_size='22sp',
            size_hint=(1, 0.1),
            color=(0, 0.8, 1, 1)  # Cyan header
        )
        layout.add_widget(self.title_label)
        
        # Output Log Box
        self.output_label = Label(
            text="System online. Ready for commands, sir.",
            font_size='16sp',
            size_hint=(1, 0.6),
            color=(0.9, 0.9, 0.9, 1),
            text_size=(Window.width - 40, None),
            halign='left',
            valign='top'
        )
        layout.add_widget(self.output_label)
        
        # Input Section
        input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.15), spacing=10)
        
        self.user_input = TextInput(
            hint_text="Type a command...",
            multiline=False,
            size_hint=(0.75, 1),
            background_color=(0.2, 0.2, 0.25, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0, 0.8, 1, 1)
        )
        input_layout.add_widget(self.user_input)
        
        send_btn = Button(
            text="SEND",
            size_hint=(0.25, 1),
            background_color=(0, 0.6, 0.9, 1),
            color=(1, 1, 1, 1)
        )
        send_btn.bind(on_press=self.process_command)
        input_layout.add_widget(send_btn)
        
        layout.add_widget(input_layout)
        return layout

    def process_command(self, instance):
        text = self.user_input.text.strip()
        if not text:
            return
            
        # Basic response logic
        response = f"User: {text}\nJ.A.R.V.I.S.: Processing '{text}'..."
        
        if "hello" in text.lower():
            response = "J.A.R.V.I.S.: Hello, sir! All systems functioning normally."
        elif "status" in text.lower():
            response = "J.A.R.V.I.S.: Core modules operational. Online."
            
        self.output_label.text = response
        self.user_input.text = ""

if __name__ == '__main__':
    JarvisApp().run()
