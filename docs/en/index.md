---
title: Home
hide:
  # - navigation # 显示右
  # - toc #显示左
  - footer
  - feedback
comments: false
---
# Home

<!-- <center><font  color= #518FC1 size=6>“循此苦旅，以达星辰”</font></center> -->
<center><font  color= #518FC1 size=6 class="ml3">"Follow this arduous journey to reach the stars"</font></center>
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/2.0.2/anime.min.js"></script>


<!-- <center>
<font  color= #608DBD size=3>
<span id="jinrishici-sentence">正在加载今日诗词....</span>
<script src="https://sdk.jinrishici.com/v2/browser/jinrishici.js" charset="utf-8"></script>
</font>
</center> -->

<!-- <center>
<font  color= #608DBD size=3>
<span id="hitokoto-sentence">正在加载一言....</span>
<script src="https://v1.hitokoto.cn"></script>
</font>
</center> -->

<!-- <center>
<font  color= #608DBD size=3>
<p id="hitokoto">
  <a href="#" id="hitokoto_text" target="_blank"></a>
</p>
<script>
  fetch('https://v1.hitokoto.cn')
    .then(response => response.json())
    .then(data => {
      const hitokoto = document.querySelector('#hitokoto_text')
      hitokoto.href = `https://hitokoto.cn/?uuid=${data.uuid}`
      hitokoto.innerText = data.hitokoto
    })
    .catch(console.error)
</script>
</font>
</center> -->


<div id="rcorners2" >
  <!-- <div id="rcorners1">
    <body>
      <font color="#4351AF">
        <p class="p1"></p>
<script defer>
    function format(newDate) {
        var day = newDate.getDay();
        var y = newDate.getFullYear();
        var m =
            newDate.getMonth() + 1 < 10
                ? "0" + (newDate.getMonth() + 1)
                : newDate.getMonth() + 1;
        var d =
            newDate.getDate() < 10 ? "0" + newDate.getDate() : newDate.getDate();
        var h =
            newDate.getHours() < 10 ? "0" + newDate.getHours() : newDate.getHours();
        var min =
            newDate.getMinutes() < 10
                ? "0" + newDate.getMinutes()
                : newDate.getMinutes();
        var s =
            newDate.getSeconds() < 10
                ? "0" + newDate.getSeconds()
                : newDate.getSeconds();
        var dict = {
            1: "一",
            2: "二",
            3: "三",
            4: "四",
            5: "五",
            6: "六",
            0: "天",
        };
        //var week=["日","一","二","三","四","五","六"]
        return (
            y +
            "年" +
            m +
            "月" +
            d +
            "日" +
            " " +
            h +
            ":" +
            min +
            ":" +
            s +
            " 星期" +
            dict[day]
        );
    }
    var timerId = setInterval(function () {
        var newDate = new Date();
        var p1 = document.querySelector(".p1");
        if (p1) {
            p1.textContent = format(newDate);
        }
    }, 1000);
</script>
      </font>
    </body>
  </div> -->
  <ul>
<li>Open articles by topic and table of contents</li>
     <ul>
       <li>For Mac/PC, please select the topic in the tab bar above and select the article in the directory on the left</li>
       <li>Mobile version, please click the icon in the upper left corner to select topics and articles</li>
     </ul>
     <li>Search for keywords to open articles</li>
     <li>
       If you encounter web page freezes or images cannot be displayed after opening an article, please use <strong>Scientific Internet Access</strong> to break information barriers
     </li>
   </ul>
</div> 
Quick Chat(1) Contact Me(2)
{ .annotate }

1. Click on the bottom right corner to chat with me online.
2. Wechat:18939533255
***  

<div class="grid cards" markdown>

-   :simple-materialformkdocs:{ .lg .middle } __Mkdocs Tutorial__

    ---

    - [Deploy static web pages to GitHub pages with Mkdocs](../blog/Mkdocs/mkdocs1.md)
    - [Mkdocs deployment configuration explanation (mkdocs.yml)](../blog/Mkdocs/mkdocs2.md)
    - [How to add friends links to MKdocs](../blog/websitebeauty/linktech.md)
    - [Adding Mkdocs blog to website](../blog/Mkdocs/mkdocsblog.md)
    - [Blogger](../blog/index.md)


-   :simple-aboutdotme:{ .lg .middle } __About__

    ---
    - [Mkdocs-Wcowin blog theme community](https://support.qq.com/products/646913/){target="_blank"}
    - [Message Board](../liuyanban.md)[^Knowing-that-loving-you-has-no-ending] 
    - [Blogger](../blog/index.md)   
    [:octicons-arrow-right-24: Learn about me](../about/geren.md)[^see-how-much-I-love-you]

</div>
  

[^Knowing-that-loving-you-has-no-ending]:The sun always warms sunflowers  
[^see-how-much-I-love-you]:All problems in computer science can be solved by another level of indirection



<!-- Start of Howxm client code snippet -->
<script>
function _howxm(){_howxmQueue.push(arguments)}
window._howxmQueue=window._howxmQueue||[];
_howxm('setAppID','14429fca-cac1-4551-a472-b046a96ebb75');
(function(){var scriptId='howxm_script';
if(!document.getElementById(scriptId)){
var e=document.createElement('script'),
t=document.getElementsByTagName('script')[0];
e.setAttribute('id',scriptId);
e.type='text/javascript';e.async=!0;
e.src='https://static.howxm.com/sdk.js';
t.parentNode.insertBefore(e,t)}})();
</script>
<!-- End of Howxm client code snippet -->

<!-- <script src="//code.tidio.co/6jmawe9m5wy4ahvlhub2riyrnujz7xxi.js" async></script> -->
</head>





<!-- <head>
<script charset="UTF-8" id="LA_COLLECT" src="//sdk.51.la/js-sdk-pro.min.js"></script>
<script>LA.init({id:"3HOcxvgwJJmkuGUi",ck:"3HOcxvgwJJmkuGUi"})</script>
</head> -->



   <body>
        <font color="#B9B9B9">
        <p style="text-align: center; ">
                <span>This site is already running</span>
                <span id='box1'></span>
    </p>
      <div id="box1"></div>
      <script>
        function timingTime(){
          let start = '2022-10-20 00:00:00'
          let startTime = new Date(start).getTime()
          let currentTime = new Date().getTime()
          let difference = currentTime - startTime
          let m =  Math.floor(difference / (1000))
          let mm = m % 60  // 秒
          let f = Math.floor(m / 60)
          let ff = f % 60 // 分钟
          let s = Math.floor(f/ 60) // 小时
          let ss = s % 24
          let day = Math.floor(s  / 24 ) // 天数
          return day + "day" + ss + "hour" + ff + "minute" + mm +'second'
        }
        setInterval(()=>{
          document.getElementById('box1').innerHTML = timingTime()
        },1000)
      </script>
      </font>
    </body>


<!-- <head>
<script defer src="https://analytics.us.umami.is/script.js" data-website-id="dae37494-1db6-408a-afdd-1868e1a7d41a"></script>
</head> -->
