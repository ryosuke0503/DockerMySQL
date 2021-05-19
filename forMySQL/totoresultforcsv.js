const puppeteer = require('puppeteer');

const main = async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox'],
    ignoreDefaultArgs: ['--disable-extensions']
  });

  const page = await browser.newPage();
  //testNo:1231
  var url = "https://store.toto-dream.com/dcs/subos/screen/pi04/spin011/PGSPIN01101LnkHoldCntLotResultLsttoto.form?holdCntId="+process.argv[2].toString()
  await page.goto(url);

  //tdタグの要素を抽出
  const h1s = await page.$$('td');
  var h1 = h1s[1];
  var title = await page.evaluate(el => el.innerText, h1);

  var output = process.argv[2].toString();
  output += ",";

  for(i=3; i<94; i++){
    h1 = h1s[i];
    title = await page.evaluate(el => el.innerText, h1);

    if((i-3)%7==0 || (i-3)%7==1 || (i-3)%7==3 || (i-3)%7==5){
      if(title == "横浜Ｍ"){title = "横浜FM";}
      if(title == "横浜Ｃ"){title = "横浜FC";}
      if(title == "川崎"){title = "川崎Ｆ";}

      output += title;
      output += ",";
    }
    if((i-3)%7==6){
      output += title;
      console.log(output);
      output = process.argv[2].toString();
      output += ",";
    }
  }

  /*
  //結構強引にcsvファイルの形を形成
  for(i=3; i<94; i++){
    h1 = h1s[i];
    title = await page.evaluate(el => el.innerText, h1);

    output += title;
    if((i-3)%7!=6){
      output += ",";
    }else{
      console.log(output);
      output = "";
    }
  }
  */

  browser.close();
}

main();