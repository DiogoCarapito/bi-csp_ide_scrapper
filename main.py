import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def main():
    url_bicsp_idg = "https://bicsp.min-saude.pt/pt/contratualizacao/idg/Paginas/default.aspx"
    
    options = Options()
    options.add_experimental_option("detach", True)
    
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    
    # Navigate to a webpage
    driver.get(url_bicsp_idg)
    
    # Keep the browser open for 10 seconds
    time.sleep(6)

    
    # click in a PowerBI dashboard separator down below amed "UF - IDG - Indicadores"
    # Create an ActionChains object
    # actions = ActionChains(driver)

    # actions.pointer_action.move_to_location(8, 0)
    # actions.perform()

    mouse_tracker = driver.find_element(By.ID, "mouse-tracker")
    ActionChains(driver)\
        .move_to_element_with_offset(mouse_tracker, 8, 0)\
        .perform()

    
    # # Find the element you want to interact with
    # element = driver.find_element('UF - IDG - Indicadores')

    # # Move to the element and click it
    # actions.move_to_element(element).click().perform()

    time.sleep(10)
    
    # Close the browser
    driver.quit()
    
if __name__ == "__main__":
    main()