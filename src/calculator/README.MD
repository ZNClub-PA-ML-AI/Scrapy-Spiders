# SCRAPY FOR CALCULATOR PRICE ANALYSIS

## URL
- [LIST OF ITEMS VIEW](https://www.olx.in/mumbai/q-scientific-calculator/?page=2&view=list)
- ITER = 0 to 40 
- 0,1,.. and last 41,42,.. MIGHT BE null due to ads
- [GALLERY VIEW](https://www.olx.in/mumbai/q-scientific-calculator/?view=galleryWide&page=2)
- if remove p, then gives TITLE\n\tPRICE. However TITLE is in incomplete form
- Date of post not available
- Section and Area cannot be recognized as separate XPaths

## XPATH

### PRICE
- __LIST OF ITEMS VIEW__
- /html/body/div[@id='innerLayout']/div[@id='listContainer']/section[@id='body-container']/div/div/div/table/tbody/tr[ITER]/td/table/tbody/tr[1]/td/div/p

- __GALLERY VIEW__
- /html/body/div[@id='innerLayout']/div[@id='listContainer']/section[@id='body-container']/div/div/div/ul[@id='gallerywide']/li/div/div/p


### NAME with href link
- __LIST OF ITEMS VIEW__
- /html/body/div/div/section/div/div/div/table/tbody/tr[ITER]/td/table/tbody/tr[1]/td[2]/h3/a

### AREA
- /html/body/div/div/section/div/div/div/table/tbody/tr[ITER]/td/table/tbody/tr[1]/td[2]/p/small/span

### DATE
- /html/body/div/div/section/div/div/div/table/tbody/tr[ITER]/td/table/tbody/tr[2]/td[1]/p
