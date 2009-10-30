import os
import urllib
from xml.dom import minidom
from PyQt4 import QtGui
from datetime import datetime

confdir = os.getenv('HOME') + '/.cliptor/'
thumbdir = confdir + 'thumbnails/'
try:
    os.makedirs(confdir)
    os.makedirs(thumbdir)
except:
    pass

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
        params = urllib.urlencode({'max-results': 20, 'q': s})
        url = urllib.urlopen( 'http://gdata.youtube.com/feeds/api/videos?%s' % params )
        xml = url.read()
        url.close()
        dom = minidom.parseString(xml)
        result = []
        for node in dom.getElementsByTagName('entry'):
            vid = node.getElementsByTagName('id')[0].firstChild.data.replace('http://gdata.youtube.com/feeds/api/videos/','')
            author = node.getElementsByTagName('author')[0].firstChild.firstChild.data
            published = datetime.strptime( node.getElementsByTagName('published')[0].firstChild.data[:19] , '%Y-%m-%dT%H:%M:%S')
            media = node.getElementsByTagName('media:group')[0]
            title = media.getElementsByTagName('media:title')[0].firstChild.data
            if media.getElementsByTagName('media:description')[0].firstChild != None:
                desc = media.getElementsByTagName('media:description')[0].firstChild.data
            else:
                desc = ''
            length = int(media.getElementsByTagName('yt:duration')[0].attributes['seconds'].value)
            if len(node.getElementsByTagName('gd:rating')) > 0:
                rating = float(node.getElementsByTagName('gd:rating')[0].attributes['average'].value)
            else:
                rating = 0.0
            if len(node.getElementsByTagName('yt:statistics')) > 0:
                views = int(node.getElementsByTagName('yt:statistics')[0].attributes['viewCount'].value)
            else:
                views = 0
            result.append({
                'vid': vid,
                'author': author,
                'published': published,
                'title': title,
                'desc': desc,
                'length': length,
                'rating': rating,
                'views': views,
                'thumbs': [ (thumbdir +'%s_%d.jpg') % (vid, i) for i in range(1,2) ]
            })
            for i in range(1,2):
                if not os.path.exists( (thumbdir +'%s_%d.jpg') % (vid, i) ):
                    urllib.urlretrieve('http://i.ytimg.com/vi/%s/%d.jpg' % (vid, i), (thumbdir +'%s_%d.jpg') % (vid, i) )
        return result

    @staticmethod
    def getIcon(s):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/" + s + ".png"))
        return icon
