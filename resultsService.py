import json
import datetime
import os

class ResultsService:
    def parse(self,results):
        result_list = []
        for item in results:
            parsed_item = json.dumps(item)
            list_item = json.loads(parsed_item)
            result_list.append(list_item)
        self.save(result_list)
        return result_list

    def save(self,results):
        now = datetime.datetime.now()
        _path = os.path.expanduser(r'~\Documents')
        timenow = now.strftime("%d%m%Y_%H_%M_%S")
        name = timenow + ".json"
        filename = _path + '\\' + name
        with open(filename, 'w') as outfile:
            json.dump(results, outfile)

