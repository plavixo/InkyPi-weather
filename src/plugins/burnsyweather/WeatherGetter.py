from urllib.request import urlopen

class WeatherGetter:
    def get_content(self):
     
        url = "http://olympus.realpython.org/profiles/aphrodite"
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        title_index = html.find("<title>")
        start_index = title_index + len("<title>")
        end_index = html.find("</title>")
        title = html[start_index:end_index]
        return f"It's going to be a superb day, {title}"