import json

class ResultsService:
    def parse(self,results):
        result_list = []
        for item in results:
            parsed_item = json.dumps(item)
            list_item = json.loads(parsed_item)
            result_list.append(list_item)
        
        return result_list

    
