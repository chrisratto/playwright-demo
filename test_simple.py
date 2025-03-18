from playwright.sync_api import Page, expect

def test_homepage(page: Page):
    # Navigate to the test site
    page.goto("http://the-internet.herokuapp.com/")
    
    # Check the page title
    expect(page).to_have_title("The Internet")
    
    # Click the "A/B Testing" link and verify the new page
    page.click("text=A/B Testing")
    expect(page).to_have_url("http://the-internet.herokuapp.com/abtest")
    assert "A/B Test" in page.text_content("h3")