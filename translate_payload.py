import json
import requests

long_string = "Interstate 196 (I-196) is an auxiliary Interstate Highway that runs for 80.6 " \
              "miles (129.7 km) in the US state of Michigan. It is a state trunkline highway " \
              "that links Benton Harbor, South Haven, Holland, and Grand Rapids. In Kent, " \
              "Ottawa, and Allegan counties, I-196 is known as the Gerald R. Ford Freeway, or" \
              " simply the Ford Freeway, after the 38th President of the United States, Gerald" \
              " Ford, who was raised in Grand Rapids and served Michigan in the House of Representatives" \
              " for 25 years. This name generally refers only to the section between Holland and Grand Rapids." \
              " I-196 changes direction; it is signed as a north–south highway from its southern terminus to the " \
              "junction with US Highway 31 (US 31) just south of Holland, and as an east–west trunkline from this" \
              " point to its eastern terminus at an interchange with I-96, its parent highway. " \
              "There are three business routes related to the main freeway.There are two business loops (BL I-196) " \
              "and one business spur (BS I-196) that serve South Haven, Holland and the Grand Rapids areas. Another " \
              "business spur for Muskegon had been designated relative to the I-196 number. " \
              "The freeway numbered I-196 is the second in the state to bear the number. " \
              "Originally to be numbered as part of the I-94 corridor in the state, the Benton" \
              " Harbor–Grand Rapids freeway was given the I-96 number in the 1950s while another " \
              "Interstate between Muskegon and Grand Rapids was numbered I-196. That I-196 was built " \
              "in the late 1950s and completed in the early 1960s. The first segment of the current I-196 " \
              "was opened as I-96 near Benton Harbor in 1962. Michigan officials requested a change in 1963" \
              " which reversed the two numbers, and the subsequent segments of freeway opened" \
              " northward to Holland and from Grand Rapids westward under the current number." \
              " The gap between Holland and Grandville was filled in the 1970s, and a section" \
              " of freeway that runs through downtown Grand Rapids was rebuilt as a wider freeway in 2010."

translate_dict = {'trgt': "es", 'text': long_string}

res = requests.post('http://localhost:8080/translate',
                    json=json.dumps(translate_dict))
if res.ok:
    print(res.text)
