import asyncio
import time
from pyppeteer import launch
async def main():
    # launch chromium browser in the background
    browser = await launch(options={"headless":False, "executablePath":'C:\Program Files\Google\Chrome\Application\chrome.exe'})
    # open a new tab in the browser
    page = await browser.newPage()
    async def choose():
        i=input("Choice:")
        print(await page.evaluate("document.getElementsByClassName('os-content')[1].getElementsByTagName('li')["+i+"].getElementsByClassName('Type__TypeElement-sc-goli3j-0')[0].click()"))
    async def getlistd():
        await page.goto("https://open.spotify.com/")
        await page.waitForSelector("#device-picker-icon-button")
        await page.click("#device-picker-icon-button")
        time.sleep(1)
        l=await page.evaluate("""()=>{
        var elements = document.getElementsByClassName("os-content")[1].getElementsByTagName("li");
var ll = [];
for (var i = 0; i < elements.length; i++) {
    ll.push(elements[i].getElementsByClassName("Type__TypeElement-sc-goli3j-0")[0].innerHTML);
}return(ll);
        }""")
        print(l)
        await choose()
    await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
    await page.setBypassCSP(True)
    # add URL to a new page and then open it
    await page.goto("https://accounts.spotify.com/it/login?continue=https%3A%2F%2Fopen.spotify.com%2F")
    # create a screenshot of the page and save it
    await page.type('#login-username', 'lucar220903@gmail.com')
    await page.type('#login-password', 'Ajax1Napoli6@')
    await page.click("#login-button")
    await page.waitForSelector("#onetrust-accept-btn-handler")
    time.sleep(1)
    await page.click("#onetrust-accept-btn-handler")
    await getlistd()
    # close the browser
    time.sleep(100)
    await browser.close()

print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
print("Screenshot has been taken")