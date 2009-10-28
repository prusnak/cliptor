import urllib
from xml.dom import minidom
from PyQt4 import QtGui

class Utils():

    @staticmethod
    def getSuggestions(s):
        params = urllib.urlencode({'ds': 'yt', 'output': 'toolbar', 'q': s})
        url = urllib.urlopen( 'http://suggestqueries.google.com/complete/search?%s' % params )
        xml = url.read()
        url.close()
        dom = minidom.parseString(xml)
        result = []
        for node in dom.firstChild.childNodes:
            if node.nodeName != 'CompleteSuggestion': continue
            data = node.firstChild.attributes['data'].value
            cnt = int(node.childNodes[1].attributes['int'].value)
            result.append( (data, cnt) )
        result.sort(key = lambda x: -x[1])
        return [x[0] for x in result]

    @staticmethod
    def getVideos(s):
        params = urllib.urlencode({'max-results': 30, 'q': s})
        url = urllib.urlopen( 'http://gdata.youtube.com/feeds/api/videos?%s' % params )
        xml = url.read()
        url.close()
        dom = minidom.parseString(xml)
        result = []
        for node in dom.getElementsByTagName('entry'):
            vid = node.getElementsByTagName('id')[0].firstChild.data.replace('http://gdata.youtube.com/feeds/api/videos/','')
            author = node.getElementsByTagName('author')[0].firstChild.firstChild.data
            published = node.getElementsByTagName('published')[0].firstChild.data
            media = node.getElementsByTagName('media:group')[0]
            title = media.getElementsByTagName('media:title')[0].firstChild.data
            desc = media.getElementsByTagName('media:description')[0].firstChild.data
            length = int(media.getElementsByTagName('yt:duration')[0].attributes['seconds'].value)
            rating = float(node.getElementsByTagName('gd:rating')[0].attributes['average'].value)
            views = int(node.getElementsByTagName('yt:statistics')[0].attributes['viewCount'].value)
            result.append({
                'vid': vid,
                'author': author,
                'published': published,
                'title': title,
                'desc': desc,
                'length': length,
                'rating': rating,
                'views': views,
                'thumbs': [ ('http://i.ytimg.com/vi/%s/' % vid) + str(i) + '.jpg' for i in range(1,4) ]
            })
        return result

    @staticmethod
    def getIcon(s):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/" + s + ".png"))
        return icon
