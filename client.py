# coding:utf-8
import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("127.0.0.1", 14444)))
    
    def parse(self, text):
        print text
        resultt = self.server.parse(text)
        print resultt
        return json.loads(resultt)
        #return json.loads(self.server.parse(text))

nlp = StanfordNLP()
#result = nlp.parse("John is a computer scientist. He is very good at Artificial Intelligence.")
text = u"周子叶是一个计算机科学家。他很擅长人工智能。"

#text = text.decode('ascii', 'ignore')
result = nlp.parse(text)
pprint(result)

#from nltk.tree import Tree
#tree = Tree.parse(result['sentences'][0]['parsetree'])
#pprint(tree)

