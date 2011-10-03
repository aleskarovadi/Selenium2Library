from robot.utils import ConnectionCache

class BrowserCache(ConnectionCache):

    def __init__(self):
        ConnectionCache.__init__(self, no_current_msg='No current browser')
        self._closed = set()
    
    def close(self):
        if self.current:
            browser = self.current
            browser.quit()
            self.current = self._no_current
            self.current_index = None
            self._closed.add(browser)

    def close_all(self):
        for browser in self._connections:
            if browser not in self._closed:
                browser.quit()
        self.empty_cache()
        return self.current
