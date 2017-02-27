#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
"""
Simple client web per descarregar de udl.cat

@author: jordigm@jordigm.com
"""

import urllib2
import bs4

class Client(object):

    def get_webpage(self,page):
        """ obtenir la pagina web """
        f = urllib2.urlopen(page)
        htmlpage = f.read()
        f.close()
        return htmlpage

    def search_data(self,html):
        """ buscar dades """
        bs = bs4.BeautifulSoup(html,"lxml")
        caixa = bs.find("div", "sg-featuredlink")
        items = caixa.find_all("div","featured-links-item")
        results = []
        
        for item in items:
            time = item.find('time')["datetime"]
            text = item.find('span','flink-title').text
            results.append((time,text))
        return results

    def main(self):
        #obtenir plana web
        webpag = self.get_webpage('http://www.udl.cat')
        #buscar dades
        results = self.search_data(webpag)
        #imprimir resultats
        print results


if __name__ == "__main__":
    cw = Client()
    cw.main()
