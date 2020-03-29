const puppeteer = require("puppeteer");
(async () => {
  const browser = await puppeteer.launch({
    args: ["--no-sandbox"],
    headless: false
  });
  const page = await browser.newPage();

  await page.goto("https://www.google.com/");

  await page.focus("input[name=q]");

  await page.keyboard.type("Zelda");

  await page.keyboard.press("Enter");

  await page.waitForNavigation();

  await page.screenshot({ path: "ex.png" });

  await browser.close();
})();
