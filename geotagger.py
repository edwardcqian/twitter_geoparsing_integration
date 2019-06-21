from mordecai import Geoparser

states = """Alabama-AL
Alaska-AK
Arizona-AZ
Arkansas-AR
California-CA
Colorado-CO
Connecticut-CT
Delaware-DE
Florida-FL
Georgia-GA
Hawaii-HI
Idaho-ID
Illinois-IL
Indiana-IN
Iowa-IA
Kansas-KS
Kentucky-KY
Louisiana-LA
Maine-ME
Maryland-MD
Massachusetts-MA
Michigan-MI
Minnesota-MN
Mississippi-MS
Missouri-MO
Montana-MT
Nebraska-NE
Nevada-NV
New Hampshire-NH
New Jersey-NJ
New Mexico-NM
New York-NY
North Carolina-NC
North Dakota-ND
Ohio-OH
Oklahoma-OK
Oregon-OR
Pennsylvania-PA
Rhode Island-RI
South Carolina-SC
South Dakota-SD
Tennessee-TN
Texas-TX
Utah-UT
Vermont-VT
Virginia-VA
Washington-WA
West Virginia-WV
Wisconsin-WI
Wyoming-WY
Alberta-AB
British Columbia-BC
Manitoba-MB
New Brunswick-NB
Newfoundland and Labrador-NL
Northwest Territories-NT
Nova Scotia-NS
Nunavut-NU
Ontario-ON
Prince Edward Island-PE
Quebec-QC
Saskatchewan-SK
Yukon-YT"""

class VCGeotagger:
    def __init__(self):
        self.geo = Geoparser()
        long_short_state = states.split('\n')

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
        