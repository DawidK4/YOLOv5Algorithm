from icrawler.builtin import GoogleImageCrawler

def download_images(keyword, max_num=20, save_dir=None):
    crawler = GoogleImageCrawler(storage={'root_dir': save_dir or keyword})
    crawler.crawl(keyword=keyword, max_num=max_num, file_idx_offset=0, min_size=(200, 200), max_size=None)

if __name__ == "__main__":
    keyword = 'boeing737'

    save_path = './images/all'  # all images go here
    
    print(f"Downloading images for: {keyword}")
    download_images(keyword, max_num=450, save_dir=save_path)
    print("Download completed.")
