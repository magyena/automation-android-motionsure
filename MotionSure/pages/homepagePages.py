from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MotionSure.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
from MotionSure.object.homeObject import homeObject
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MotionSure.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
import time
import subprocess
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.homeObj = homeObject()

    def scrollDown(self):
        finger = PointerInput(interaction.POINTER_TOUCH, "finger")
        actions = ActionChains(self.driver)

        actions.w3c_actions.pointer_action.move_to_location(570, 1730)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(570, 590)
        actions.w3c_actions.pointer_action.pointer_up()

        actions.perform()

    def scroll_down(self):

        size = self.driver.get_window_size()
        start_x = size["width"] // 5
        start_y = size["height"] * 6 // 7
        end_x = size["width"] // 5
        end_y = size["height"] // 7

        self.driver.swipe(start_x, start_y, end_x, end_y, 790)

    @staticmethod
    def scroll_to_element(driver, element_xpath, max_swipes=15):
        size = driver.get_window_size()
        start_x = size["width"] // 5
        start_y = size["height"] * 6 // 7
        end_x = start_x
        end_y = size["height"] // 7

        for _ in range(max_swipes):
            try:
                element = driver.find_element(By.XPATH, element_xpath)
                if element.is_displayed():
                    return element
            except NoSuchElementException:
                driver.swipe(start_x, start_y, end_x, end_y, 650)
            else:
                break  # Stop swiping if element is found

        raise Exception("Element not found after maximum swipes")

    def scroll_left(
        self,
        start_x=None,
        start_y=None,
        end_x=None,
        end_y=None,
        start_x_ratio=None,
        start_y_ratio=None,
        end_x_ratio=None,
        end_y_ratio=None,
        duration=300,
    ):

        size = self.driver.get_window_size()

        if start_x is None and start_x_ratio is not None:
            start_x = int(size["width"] * start_x_ratio)
        if start_y is None and start_y_ratio is not None:
            start_y = int(size["height"] * start_y_ratio)
        if end_x is None and end_x_ratio is not None:
            end_x = int(size["width"] * end_x_ratio)
        if end_y is None and end_y_ratio is not None:
            end_y = int(size["height"] * end_y_ratio)

        if None in [start_x, start_y, end_x, end_y]:
            raise ValueError(
                "You must provide either absolute positions or relative ratios for all start and end points."
            )

        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def scroll_right(
        self,
        start_x=None,
        start_y=None,
        end_x=None,
        end_y=None,
        start_x_ratio=None,
        start_y_ratio=None,
        end_x_ratio=None,
        end_y_ratio=None,
        duration=300,
    ):

        size = self.driver.get_window_size()

        if start_x is None and start_x_ratio is not None:
            start_x = int(size["width"] * start_x_ratio)
        if start_y is None and start_y_ratio is not None:
            start_y = int(size["height"] * start_y_ratio)
        if end_x is None and end_x_ratio is not None:
            end_x = int(size["width"] * end_x_ratio)
        if end_y is None and end_y_ratio is not None:
            end_y = int(size["height"] * end_y_ratio)

        if None in [start_x, start_y, end_x, end_y]:
            raise ValueError(
                "You must provide either absolute positions or relative ratios for all start and end points."
            )

        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def scrollUp(self):
        finger = PointerInput(interaction.POINTER_TOUCH, "finger")
        actions = ActionChains(self.driver)

        actions.w3c_actions.pointer_action.move_to_location(507, 350)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(487, 1777)
        actions.w3c_actions.pointer_action.pointer_up()

        actions.perform()

    def disable_wifi_connection(self, emulator_id):
        # adb_path = "/Users/fatahalim/Library/Android/sdk/platform-tools/adb"
        adb_path = "/users/visionplus/Library/Android/sdk/platform-tools/adb"

        try:
            subprocess.run(
                [adb_path, "-s", emulator_id, "shell", "svc", "wifi", "disable"],
                check=True,
            )
            print(f"WiFi disabled successfully.")
        except subprocess.CalledProcessError as e:
            print("Error disabling WiFi:", e)

    def enable_wifi_connection(self, emulator_id):
        # adb_path = "/Users/fatahalim/Library/Android/sdk/platform-tools/adb"
        adb_path = "/users/visionplus/Library/Android/sdk/platform-tools/adb"

        try:
            subprocess.run(
                [adb_path, "-s", emulator_id, "shell", "svc", "wifi", "enable"],
                check=True,
            )
            print("Wifi data enabled successfully.")
        except subprocess.CalledProcessError as e:
            print("Error enabling Wifi data:", e)

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

    def BtnTerms(self):

        BtnTerms = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_terms))
        )
        BtnTerms.click()

    def BtnPrivacy(self):

        BtnPrivacy = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_privacy))
        )
        BtnPrivacy.click()

    def assertClusterJustWannaSay(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_cluster_just_wanna_say)
                )
            )
            print("Assert Success : Assert Cluster Success")
        except AssertionError:
            print("Assert Failed : Assert Cluster Failed")

    def clickContentClusterJustWannaSay(self):

        content = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homeObj.content_cluster_just_wanna_say)
            )
        )
        content.click()

    def clickSearchResultThree(self):

        search_result = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.result_search_three))
        )
        search_result.click()

    def assertSearchResultThreeinWatchlist(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.result_search_three)
                )
            )
            print("Assert Success : Assert Result in Watchlist Success")
        except AssertionError:
            print("Assert Failed : Assert Result in Watchlist Failed")

    def clickContentClusterWatchlist(self):

        content_watchlist = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homeObj.content_cluster_watchlist)
            )
        )
        content_watchlist.click()

    def clickContentClusterComedy(self):

        content_comedy = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.content_cluster_comedy))
        )
        content_comedy.click()

    def assertClusterComedy(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_cluster_comedy)
                )
            )
            print("Assert Success : Assert Cluster Comedy Success")
        except AssertionError:
            print("Assert Failed : Assert Cluster Comedy Failed")

    def assertClusterBecauseYouWatched(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_cluster_because_youwatched)
                )
            )
            print("Assert Success : Assert Cluster Because You Watched Success")
        except AssertionError:
            print("Assert Failed : Assert Cluster Because You Watched Failed")

    def clickContentClusterBecauseYouWatched(self):

        content_because = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homeObj.content_cluster_because_you_watched)
            )
        )
        content_because.click()

    def clickCategoryMovies(self):

        category_film = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.txt_category_movies))
        )
        category_film.click()

    def assertCategoryMovies(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_category_movies)
                )
            )
            print("Assert Success : Assert Category Movies Success")
        except AssertionError:
            print("Assert Failed : Assert Category Movies Failed")

    def clickContentCategoryMovies(self):

        category_film_content = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.content_category_movies))
        )
        category_film_content.click()

    def clickCategoryLiveTV(self):

        category_liveTV = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.txt_category_livetv))
        )
        category_liveTV.click()

    def clickResultSportsChannel(self):

        sports_channel = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homeObj.result_search_sportschannel)
            )
        )
        sports_channel.click()

    def clickCategorySeries(self):

        category_series = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.txt_category_series))
        )
        category_series.click()

    def clickContentCategorySeries(self):

        content_category_series = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.content_category_series))
        )
        content_category_series.click()

    def clickMyDownloadsMenu(self):

        my_download = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.img_my_downloads))
        )
        my_download.click()

    def assertMyDownloadsPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, self.homeObj.img_upgrade_download)
                )
            )
            print("Assert Success : Assert My Download Page Success")
        except AssertionError:
            print("Assert Failed : Assert My Download Page Failed")

    def clickSubscribeMyDownloads(self):

        btn_subscribe_my_download = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_subscribe_my_downloads))
        )
        btn_subscribe_my_download.click()
