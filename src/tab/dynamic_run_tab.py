from src.tab.run import RunTab
from src.config.color_config import ColorConfig

class DynamicRunTab(RunTab):
    def __init__(self, tab_name, tab_manager, color_config):
        """Creates a new tab that inherits from RunTab"""
        self.tab_name = tab_name  
        self.tab_manager = tab_manager  
        self.color_config = color_config  

        tab = self.tab_manager.new_tab(tab_name)
        
        super().__init__(tab, self.color_config)