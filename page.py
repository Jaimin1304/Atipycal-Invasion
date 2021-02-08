import data_storage as ds
import game_obj as go

class page(object):

    def __init__(self):
        """
        """
        self.obj_lst = []
        self.tools_lst = []

    def handle_logic(self):
        """
        """
        for i in self.obj_lst:
            i.change_status()
        for i in self.tools_lst:
            i.run()


class start_menu(page):

    def __init__(self):
        """
        The start menu page.
        """
        self.play_txt = go.text(100,100,"Play")
        self.settings_txt = go.text(100,100,"Settings")
        self.help_txt = go.text(100,100,"Help")
        self.info_txt = go.text(100,100,"Info")
        self.quit_txt = go.text(100,100,"Quit")
        self.difficultly_txt = go.text(100,100,"diffculty")
        self.logo_pic = go.picture(100,100,0)