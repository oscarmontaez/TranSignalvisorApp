from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class TranSignalvisorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Bienvenida con estilo
        welcome_label = Label(text='¡Bienvenido a TranSignalvisor!', font_size=24, color=(0, 0.7, 1, 1))
        layout.add_widget(welcome_label)

        # Botones del menú
        signals_button = Button(text='Explorar Señales', on_press=self.show_signals, size_hint_y=None, height=50)
        quiz_button = Button(text='Test de Preguntas', on_press=self.show_question_form, size_hint_y=None, height=50)
        social_button = Button(text='Redes Sociales', on_press=self.show_social_links, size_hint_y=None, height=50)

        # Agregar botones al diseño
        layout.add_widget(signals_button)
        layout.add_widget(quiz_button)
        layout.add_widget(social_button)

        # Estilo de los botones
        for button in [signals_button, quiz_button, social_button]:
            button.background_color = (0, 0.7, 1, 1)
            button.color = (1, 1, 1, 1)
            button.font_size = 18

        return layout

    def show_signals(self, instance):
        # Lista de nombres de archivos de imágenes
        self.image_files = ['senal1.png', 'senal2.png', 'senal3.png','senal4.png','senal5.png','senal6.png','senal7.png']  # Agrega más nombres de archivos según sea necesario

        # Lista de descripciones correspondientes a cada imagen
        self.descriptions = [
            'Señal 1. Flujo de vehiculos en doble sentido',
            'Señal 2. Señal de pare para que un vehiculo se detenga antes de un cruce',
            'Señal 3. Prohibido hacer giro a la izquierda',
            'Señal 4. Prohibido hacer giro en U en esa via',
            'Señal 5. Prohibido la circulacion de vehiculos',
            'Señal 6. Prohibido adelantar vehiculos',
            'Señal 7. Prohibido parquear vehiculos'
        ]  # Ajusta las descripciones según tus necesidades

        # Crear una nueva ventana emergente para mostrar imágenes de señales de tráfico
        popup_layout = BoxLayout(orientation='vertical')
        self.image_index = 0
        self.image = Image(source=self.image_files[self.image_index], allow_stretch=True, size_hint=(1, 0.6))
        popup_layout.add_widget(self.image)

        # ScrollView para la descripción
        description_scrollview = ScrollView(size_hint=(1, None), size=(400, 150))
        self.description_label = Label(text=self.descriptions[self.image_index], size_hint_y=None,
                                       height=description_scrollview.height)
        self.description_label.bind(size=self.description_label.setter('text_size'))
        description_scrollview.add_widget(self.description_label)
        popup_layout.add_widget(description_scrollview)

        # Botón "Siguiente" estilizado y centrado
        next_button = Button(text='Siguiente', on_press=self.change_image, size_hint=(None, None), size=(150, 50),
                             background_color=(0, 0.7, 1, 1), color=(1, 1, 1, 1), font_size=16, pos_hint={'center_x': 0.5})
        popup_layout.add_widget(next_button)

        popup = Popup(title='Señales de Tráfico', content=popup_layout, size_hint=(None, None), size=(500, 500))
        popup.open()

    def change_image(self, instance):
        # Incrementar el índice de la imagen
        self.image_index = (self.image_index + 1) % len(self.image_files)
        self.image.source = self.image_files[self.image_index]
        self.description_label.text = self.descriptions[self.image_index]


    def show_question_form(self, instance):
        # Crear una nueva ventana emergente para el formulario de preguntas
        popup_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Preguntas y opciones de respuesta
        questions = [
            {
                "question_text": "¿Cuál es el significado de la señal de tráfico con una P y una banda cruzada?",
                "options": ["Prohibido parar", "Prohibido parquear", "Prohibido pasar"]
            },
            {
                "question_text": "¿Qué acción no debes realizar al ver la señal con una flecha y una banda?",
                "options": ["Girar en sentido de la flecha", "No girar en ese sentido", "Omitir la señal"]
            }
        ]

        # Crear widgets para las preguntas y opciones de respuesta
        for question_data in questions:
            question_label = Label(text=question_data["question_text"], font_size=18, color=(0, 0.7, 1, 1))
            popup_layout.add_widget(question_label)

            # Contenedor para CheckBoxes centrados
            checkbox_container = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            popup_layout.add_widget(checkbox_container)

            # Crear CheckBoxes para cada opción de respuesta
            for option_text in question_data["options"]:
                checkbox = CheckBox(group=question_data["question_text"], size_hint=(None, None), size=(50, 50),
                                    active=False, color=(1, 1, 1, 1))  # Cambiado el color del texto a blanco
                option_label = Label(text=option_text, font_size=16, color=(1, 1, 1, 1))  # Cambiado el color del texto a blanco
                checkbox_container.add_widget(checkbox)
                checkbox_container.add_widget(option_label)

        # Botón de enviar respuestas
        submit_button = Button(text='Enviar Respuestas', on_press=self.submit_answers, size_hint_y=None, height=50,
                               background_color=(0, 0.7, 1, 1), color=(1, 1, 1, 1), font_size=18)
        popup_layout.add_widget(submit_button)

        # Crear la ventana emergente
        popup = Popup(title='Test de Preguntas', content=popup_layout, size_hint=(None, None), size=(600, 400))
        popup.open()

    def submit_answers(self, instance):
        # Implementación para procesar las respuestas del usuario
        # Puedes acceder a las respuestas a través de los widgets CheckBox en el diseño de la ventana emergente
        print("Respuestas enviadas")

    def show_social_links(self, instance):
        # Crear una nueva ventana emergente para mostrar enlaces a redes sociales
        social_layout = GridLayout(cols=1, spacing=10, padding=20)
        social_layout.add_widget(Button(text='Facebook', on_press=self.open_facebook, size_hint_y=None, height=50))
        social_layout.add_widget(Button(text='Instagram', on_press=self.open_instagram, size_hint_y=None, height=50))
        social_layout.add_widget(Button(text='Twitter', on_press=self.open_twitter, size_hint_y=None, height=50))
        social_layout.add_widget(Button(text='Cerrar', on_press=lambda x: popup.dismiss(), size_hint_y=None, height=50))

        popup = Popup(title='Redes Sociales', content=social_layout, size_hint=(None, None), size=(500, 350))
        popup.open()

    def open_facebook(self, instance):
        print('Abriendo enlace de Facebook')

    def open_instagram(self, instance):
        print('Abriendo enlace de Instagram')

    def open_twitter(self, instance):
        print('Abriendo enlace de Twitter')

if __name__ == '__main__':
    TranSignalvisorApp().run()