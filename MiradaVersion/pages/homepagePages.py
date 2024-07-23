from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
from MiradaVersion.object.loginObject import loginObject
from MiradaVersion.object.homeObject import homeObject
import time


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.loginObj = loginObject()
        self.homeObj = homeObject()

    def assertHomePage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.ID, self.homeObj.txt_vision_logo))
            )
            print("Assert Success : Assert Homepage Logo Success")
        except AssertionError:
            print("Assert Failed : Assert Homepage Logo Failed")

    def clickMenuButton(self):

        btn_menu = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_menu_button))
        )
        btn_menu.click()

    def assertMenu(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.homeObj.img_home))
            )
            print("Assert Success : Assert Menu Button Success")
        except AssertionError:
            print("Assert Failed : Assert Menu Button Failed")

    def clickSettingsButton(self):

        btn_settings_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_settings_button))
        )
        btn_settings_button.click()

    def assertSettingsPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_settings_page)
                )
            )
            print("Assert Success : Assert Settings Page Success")
        except AssertionError:
            print("Assert Failed : Assert Settings Page Failed")

    def clickSettingsProfile(self):

        settings_profile = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homeObj.txt_settings_account_profile)
            )
        )
        settings_profile.click()

    def assertSettingsAccountPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_account_page)
                )
            )
            print("Assert Success : Assert Account Page Success")
        except AssertionError:
            print("Assert Failed : Assert Account Page Failed")

    def clickLogoutButton(self):

        logout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_logout))
        )
        logout_button.click()

    def clickLiveTvMenu(self):

        live_tv_menu = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.img_live_tv))
        )
        live_tv_menu.click()

    def clickBtnProfile(self):

        btn_profile = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_profile))
        )
        btn_profile.click()

    def clickBtnSearch(self):

        btn_search = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.btn_search))
        )
        btn_search.click()

    def assertSearchPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_search_page)
                )
            )
            print("Assert Success : Assert Search Success")
        except AssertionError:
            print("Assert Failed : Assert Search Failed")

    def inputSearch(self, keyword):
        self.wait = WebDriverWait(self.driver, 20)

        fld_search = self.driver.find_element(By.ID, self.homeObj.fld_search)

        fld_search.clear()
        fld_search.click()
        time.sleep(3)
        fld_search.send_keys(keyword)
        time.sleep(3)
        self.driver.press_keycode(4)

    def clickResultOne(self):

        result = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.result_search_one))
        )
        result.click()

    def clickResultTwo(self):

        result_two = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.result_search_two))
        )
        result_two.click()

    def clickResultLiveTV(self):

        result_tv = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.result_search_livetv))
        )
        result_tv.click()

    def assertSearchNoResult(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, self.homeObj.txt_search_no_result)
                )
            )
            print("Assert Success : Assert Search  No Result Success")
        except AssertionError:
            print("Assert Failed : Assert Search  No Result  Failed")

    def clickProgramGuide(self):

        guide = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.img_program_guide))
        )
        guide.click()

    def clickBanner(self):

        banner = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.detail_banner))
        )
        banner.click()

    def clickViewlAllVplusOriginals(self):

        view_all = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.homeObj.txt_viewl_all_cluster_originals)
            )
        )
        view_all.click()

    def assertBannerInfo(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.ID, self.homeObj.detail_banner))
            )
            print("Assert Success : Assert Banner Info Success")
        except AssertionError:
            print("Assert Failed : Assert Banner Info Failed")

    def clickContent(self):

        content = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homeObj.txt_first_view_all_cluster_originals)
            )
        )
        content.click()

    def clickContentClusterVplusOriginals(self):

        content = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homeObj.txt_content_detail_cluster_vplus_originals)
            )
        )
        content.click()

    def clickChannelClusterLivetv(self):

        clusterLivetv = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homeObj.txt_channel_cluster_live_tv)
            )
        )
        clusterLivetv.click()

    def assertClusterLiveTV(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_channel_cluster_live_tv)
                )
            )
            print("Assert Success : Assert Cluster Live TV Success")
        except AssertionError:
            print("Assert Failed : Assert Cluster Live TV  Failed")

    def clickMenuHome(self):

        home = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.img_home))
        )
        home.click()

    def clickContentClusterTop10(self):

        content_cluster_top10 = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homeObj.txt_content_cluster_10_this_week)
            )
        )
        content_cluster_top10.click()

    def assertClusterWatchlist(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_cluster_watchlist)
                )
            )
            print("Assert Success : Assert Cluster Watchlist Success")
        except AssertionError:
            print("Assert Failed : Assert Cluster Watchlist Failed")

    def clickBtnProfile(self):

        btn_profile = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_profile))
        )
        btn_profile.click()

    def assertClusterNewReleases(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_cluster_new_releases)
                )
            )
            print("Assert Success : Assert Cluster New Releases Success")
        except AssertionError:
            print("Assert Failed : Assert Cluster New Releases Failed")

    def clickContentClusterNewReleases(self):

        content__new_release = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homeObj.content_cluster_new_releases)
            )
        )
        content__new_release.click()

    def clickActionGenre(self):

        action_genre = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.txt_genre_action))
        )
        action_genre.click()

    def clickContentActionGenre(self):

        content_action_genre = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.content_genre_action))
        )
        content_action_genre.click()

    def clickTheActors(self):

        actors = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.btn_popular_actors))
        )
        actors.click()

    def clickContentPopularActors(self):

        content_actors = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.content_popular_actors))
        )
        content_actors.click()

    def assertClusterExplorebyGenre(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.cluster_genre_action)
                )
            )
            print("Assert Success : Assert Cluster Explore by Genre Success")
        except AssertionError:
            print("Assert Failed : Assert Cluster Explore by Genre Failed")

    def assertClusterPopularActors(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.cluster_popular_actors)
                )
            )
            print("Assert Success : Assert Cluster Popular Actors Success")
        except AssertionError:
            print("Assert Failed : Assert Cluster Popular Actors Failed")

    def clickPaymentPackage(self):

        buy_package = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.img_buy_package))
        )
        buy_package.click()

    def assertBuyPackageMenu(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_buy_package)
                )
            )
            print("Assert Success : Assert Buy Package Page Success")
        except AssertionError:
            print("Assert Failed : Assert Buy Package Page Failed")

    def clickPackagePremium30(self):

        premium_30 = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.package_premium_30))
        )
        premium_30.click()

    def clickPackagePremiumSports30(self):

        premium_sports_30 = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homeObj.package_premium_sports_30)
            )
        )
        premium_sports_30.click()

    def clickBtnAccept(self):

        btn_accept = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_accept_google))
        )
        btn_accept.click()

    def assertFirstEntitlement(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.first_entitlement)
                )
            )
            print("Assert Success : Assert Entitlement Package Premium Success")
        except AssertionError:
            print("Assert Failed : Assert  Entitlement Package Premium Failed")

    def assertSecondEntitlement(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.second_entitlement)
                )
            )
            print("Assert Success : Assert Entitlemnet Package Sports Success")
        except AssertionError:
            print("Assert Failed : Assert  Entitlemnet Package Sports Failed")

    def assertErrorBuyPackage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_error_buy_package)
                )
            )
            print("Assert Success : Assert error buy package Success")
        except AssertionError:
            print("Assert Failed : Assert  error buy package Failed")

    def BtnGotIt(self):

        btn_got_it = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.btn_got_it))
        )
        btn_got_it.click()
