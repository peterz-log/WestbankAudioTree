from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

# ---------------------------------------------------------
# Westbank Audio Tree
# Many Voices. One Community.
# ---------------------------------------------------------

Window.clearcolor = (0.055, 0.07, 0.065, 1)


class WestbankApp(App):

    def build(self):
        self.title = "Westbank Audio Tree"
        self.sound = None
        self.language = "English"
        self.current_title = "Welcome to Westbank Audio Tree"

        root = BoxLayout(
            orientation="vertical",
            spacing=dp(6),
            padding=dp(10)
        )

        # ---------------- TOP BAR ----------------
        top = BoxLayout(
            size_hint_y=None,
            height=dp(58),
            spacing=dp(8)
        )

        logo = Label(
            text="[b]🌳 WESTBANK[/b]\n[size=11]Audio Tree[/size]",
            markup=True,
            halign="left",
            valign="middle",
            color=(0.45, 1, 0.55, 1)
        )
        top.add_widget(logo)

        language_btn = Button(
            text="🌐 English",
            size_hint_x=None,
            width=dp(105),
            background_normal="",
            background_color=(0.12, 0.18, 0.15, 1)
        )
        language_btn.bind(on_release=self.toggle_language)
        top.add_widget(language_btn)

        root.add_widget(top)

        # ---------------- SEARCH ----------------
        search = TextInput(
            hint_text="Search stories, farming, finance, faith...",
            multiline=False,
            size_hint_y=None,
            height=dp(46),
            background_color=(0.11, 0.13, 0.12, 1),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.55, 0.6, 0.57, 1),
            padding=[dp(14), dp(12)]
        )
        root.add_widget(search)

        # ---------------- CONTENT ----------------
        scroll = ScrollView()

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(14),
            size_hint_y=None,
            padding=[dp(4), dp(10)]
        )
        content.bind(minimum_height=content.setter("height"))

        # HERO
        hero = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(8),
            size_hint_y=None,
            height=dp(170)
        )

        hero.add_widget(Label(
            text="[b]Many Voices.\nOne Community.[/b]",
            markup=True,
            font_size=dp(25),
            color=(1, 1, 1, 1),
            halign="left"
        ))

        hero.add_widget(Label(
            text="Listen. Learn. Connect. Grow.\n"
                 "Discover stories and knowledge from Malawi.",
            font_size=dp(14),
            color=(0.72, 0.76, 0.74, 1)
        ))

        content.add_widget(hero)

        # FEATURED
        content.add_widget(Label(
            text="[b]🔥 Featured today[/b]",
            markup=True,
            font_size=dp(19),
            size_hint_y=None,
            height=dp(35),
            halign="left"
        ))

        featured = BoxLayout(
            orientation="vertical",
            padding=dp(16),
            spacing=dp(7),
            size_hint_y=None,
            height=dp(145)
        )

        featured.add_widget(Label(
            text="[b]Episode 1: Sena Voices, Shire Rhythms[/b]",
            markup=True,
            font_size=dp(17),
            color=(1, 1, 1, 1)
        ))

        featured.add_widget(Label(
            text="Community stories • Lower Shire • 5 min",
            color=(0.65, 0.7, 0.67, 1)
        ))

        play = Button(
            text="▶  PLAY EPISODE",
            size_hint_y=None,
            height=dp(45),
            background_normal="",
            background_color=(0.15, 0.75, 0.35, 1),
            color=(0, 0, 0, 1)
        )
        play.bind(on_release=self.play_episode)
        featured.add_widget(play)

        content.add_widget(featured)

        # CATEGORIES
        content.add_widget(Label(
            text="[b]Explore categories[/b]",
            markup=True,
            font_size=dp(19),
            size_hint_y=None,
            height=dp(35)
        ))

        categories = GridLayout(
            cols=2,
            spacing=dp(8),
            size_hint_y=None
        )
        categories.bind(minimum_height=categories.setter("height"))

        category_data = [
            ("🌱", "Development"),
            ("💰", "Finance"),
            ("⚖️", "Civic & Law"),
            ("⚽", "Sports"),
            ("📜", "History"),
            ("🪘", "Culture"),
            ("✝️", "God's Word"),
            ("🎙️", "Community Voices"),
        ]

        for icon, name in category_data:
            btn = Button(
                text=f"{icon}  {name}",
                size_hint_y=None,
                height=dp(65),
                background_normal="",
                background_color=(0.11, 0.15, 0.13, 1),
                color=(1, 1, 1, 1)
            )
            btn.bind(on_release=lambda instance, n=name:
                     self.category_selected(n))
            categories.add_widget(btn)

        content.add_widget(categories)

        # LIBRARY
        content.add_widget(Label(
            text="[b]Your audio library[/b]",
            markup=True,
            font_size=dp(19),
            size_hint_y=None,
            height=dp(35)
        ))

        library = BoxLayout(
            orientation="vertical",
            spacing=dp(7),
            size_hint_y=None,
            height=dp(150)
        )

        library.add_widget(self.library_button(
            "🎧  Latest community stories"
        ))
        library.add_widget(self.library_button(
            "📥  Offline downloads"
        ))
        library.add_widget(self.library_button(
            "❤️  Saved episodes"
        ))

        content.add_widget(library)

        # SUPPORT
        support = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(8),
            size_hint_y=None,
            height=dp(135)
        )

        support.add_widget(Label(
            text="[b]Support Westbank Audio Tree[/b]",
            markup=True,
            font_size=dp(17)
        ))

        support.add_widget(Label(
            text="Help us give local voices a place to be heard.",
            color=(0.7, 0.74, 0.72, 1)
        ))

        donate = Button(
            text="❤️  SUPPORT / DONATE",
            size_hint_y=None,
            height=dp(42),
            background_normal="",
            background_color=(0.16, 0.45, 0.28, 1)
        )
        donate.bind(on_release=self.support)
        support.add_widget(donate)

        content.add_widget(support)

        scroll.add_widget(content)
        root.add_widget(scroll)

        # ---------------- MINI PLAYER ----------------
        mini = BoxLayout(
            size_hint_y=None,
            height=dp(68),
            spacing=dp(8),
            padding=dp(6)
        )

        self.mini_title = Label(
            text="Nothing playing",
            halign="left",
            valign="middle"
        )

        mini.add_widget(self.mini_title)

        self.pause_button = Button(
            text="▶",
            size_hint_x=None,
            width=dp(55),
            background_normal="",
            background_color=(0.15, 0.75, 0.35, 1)
        )
        self.pause_button.bind(on_release=self.pause_resume)
        mini.add_widget(self.pause_button)

        root.add_widget(mini)

        # ---------------- BOTTOM NAVIGATION ----------------
        nav = BoxLayout(
            size_hint_y=None,
            height=dp(55),
            spacing=dp(4)
        )

        for text in ["🏠 Home", "🎧 Library", "📥 Offline", "❤️ Support"]:
            btn = Button(
                text=text,
                font_size=dp(11),
                background_normal="",
                background_color=(0.08, 0.11, 0.1, 1)
            )
            btn.bind(on_release=self.navigation)
            nav.add_widget(btn)

        root.add_widget(nav)

        return root

    # -----------------------------------------------------
    # Helper button
    # -----------------------------------------------------

    def library_button(self, text):
        btn = Button(
            text=text,
            size_hint_y=None,
            height=dp(43),
            background_normal="",
            background_color=(0.1, 0.13, 0.12, 1)
        )
        return btn

    # -----------------------------------------------------
    # Audio
    # -----------------------------------------------------

    def play_episode(self, instance):
        self.current_title = "Sena Voices, Shire Rhythms"
        self.mini_title.text = "▶  " + self.current_title
        self.pause_button.text = "⏸"

        # Replace this URL later with your real MP3.
        audio_url = (
            "https://www.soundhelix.com/examples/mp3/"
            "SoundHelix-Song-1.mp3"
        )

        try:
            if self.sound:
                self.sound.stop()

            self.sound = SoundLoader.load(audio_url)

            if self.sound:
                self.sound.play()
        except Exception:
            pass

    def pause_resume(self, instance):
        if not self.sound:
            return

        try:
            if self.pause_button.text == "⏸":
                self.sound.stop()
                self.pause_button.text = "▶"
            else:
                self.sound.play()
                self.pause_button.text = "⏸"
        except Exception:
            pass

    # -----------------------------------------------------
    # Language
    # -----------------------------------------------------

    def toggle_language(self, instance):
        if self.language == "English":
            self.language = "Chisena"
            instance.text = "🌐 Chisena"
        else:
            self.language = "English"
            instance.text = "🌐 English"

    # -----------------------------------------------------
    # Category
    # -----------------------------------------------------

    def category_selected(self, category):
        self.mini_title.text = "Selected: " + category

    # -----------------------------------------------------
    # Navigation
    # -----------------------------------------------------

    def navigation(self, instance):
        self.mini_title.text = instance.text

    # -----------------------------------------------------
    # Support
    # -----------------------------------------------------

    def support(self, instance):
        self.mini_title.text = "❤️ Thank you for supporting Westbank!"

    # -----------------------------------------------------
    # App lifecycle
    # -----------------------------------------------------

    def on_stop(self):
        if self.sound:
            try:
                self.sound.stop()
            except Exception:
                pass


if __name__ == "__main__":
    WestbankApp().run()
