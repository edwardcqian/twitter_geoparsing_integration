from mordecai import Geoparser

class VCGeotagger:
    def __init__(self):
        self.geo = Geoparser()
        with open ("US_CA.txt", "r") as myfile:
            long_short_state = myfile.read()
        long_short_state = long_short_state.split('\n')

        long_short_state = [ent.split('-') for ent in long_short_state]

        long_short_state[9] = ['Georgia United States', 'GA']

        self.state_dict = {a[1]: a[0] for a in long_short_state}

    def remove_non_ascii(self,text):
        return ''.join(i for i in text if ord(i)<128)

    def geotag(self, text):
        text = self.remove_non_ascii(text)
        result = self.geo.geoparse(text)
        if not result:
            return "None", "None"
        for r in result:
            if r['country_predicted'] == 'USA' and 'geo' in r:
                state = r['geo']['admin1']
                city = r['geo']['place_name'] 
                if state != city:
                    return city, state 
                else:
                    return "None", state

    def placetag(self, text):
        tmp_list = text.split(', ')
        if len(tmp_list) == 2:
            if tmp_list[1] in self.state_dict:
                state = self.state_dict[tmp_list[1]]
            else:
                state = tmp_list[1]
            city = tmp_list[0]
        else:
            state = 'None'
            city = 'None'
        return city, state
        