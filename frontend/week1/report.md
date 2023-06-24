 1. Yes, the nested elements form a tree structure. There is a parent child relationship between elements and their nesting levels.
![image](https://github.com/BupuBupu/summer-of-code-2023/assets/72183674/270d3229-2231-485a-b437-786998354da6)
As can be seen above, <html> </html> is the root element. It has various child elements like <head></head>, <body></body>, <style>,<link>,<Grammarly>.
2. I removed some style class from the HTML format and edited some text.
Before
![image](https://github.com/BupuBupu/summer-of-code-2023/assets/72183674/5d444af2-a491-4a76-bca7-c28b6b6cdaf9)
After
![image](https://github.com/BupuBupu/summer-of-code-2023/assets/72183674/e5ba6572-015a-48cb-a186-ad9f7162180e)
3. The value of the CSS selector with id= username is “”
![image](https://github.com/BupuBupu/summer-of-code-2023/assets/72183674/bfb48db6-cb9d-4f6c-92f2-9f33489400bb)
Another example ; document.querySelector(“#id”).childElementCount shows the number of child elements of the tag with given id.
 ![image](https://github.com/BupuBupu/summer-of-code-2023/assets/72183674/5ffe691c-926f-4bf0-85fc-d846d3cb272c)
We can use various other functions to get our desired answers.
4. After I disabled cache and enabled throttling with fast 3G, there were no visual change in the website. But the website took longer to load.
It took 8.38 sec
Compared to this when cache was enabled and throttling was disabled it took 1 Sec.
attached are the screenshots.
![image](https://github.com/BupuBupu/summer-of-code-2023/assets/72183674/0d28c3fd-6f1f-48ef-8fd2-8addf7dc4639)
And while cache was disabled and throttling was enabled with fast  3G
![image](https://github.com/BupuBupu/summer-of-code-2023/assets/72183674/e4857edc-7050-49b8-8636-0ec17a16a19f)
