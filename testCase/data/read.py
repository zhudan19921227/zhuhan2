import yaml
import json
def getData(yamlDir):
    #yamlDir = '../data/data.yaml'
    fo = open(yamlDir,'r',encoding='utf-8')
    res = yaml.load(fo, Loader=yaml.FullLoader)
    resList = []
    for one in res:
        resList.append((json.dumps(one['data']),json.dumps(one['rep'])))
    return resList
if __name__ == '__main__':
    print(getData())