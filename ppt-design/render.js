const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function renderDesign(designFile, outputFile) {
    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    
    const page = await browser.newPage();
    await page.setViewport({ width: 1920, height: 1080 });
    
    const htmlPath = path.resolve(__dirname, designFile);
    await page.goto(`file://${htmlPath}`, { 
        waitUntil: 'networkidle0',
        timeout: 60000
    });
    
    // 等待动画稳定
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    await page.screenshot({
        path: path.resolve(__dirname, outputFile),
        fullPage: true,
        type: 'png'
    });
    
    await browser.close();
    console.log(`✓ Rendered: ${outputFile}`);
}

async function main() {
    console.log('🎨 Rendering PPT cover designs...\n');
    
    // 原三个方案
    await renderDesign('design-01-stellar.html', 'cover-01-stellar.png');
    await renderDesign('design-02-metallic.html', 'cover-02-metallic.png');
    await renderDesign('design-03-spotlight.html', 'cover-03-spotlight.png');
    
    // 王家卫风格新方案
    await renderDesign('wong-01-chongqing.html', 'cover-wong-01-chongqing.png');
    await renderDesign('wong-02-inthemood.html', 'cover-wong-02-inthemood.png');
    
    console.log('\n✅ All designs rendered successfully!');
}

main().catch(console.error);
