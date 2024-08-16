from krita import DockWidget, DockWidgetFactory, DockWidgetFactoryBase

DOCKER_NAME = 'DGPP'
DOCKER_ID = 'pyKrita_DGPP'

class DGPP(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(DOCKER_NAME) 

    def canvasChanged(self, canvas):
        pass

instance = Krita.instance()
dock_widget_factory = DockWidgetFactory(DOCKER_ID, 
    DockWidgetFactoryBase.DockRight, 
    DGPP)

instance.addDockWidgetFactory(dock_widget_factory)