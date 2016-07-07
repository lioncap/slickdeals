from utils import crawl_deals

if __name__ == '__main__':
    deals = crawl_deals()
    for i, item in enumerate(deals):
        print '%d. %s\nLink: %s\nPrice: %s\nInfo: %s\n\n' % (
            i+1, item['title'], item['link'], item['price'], item['info']
        )
