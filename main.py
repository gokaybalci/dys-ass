from playwright.sync_api import Playwright, sync_playwright, expect

login_website = "https://dysweb.meb.gov.tr/index.xhtml"

login_info = []
with open ('edevlet.txt', 'rt') as myfile:
        for line in myfile:
            login_info.append(line)

# login credentials
username = login_info[0]
password = login_info[1]

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(login_website)
    page.get_by_role("link", name="EDEVLET GİRİŞ").click()
    page.get_by_label("T. C. Kimlik Numaranızı Girin").click()
    page.get_by_label("T. C. Kimlik Numaranızı Girin").fill(username)
    page.get_by_label("e-Devlet Şifrenizi Girin").click()
    page.get_by_label("e-Devlet Şifrenizi Girin").fill(password)
    page.get_by_role("button", name="Giriş Yap").click()
    
    try:
        while True:
            page.get_by_role("gridcell", name="1", exact=True).click()
            page.frame_locator("iframe[name=\"gozdenGecirmeEkraniId\"]").get_by_role("button", name="Okudum").click()
    except Exception as e:
        print("Ana okulda DYS yazısı bulunamadı.")
    finally:
        # Görevlendirme Okuluna Geçme
        try:
            page.locator('//*[@id="menuForm:roller_tree:1"]/span/span[3]').click();
            print("Görevlendirme okuluna geçtim.")
            page.get_by_role("gridcell", name="1", exact=True).click()
            while True:
                page.frame_locator("iframe[name=\"gozdenGecirmeEkraniId\"]").get_by_role("button", name="Okudum").click()
        except Exception as e:
            print("Görevlendirme DYS yazısı bulunamadı.")


    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
