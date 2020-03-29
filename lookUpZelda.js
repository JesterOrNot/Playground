const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch()
  const page = await browser.newPage()
  
  const navigationPromise = page.waitForNavigation()
  
  await navigationPromise
  
  await page.goto('https://www.google.com/')
  
  await page.setViewport({ width: 1366, height: 641 })
  
  await page.waitForSelector('.A8SBwf > .RNNXgb > .SDkEP > .a4bIc > .gLFyf')
  await page.click('.A8SBwf > .RNNXgb > .SDkEP > .a4bIc > .gLFyf')
  
  await page.waitForSelector('.UUbT9 > .aajZCb > .tfB0Bf > center > .gNO89b')
  await page.click('.UUbT9 > .aajZCb > .tfB0Bf > center > .gNO89b')
  
  await navigationPromise
  
  await browser.close()
})()
