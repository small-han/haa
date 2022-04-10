from ipyfilechooser import FileChooser
from ipywidgets import widgets
from IPython import display


class ShowProject(object):

    def __init__(self):
        self.output = widgets.Output()
        self.fc=FileChooser(".")

    def show_create_project(self):
        self.fc.title='<b>选择文件夹</b>'
        with self.output:
            display(self.fc)
        display(self.output)
        return self.fc.selected
