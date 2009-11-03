import sys
import os
import urllib
import urllib2
from xml.dom import minidom
from PyQt4 import QtGui
from datetime import datetime

HOMEDIR = os.getenv('HOME')
if HOMEDIR == None:
    print >> sys.stderr, 'Your $HOME is empty'
    sys.exit(1)
CONFDIR = os.getenv('XDG_CONFIG_HOME')
CACHEDIR = os.getenv('XDG_CACHE_HOME')
if CONFDIR == None:
    CONFDIR = HOMEDIR + '/.config'
if CACHEDIR == None:
    CACHEDIR = HOMEDIR + '/.cache'

CONFDIR = CONFDIR + '/cliptor/'
CACHEDIR = CACHEDIR + '/cliptor/'

THUMBDIR = CACHEDIR + 'thumbnails/'
SEARCHRESULTS = 20

quality = [
    'small',      # <  640 x 360
    'medium',     # >= 640 x 360
    'large',      # >= 854 x 480
    'hd720'       # >= 1280 x 720
]

try:
    os.makedirs(CONFDIR)
    os.makedirs(THUMBDIR)
except:
    pass

class Utils():

    @staticmethod
    def getSuggestions(s):
        params = urllib.urlencode({'ds': 'yt', 'output': 'toolbar', 'q': s})
        url = 'http://suggestqueries.google.com/complete/search?%s' % params
        print 'GET %s' % url
        sock = urllib2.urlopen( url, timeout = 1 )
        xml = sock.read()
        sock.close()
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
        params = urllib.urlencode({'max-results': SEARCHRESULTS, 'q': s})
        url = 'http://gdata.youtube.com/feeds/api/videos?%s' % params
        print 'GET %s' % url
        sock = urllib2.urlopen( url, timeout = 30 )
        xml = sock.read()
        sock.close()
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
                'thumbs': [ (THUMBDIR +'yt_%s_%d.jpg') % (vid, i) for i in range(1,4) ]
            })
            for i in range(1,2):
                url = 'http://i.ytimg.com/vi/%s/%d.jpg' % (vid, i)
                dest = (THUMBDIR +'yt_%s_%d.jpg') % (vid, i)
                if not os.path.exists( dest ):
                    print 'GET %s -> %s' % (url, dest)
                    urllib.urlretrieve(url, dest)
        return result

    @staticmethod
    def getIcon(s):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/" + s + ".png"))
        return icon
