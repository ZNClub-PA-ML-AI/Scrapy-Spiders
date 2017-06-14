# SCRAPY FOR CALCULATOR PRICE ANALYSIS

## URL & XPATH

### PRICE
- [LIST OF ITEMS VIEW](https://www.olx.in/mumbai/q-scientific-calculator/?page=2)
- /html/body/div[@id='innerLayout']/div[@id='listContainer']/section[@id='body-container']/div/div/div/table/tbody/tr[ITER]/td/table/tbody/tr[1]/td/div/p
- ITER = 0 to 40 
- 0,1,.. and last 41,42,.. MIGHT BE null due to ads
- [VIEW WITHOUT ADS](https://www.olx.in/mumbai/q-scientific-calculator/?view=galleryWide&page=2)
- /html/body/div[@id='innerLayout']/div[@id='listContainer']/section[@id='body-container']/div/div/div/ul[@id='gallerywide']/li/div/div/p
- if remove p, then gives TITLE\n\tPRICE. However TITLE is in incomplete form
- 
