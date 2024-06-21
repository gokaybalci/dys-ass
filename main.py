from playwright.sync_api import Playwright, sync_playwright, expect

login_website = "https://dysweb.meb.gov.tr/index.xhtml"

login_info = []
with open('edevlet.txt', 'rt') as myfile:
    for line in myfile:
        login_info.append(line.strip())

# login credentials
username = login_info[0]
password = login_info[1]

def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto(login_website)
    page.get_by_role("link", name="EDEVLET GİRİŞ").click()
    
    page.get_by_label("T. C. Kimlik Numaranızı Girin").click()
    page.get_by_label("T. C. Kimlik Numaranızı Girin").fill(username)
    
    page.get_by_label("e-Devlet Şifrenizi Girin").click()
    page.get_by_label("e-Devlet Şifrenizi Girin").fill(password)
    
    page.get_by_role("button", name="Giriş Yap").click()
    
    def process_frame():
        while True:
            try:
                frame = page.frame_locator("iframe[name=\"gozdenGecirmeEkraniId\"]")
                frame.locator("button:has-text('Okudum')").wait_for(state='visible', timeout=10000)
                
                for _ in range(2):
                    frame.locator("button:has-text('Okudum')").click()
                    page.wait_for_timeout(1000) # Bunu değiştir, başka yöntem ile yapmak daha sağlıklı
            except Exception as e:
                break
        

        close_button_selector = '#formspanel\\:_08001kapat2 > span:nth-child(1)'
        
        try:
            page.locator(close_button_selector).click()
            page.wait_for_selector_to_be_hidden(close_button_selector)
        except Exception as e:
            pass

    try:
        while True:
            page.get_by_role("gridcell", name="1", exact=True).click()
            try:
                process_frame()
            except Exception as e:
                break
    except Exception as e:
        pass
    finally:
        try:
            page.locator('//*[@id="menuForm:roller_tree:1"]/span/span[3]').click()
            page.get_by_role("gridcell", name="1", exact=True).click()
            while True:
                try:
                    process_frame()
                except Exception as e:
                    break
        except Exception as e:
            pass
# Yeni sayfaya geçmek için bunu kullanıyoruz ama kontrol edilmedi
    page.locator("/html/body/div[2]/div[4]/form/div[1]/div/div/div[2]/div/div[1]/a[3]/span").click()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
