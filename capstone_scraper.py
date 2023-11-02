from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict, field
import pandas as pd
import argparse

@dataclass
class Review:
    username: str = None
    star_rating: int = None
    #thumbsup_count: int = None
    #rating_time: str = None
    review: str = None

@dataclass
class ReviewList :
    review_list : list[Review] = field(default_factory=list)

    def dataframe(self):
        """transform business_list to pandas dataframe 

        Returns: pandas dataframe
        """
        return pd.json_normalize((asdict(review) for review in self.review_list), sep="_")

    def save_to_csv(self, filename):
    	self.dataframe().to_csv(f'./capstone/{filename}.csv', index=False)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()                                                               
        
        #open browser window
        page.goto("https://play.google.com/store", timeout=60000)
        search_for = f"freecharge" 
        
        page.locator('//button[@class="VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ mN1ivc"]').click()
        page.locator('//input[@class="HWAcU"]').fill(search_for)
        page.wait_for_timeout(3000)
        page.keyboard.press('Enter')
        page.wait_for_timeout(5000)
        page.locator('//a[@class="Qfxief"]').click()
        page.wait_for_timeout(3000)
        page.locator('//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d LQeN7 aLey0c"]').click()
        page.wait_for_timeout(3000)

        #scroll
        page.hover('//div[@class="odk6He"]')
        for _ in range(10):
            page.mouse.wheel(0, 5000)
            page.wait_for_timeout(2000)

        username_xpath = '//header[@class="c1bOId"]/div[@class="YNR7H"]/div[@class="gSGphe"]/div[@class="X5PpBb"]'
        review_xpath = '//div[@class="h3YV2d"]'
        star_count_xpath = '//header[@class="c1bOId"]/div[2]/div/span/span[@class="Z1Dz7b"]'


        rl = ReviewList()        
        reviewBox_xpath = '//div[@class="odk6He"]/div/div[@class="RHo1pe"]'        
        reviewsList = page.locator(reviewBox_xpath).all()
        print(len(reviewsList))

        for j in range(len(reviewsList)):
            reviewNode = Review()
            #username
            try:
                node = reviewsList[j].locator(username_xpath)
                reviewNode.username = node.inner_text()
                print(f"USERNAME: {reviewNode.username}")
            except:
                reviewNode.username = None

            #review
            try:
                node = reviewsList[j].locator(review_xpath)
                reviewNode.review = node.inner_text()
                print(f"REVIEW = {reviewNode.review}")
            except:
                reviewNode.review = None
                print(reviewNode.review)
            
            # star count
            try :
                nodes = reviewsList[j].locator(star_count_xpath).all()
                reviewNode.star_rating = len(nodes)
                print(f"STAR RATING = {reviewNode.star_rating}\n")
            except : 
                reviewNode.star_rating = None

            rl.review_list.append(reviewNode)

        rl.save_to_csv(f"freecharge")       
    
        browser.close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search", type=str)
    parser.add_argument("-l", "--location", type=str)
    args = parser.parse_args()

    if args.location and args.search:
        search_for = f'{args.search}  {args.location}'
    else:
        # in case no arguments passed:
        # scraper will search for this on Google Maps
        search_for = 'freecharge'

main()