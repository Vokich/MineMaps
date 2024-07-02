from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest
import webbrowser
import requests
import re
from bs4 import BeautifulSoup

KV = '''
Screen:

    ScreenManager:
        id: screen_manager

        Screen:
            name: 'main_menu'    

            BoxLayout:
                orientation: 'vertical'

                MDTopAppBar:
                    title: 'Menu'
                    md_bg_color: 30/255, 144/255, 255/255
                    specific_text_color: 1, 1, 1, 1

                MDBottomNavigation:

                    MDBottomNavigationItem:
                        name: 'Maps'
                        text: 'Maps'
                        icon: 'map'

                        ScrollView:
                            GridLayout:
                                cols: 2

                                MDSmartTile:
                                    radius: 24
                                    box_radius: [0, 0, 24, 24]
                                    source: 'Shrum.png'
                                    box_color: 1, 1, 1, .2
                                    size_hint: None, None
                                    size: "220dp", "220dp"
                                    MDRaisedButton:
                                        text: "MDRaisedButton"
                                        md_bg_color: "red"
                                        on_release: app.parkur()

                                MDSmartTile:
                                    radius: 24
                                    box_radius: [0, 0, 24, 24]
                                    source: 'Shrum.png'
                                    box_color: 1, 1, 1, .2
                                    size_hint: None, None
                                    size: "220dp", "220dp"
                                    MDRaisedButton:
                                        text: "MDRaisedButton"
                                        md_bg_color: "blue"
                                        on_release: app.parkur()

                                MDSmartTile:
                                    radius: 24
                                    box_radius: [0, 0, 24, 24]
                                    source: 'Shrum.png'
                                    box_color: 1, 1, 1, .2
                                    size_hint: None, None
                                    size: "220dp", "220dp"
                                    MDRaisedButton:
                                        text: "MDRaisedButton"
                                        md_bg_color: "red"
                                        on_release: app.parkur()

                                MDSmartTile:
                                    radius: 24
                                    box_radius: [0, 0, 24, 24]
                                    source: 'Shrum.png'
                                    box_color: 1, 1, 1, .2
                                    size_hint: None, None
                                    size: "220dp", "220dp"
                                    MDRaisedButton:
                                        text: "MDRaisedButton"
                                        md_bg_color: "green"
                                        on_release: app.parkur()

                    MDBottomNavigationItem:
                        name: 'Mods'
                        text: 'Mods'
                        icon: 'linkedin'

                        ScrollView:
                            GridLayout:
                                cols: 2

                                MDSmartTile:
                                    radius: 24
                                    box_radius: [0, 0, 24, 24]
                                    source: 'Shrum.png'
                                    box_color: 1, 1, 1, .2
                                    size_hint: None, None
                                    size: "220dp", "220dp"
                                    MDRaisedButton:
                                        text: "MDRaisedButton"
                                        md_bg_color: "red"
                                        on_release: app.sirenhead()

                                MDSmartTile:
                                    radius: 24
                                    box_radius: [0, 0, 24, 24]
                                    source: 'Shrum.png'
                                    box_color: 1, 1, 1, .2
                                    size_hint: None, None
                                    size: "220dp", "220dp"
                                    MDRaisedButton:
                                        text: "MDRaisedButton"
                                        md_bg_color: "blue"
                                        on_release: app.sirenhead()

                                MDSmartTile:
                                    radius: 24
                                    box_radius: [0, 0, 24, 24]
                                    source: 'Shrum.png'
                                    box_color: 1, 1, 1, .2
                                    size_hint: None, None
                                    size: "220dp", "220dp"
                                    MDRaisedButton:
                                        text: "MDRaisedButton"
                                        md_bg_color: "red"
                                        on_release: app.sirenhead()

                                MDSmartTile:
                                    radius: 24
                                    box_radius: [0, 0, 24, 24]
                                    source: 'Shrum.png'
                                    box_color: 1, 1, 1, .2
                                    size_hint: None, None
                                    size: "220dp", "220dp"
                                    MDRaisedButton:
                                        text: "MDRaisedButton"
                                        md_bg_color: "green"
                                        on_release: app.sirenhead()

                    MDBottomNavigationItem:
                        name: 'Texture packs'
                        text: 'Texture packs'
                        icon: 'github'

                        ScrollView:
                            GridLayout:
                                cols: 2

                                MDSmartTile:
                                    radius: 24
                                    box_radius: [0, 0, 24, 24]
                                    source: 'Shrum.png'
                                    box_color: 1, 1, 1, .2
                                    size_hint: None, None
                                    size: "220dp", "220dp"
                                    MDRaisedButton:
                                        text: "MDRaisedButton"
                                        md_bg_color: "red"
                                        on_release: app.ruda()

                                MDSmartTile:
                                    radius: 24
                                    box_radius: [0, 0, 24, 24]
                                    source: 'Shrum.png'
                                    box_color: 1, 1, 1, .2
                                    size_hint: None, None
                                    size: "220dp", "220dp"
                                    MDRaisedButton:
                                        text: "MDRaisedButton"
                                        md_bg_color: "blue"
                                        on_release: app.ruda()
                                        
                                MDSmartTile:
                                    radius: 24
                                    box_radius: [0, 0, 24, 24]
                                    source: 'Shrum.png'
                                    box_color: 1, 1, 1, .2
                                    size_hint: None, None
                                    size: "220dp", "220dp"
                                    MDRaisedButton:
                                        text: "MDRaisedButton"
                                        md_bg_color: "red"
                                        on_release: app.ruda()

                                MDSmartTile:
                                    radius: 24
                                    box_radius: [0, 0, 24, 24]
                                    source: 'Shrum.png'
                                    box_color: 1, 1, 1, .2
                                    size_hint: None, None
                                    size: "220dp", "220dp"
                                    MDRaisedButton:
                                        text: "MDRaisedButton"
                                        md_bg_color: "green"
                                        on_release: app.ruda()

        Screen:
            name: 'parkur_screen'

            MDLabel:
                text: "Гартен оф Бан Бан"
                color: (0.5, 0.5, 0.5, 1)
                font_size: 45
                halign: 'center'

            MDLabel:
                id: content_label
                text: "Loading..."
                halign: 'center'
                pos_hint: {"center_x": .5, "center_y": .3}
            MDRaisedButton:
                text: "Скачать"
                md_bg_color: "red"
                on_release: app.search('https://mcpeland.io/maps/1377-karta-ostrova-parkura.html')
                pos_hint: {"center_x":.5,  "center_y": .07}
            MDRaisedButton:
                text: "Выйти"
                md_bg_color: "red"
                on_release: app.back_to_menu()
                pos_hint: {"center_x":.1,  "center_y": .9}

        Screen:
            name: 'sirenhead_screen'

            MDLabel:
                text: "Sirenhead mode"
                color: (0.5, 0.5, 0.5, 1)
                font_size: 45
                halign: 'center'
            MDLabel:
                id: sirenhead_content
                text: "Loading1..."
                halign: 'center'
                pos_hint: {"center_x": .5, "center_y": .3}
            MDRaisedButton:
                text: "Скачать"
                md_bg_color: "red"
                on_release: app.search('https://mcpeland.io/mods/1392-mod-sirenogolovyj-2018.html')
                pos_hint: {"center_x":.5,  "center_y": .07}
            MDRaisedButton:
                text: "Выйти"
                md_bg_color: "red"
                on_release: app.back_to_menu()
                pos_hint: {"center_x":.1,  "center_y": .9}

        Screen:
            name: 'ruda_screen'

            MDLabel:
                text: "Мерцающая руда"
                color: (0.5, 0.5, 0.5, 1)
                font_size: 45
                halign: 'center'
            MDLabel:
                id: ruda_content
                text: "Loading2..."
                halign: 'center'
                pos_hint: {"center_x": .5, "center_y": .3}
            MDRaisedButton:
                text: "Скачать"
                md_bg_color: "red"
                on_release: app.search('https://mcpeland.io/textures/1114-tekstury-mercajuschaja-ruda.html')
                pos_hint: {"center_x":.5,  "center_y": .07}
            MDRaisedButton:
                text: "Выйти"
                md_bg_color: "red"
                on_release: app.back_to_menu()
                pos_hint: {"center_x":.1,  "center_y": .9}



'''


class MineMaps(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def back_to_menu(self):
        self.root.ids.screen_manager.current = 'main_menu'

    def parkur(self):
        self.root.ids.screen_manager.current = 'parkur_screen'

    def ruda(self):
        self.root.ids.screen_manager.current = 'ruda_screen'
        self.load_ruda_content()

    def load_ruda_content(self):
        url = "https://mcpeland.io/textures/1114-tekstury-mercajuschaja-ruda.html"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_tags = soup.find_all('meta')
            meta_content = ' '.join([meta['content'][:50] for meta in meta_tags if 'content' in meta.attrs])
            self.root.ids.ruda_content.text = meta_content
        else:
            self.root.ids.ruda_content.text = "Failed to fetch data"

    def sirenhead(self):
        self.root.ids.screen_manager.current = 'sirenhead_screen'
        self.load_sirenhead_content()

    def load_sirenhead_content(self):
        url = "https://mcpeland.io/mods/1392-mod-sirenogolovyj-2018.html"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_tags = soup.find_all('meta')
            meta_content = ' '.join([meta['content'][:50] for meta in meta_tags if 'content' in meta.attrs])
            self.root.ids.sirenhead_content.text = meta_content
        else:
            self.root.ids.sirenhead_content.text = "Failed to fetch data"

    def search(self, url):
        webbrowser.open(url)

    def on_start(self):
        self.load_text_from_url("https://mcpeland.io/maps/1041-karta-garten-of-banban-2.html")

    def load_text_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_tags = soup.find_all('meta')
            meta_content = ' '.join([meta['content'][:50] for meta in meta_tags if 'content' in meta.attrs])
            self.root.ids.content_label.text = meta_content
        else:
            self.root.ids.content_label.text = "Failed to fetch data"

if __name__ == '__main__':
    MineMaps().run()