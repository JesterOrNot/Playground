const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox'], headless: false})
  const page = await browser.newPage()
  
  const navigationPromise = page.waitForNavigation()
  
  await navigationPromise
  
  await page.goto('https://www.google.com/')
  
  await page.setViewport({ width: 1366, height: 641 })
  
  await page.waitForSelector('.A8SBwf > .RNNXgb > .SDkEP > .a4bIc > .gLFyf')
  await page.click('.A8SBwf > .RNNXgb > .SDkEP > .a4bIc > .gLFyf')
  
  await navigationPromise
  
  await browser.close()
})()