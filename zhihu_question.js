const puppeteer = require('puppeteer');
const fs = require("fs");
const userAgent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1';
const workPath = './testq';

(async () => {

    const browser = await puppeteer.launch({
        executablePath: 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
        headless: false
    });

    for(let i=1; i<123; i++){
        url='https://www.zhihu.com/question/277612345/answers/created?page='+i;
        filepath=workPath+'/'+i+'.txt';

        try{
            const page = await browser.newPage();
            await page.setUserAgent(userAgent);

            await page.goto(url);
            for(let i=0; i<10; i++){
                try{
                    await page.evaluate(()=>window.scrollTo(0, document.body.scrollHeight));
                    await page.waitForNavigation({timeout:100,waitUntil: ['networkidle0']});
                }catch(err){
                    console.log('scroll');
                }
            }

            const aHandle = await page.evaluateHandle(() => document.body);
            const resultHandle = await page.evaluateHandle(body => body.innerText, aHandle);

            contents = await resultHandle.jsonValue();
            fs.writeFileSync(filepath,contents);
            await resultHandle.dispose();

            await page.close();

        }catch(err){
            console.log('url_error: '+url+' \n');
        }

    }

    await browser.close();
})();


