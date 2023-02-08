from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import pytest
import pyautogui


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

@pytest.fixture
def context():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://open.spotify.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

#==================================================================================================================================================================
#   SIGN IN
#==================================================================================================================================================================

@pytest.mark.login_positivetest
def test_login_success(context):
    context.find_element(By.XPATH, '//button[@data-testid="login-button"]').click()
    username = context.find_element(By.ID, "login-username")
    password = context.find_element(By.ID, "login-password")
    username.send_keys('testing.brins@gmail.com')
    password.send_keys('testingbrins!')
    context.find_element(By.ID, "login-button").click()

    assert "Spotify" in context.title

Kunci = [
        ('testing.brins@gmail.com','testtesttest' , 'Incorrect username or password.'),     # username benar password salah 
        ('testtesttest','testingbrins!' , 'Incorrect username or password.'),               # username salah password benar
        ('testtesttest','testtesttest' , 'Incorrect username or password.')                 # username salah password salah
]

@pytest.mark.login_negativetest
@pytest.mark.parametrize('user_name , passwrd , result', Kunci)
def test_login_failed(context, user_name, passwrd,result):
    context.find_element(By.XPATH, '//button[@data-testid="login-button"]').click()
    username = context.find_element(By.ID, "login-username")
    password = context.find_element(By.ID, "login-password")
    username.send_keys(user_name)
    password.send_keys(passwrd)
    context.find_element(By.ID, "login-button").click()

    assert result in context.find_element(By.XPATH, '//span[@class="Message-sc-15vkh7g-0 jHItEP"]').text

#==================================================================================================================================================================
#   CREATE A PLAYLIST
#==================================================================================================================================================================

@pytest.mark.create_a_playlist
def test_create_a_playlist(context):
    context.find_element(By.XPATH, '//button[@data-testid="login-button"]').click()
    username = context.find_element(By.ID, "login-username")
    password = context.find_element(By.ID, "login-password")
    username.send_keys('testing.brins@gmail.com')
    password.send_keys('testingbrins!')
    context.find_element(By.ID, "login-button").click()
    context.find_element(By.XPATH, '//button[@data-testid="create-playlist-button"]').click()
    time.sleep(5)
    assert "My Playlist" in context.title
    
    context.find_element(By.XPATH, '//span[@data-testid="entityTitle"]').click()
    create_playlits = context.find_element(By.XPATH, '//input[@data-testid="playlist-edit-details-name-input"]')
    create_playlits.send_keys('Testing Playlist Adikrisna Nugraha')
    context.find_element(By.XPATH, '//button[@data-testid="playlist-edit-details-save-button"]').click()
    time.sleep(7)

#==================================================================================================================================================================
#   SEARCH SONGS
#==================================================================================================================================================================

@pytest.mark.search_songs
def test_search_songs(context):
    context.find_element(By.XPATH, '//button[@data-testid="login-button"]').click()
    username = context.find_element(By.ID, "login-username")
    password = context.find_element(By.ID, "login-password")
    username.send_keys('testing.brins@gmail.com')
    password.send_keys('testingbrins!')
    context.find_element(By.ID, "login-button").click()
    context.find_element(By.XPATH, '//a[@href="/search"]').click()
    time.sleep(5)

    assert 'Search' in context.title
    
    search_songs = context.find_element(By.XPATH, '//input[@data-testid="search-input"]')
    search_songs.send_keys('Tulus' + Keys.ENTER)

    assert 'Tulus' in context.find_element(By.XPATH, '//div[@class="Type__TypeElement-sc-goli3j-0 gRwoMO nk6UgB4GUYNoAcPtAQaG"]').text

#==================================================================================================================================================================
#   ADD LIKED SONGS
#==================================================================================================================================================================

@pytest.mark.add_liked_songs
def test_add_liked_songs(context):
    context.find_element(By.XPATH, '//button[@data-testid="login-button"]').click()
    username = context.find_element(By.ID, "login-username")
    password = context.find_element(By.ID, "login-password")
    username.send_keys('testing.brins@gmail.com')
    password.send_keys('testingbrins!')
    context.find_element(By.ID, "login-button").click()
    context.find_element(By.XPATH, '//a[@href="/search"]').click()
    time.sleep(5)
    assert 'Search' in context.title
    
    search_songs = context.find_element(By.XPATH, '//input[@data-testid="search-input"]')
    search_songs.send_keys('Shape of You' + Keys.ENTER)

    ActionChains(context).move_to_element(context.find_element(By.XPATH, '//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]')).perform()
    ActionChains(context).context_click(context.find_element(By.XPATH, '//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]')).perform()
    context.find_element(By.XPATH, '//*[@id="context-menu"]/ul/li[6]/button').click()
    time.sleep(7)