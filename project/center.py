
import webbrowser
import patlamismisir
import requests
from bs4 import BeautifulSoup

class Film():
    def __init__(self, resim, baslik, aciklama, trailerYoutube_url):
        self.resim= resim
        self.baslik= baslik
        self.aciklama= aciklama
        self.trailerYoutube_url= trailerYoutube_url

    def trailerGoster(self):
        webbrowser.open(self.trailerYoutube_url)#videomuzun urlsini browser üzerinden açıyoruz.


sayfaUrl= "http://www.beyazperde.com/filmler/vizyondakiler/sinema-sayisi/"
r= requests.get(sayfaUrl)
soup= BeautifulSoup(r.content, "html.parser")

resim= soup.find_all("figure", {"class":"thumbnail"})
baslik= soup.find_all("div",{"class":"meta"})
aciklama= soup.find_all("div", {"class": "synopsis"})


def main():
    f1= Film(resim[0].contents, baslik[0].contents, aciklama[0].contents,"https://www.youtube.com/watch?v=Z5qWbnEVOWs")
    f2= Film(resim[1].contents, baslik[1].contents, aciklama[1].contents, "https://www.youtube.com/watch?v=0GSCVxkl2Ic")
    f3= Film(resim[2].contents, baslik[2].contents, aciklama[2].contents, "https://www.youtube.com/watch?v=457UT0ypa84")
    f4= Film(resim[3].contents, baslik[3].contents, aciklama[3].contents,"https://www.youtube.com/watch?v=Q7zvJIn96Hc")
    f5= Film(resim[4].contents, baslik[4].contents, aciklama[4].contents, "https://www.youtube.com/watch?v=AEx1fdRZD70")
    f6= Film(resim[5].contents, baslik[5].contents, aciklama[5].contents, "https://www.youtube.com/watch?v=rBxcF-r9Ibs")
    f7= Film(resim[6].contents, baslik[6].contents, aciklama[6].contents, "https://www.youtube.com/watch?v=Hh72ag46ZTY")
    f8= Film(resim[7].contents, baslik[7].contents, aciklama[7].contents, "https://www.youtube.com/watch?v=xsL2u2ZUJ4M")
    f9= Film(resim[8].contents, baslik[8].contents, aciklama[8].contents, "https://www.youtube.com/watch?v=BPXtVB2Qp-4")
    f10= Film(resim[9].contents, baslik[9].contents, aciklama[9].contents, "https://www.youtube.com/watch?v=F7Ug863S8dQ")

    filmler= [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]

    patlamismisir.open_movies_page(filmler)

if __name__== '__main__':
    main()