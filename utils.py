import urllib
from xml.dom import minidom

class Utils():

    def getSuggestions(s):
        params = urllib.urlencode({'ds': 'yt', 'output': 'toolbar', 'q': s})
        url = urllib.urlopen( 'http://suggestqueries.google.com/complete/search?%s' % params )
        xml = url.read()
        url.close()
        dom = minidom.parseString(xml)
        result = []
        for node in dom.childNodes[0].childNodes:
            if node.nodeName != 'CompleteSuggestion': continue
            data = node.childNodes[0].attributes['data'].value
            cnt = int(node.childNodes[1].attributes['int'].value)
            result.append( (data, cnt) )
        result.sort(key = lambda x: -x[1])
        return [x[0] for x in result]
    getSuggestions = staticmethod(getSuggestions)

    def getVideos(s):
        params = urllib.urlencode({'max-results': 30, 'start-index': 1, 'q': s})
        url = urllib.urlopen( 'http://gdata.youtube.com/feeds/api/videos?%s' % params )
        xml = url.read()
        url.close()
        dom = minidom.parseString(xml)
        result = []
        # TODO: do something with dom
        return result
    getVideos = staticmethod(getVideos)
