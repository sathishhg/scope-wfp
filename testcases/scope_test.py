from selenium.webdriver.common.keys import Keys
from pages.scope import scopeLogin
from time import sleep


class ScopeLoginTest():

    @classmethod
    def setUpClass(self):
        super(ScopeLoginTest,self).setUpClass()
        self.scope = scopeLogin(self.driver)

    def setUp(self):
        self.errors_and_failures = self.tally()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
            self.loginpage.return_to_apps_main_page()

    def test_T_01_scope_login(self):
        self.scope = scopeLogin(self.driver)
        sleep(5)
        self.assertEqual("https://test.scope.wfp.org/login/?next=/")


