class BasePage:
    def __init__(self,page):
        self.page = page

    def click(self,selector):
        self.page.click(selector)

    def fill(self,selector,text):
        self.page.fill(selector,text)

    def get_text(self,selector):
        self.page.text_content(selector)

    def is_visible(self,selector):
        self.page.is_visible(selector)

    def dropdown(self,selector,value):
        self.page.select_option(selector,value=value)

    def hover(self,selector):
        self.page.hover(selector)


