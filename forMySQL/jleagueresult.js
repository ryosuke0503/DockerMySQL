const puppeteer = require('puppeteer');

const main = async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox'],
    ignoreDefaultArgs: ['--disable-extensions']
  });

  const page = await browser.newPage();
  //testNo:1231
  //var url = "https://store.toto-dream.com/dcs/subos/screen/pi04/spin011/PGSPIN01101LnkHoldCntLotResultLsttoto.form?holdCntId="+process.argv[2].toString()
  //2020第一節
  //var url = "https://data.j-league.or.jp/SFMS01/search?competition_years=2020&competition_frame_ids=1&competition_ids=477&competition_section_ids=4413&tv_relay_station_name="
  //2020第二節
  //var url = "https://data.j-league.or.jp/SFMS01/search?competition_years=2020&competition_frame_ids=1&competition_ids=477&competition_section_ids=4533&tv_relay_station_name="
  var url = "https://data.j-league.or.jp/SFMS01/search?competition_years=2021&competition_frame_ids=1&competition_ids=492&competition_section_ids=4658&tv_relay_station_name="
 
  await page.goto(url);

  //tdタグの要素を抽出
  const h1s = await page.$$('td');
  var h1 = h1s[1];
  var title = await page.evaluate(el => el.innerText, h1);

  var output = "";


  for(i=0; i<h1s.length-10; i++){
    h1 = h1s[i];
    title = await page.evaluate(el => el.innerText, h1);
    if(i%11==9){
        //観客数からカンマを排除
        title = title.toString().replace(",","");
    }

    if(i%11==0||i%11==9){
        output += title;
        output += ",";
    }else if(i%11==6){
        //スコア分割
        title = title.toString().split('-');
        output += title[0];
        output += ",";
        output += title[1];
        output += ",";
    }else if(i%11 == 10){
        output += "'";
        output += title;
        output += "'";
        console.log(output);
        output = "";
    }else{
        output += "'";
        output += title;
        output += "'";
        output += ",";
    }

}

  //結構強引にcsvファイルの形を形成
  //toto結果用
  /*
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