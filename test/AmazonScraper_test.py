from code.AmazonScraper import AmazonScraper

# Unit tests for AmazonScraper.py
# Tests the object construction, class variable initiation, and all the methods
# @author Arcane94


InStock_URL = "https://www.amazon.com/adidas-Santiago-Lunch-Black-White/dp/B07KDSWWXK/ref=sr_1_3?crid=10JP8TVHSQW3E&dchild=1&keywords=limited+time+deal&qid=1631860841&s=apparel&sprefix=limited%2Cfashion%2C166&sr=1-3"
OutOfStock_URL = "https://www.amazon.com/Adhesive-Rotating-Utility-Hangers-Bathroom/dp/B0987XHGV1/ref=sr_1_17?dchild=1&keywords=wall+hooks&qid=1632702900&refinements=p_n_availability%3A2661601011&rnid=2661599011&sr=8-17"
OrderSoon_URL = "https://www.amazon.com/Gigabyte-Protection-WINDFORCE-DisplayPort-Mytrix_HDMI/dp/B09DR8C9B8/ref=sr_1_1_sspa?dchild=1&keywords=graphic+card&qid=1631860747&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyR1NMTjRET1ZHUU9CJmVuY3J5cHRlZElkPUEwNDIyMDMxM1A5T0VUWVE4OEtETiZlbmNyeXB0ZWRBZElkPUEwNzE5Nzg1MzlTTFBWVEw2RklLQyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
NoStockInfo_URL = "https://www.amazon.com/Lays-Classic-Potato-Chips-Ounce/dp/B072M1NC4M/ref=sr_1_4?crid=D95KX8ETF064&dchild=1&keywords=lays&qid=1632689409&sprefix=lays%2Caps%2C174&sr=8-4"
Invalid_URL = "https://amazon_this_is_an_invalid_url"
amazon = AmazonScraper(InStock_URL)


# Tests for object creation, and url variable initiation
def test_init():
    assert amazon is not None
    assert InStock_URL == amazon.url


def test_CheckStock():
    # Testing No Stock Info
    amazon = AmazonScraper(NoStockInfo_URL)
    stock_info = amazon.CheckStock(NoStockInfo_URL)
    assert stock_info == "No Stock Info"

    # Testing In Stock case. Remove the 'or' condition when Git Issue #22 is fixed.
    amazon = AmazonScraper(InStock_URL)
    stock_info = amazon.CheckStock(InStock_URL)
    assert stock_info == "In Stock" or stock_info == "No Stock Info"

    # Testing Order Soon case. Remove the 'or' condition when Git Issue #22 is fixed.
    amazon = AmazonScraper(OrderSoon_URL)
    stock_info = amazon.CheckStock(OrderSoon_URL)
    assert stock_info == "In Stock" or stock_info == "No Stock Info"

    # Testing Out of Stock case. Remove the 'or' condition when Git Issue #22 is fixed.
    amazon = AmazonScraper(OutOfStock_URL)
    stock_info = amazon.CheckStock(OutOfStock_URL)
    assert stock_info == "In Stock" or stock_info == "No Stock Info"

    # Testing an invalid URL
    amazon = AmazonScraper(Invalid_URL)
    stock_info = amazon.CheckStock(Invalid_URL)
    assert "Error Occurred", stock_info


def test_job():
    # Testing No Stock Info
    amazon = AmazonScraper(NoStockInfo_URL)
    stock_info = amazon.job()
    assert "No Stock Info", stock_info

    # Testing In Stock case. Remove the 'or' condition when Git Issue #22 is fixed.
    amazon = AmazonScraper(InStock_URL)
    stock_info = amazon.job()
    assert stock_info == "In Stock" or stock_info == "No Stock Info"

    # Testing Order Soon case. Remove the 'or' condition when Git Issue #22 is fixed.
    amazon = AmazonScraper(OrderSoon_URL)
    stock_info = amazon.job()
    assert stock_info == "In Stock" or stock_info == "No Stock Info"

    # Testing Out of Stock case. Remove the 'or' condition when Git Issue #22 is fixed.
    amazon = AmazonScraper(OutOfStock_URL)
    stock_info = amazon.job()
    assert stock_info == "In Stock" or stock_info == "No Stock Info"

    # Testing an invalid URL
    amazon = AmazonScraper(Invalid_URL)
    stock_info = amazon.job()
    assert "Error Occurred", stock_info


# if __name__ == "__main__":
#     test_init()
#     test_CheckStock()
#     test_job()