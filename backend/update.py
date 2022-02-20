import requests
import datetime
import json
import structures


def get_api():
    payload = {'AccountAPIKey': '7938FC89-A15C-492D-9566-12C961BC1F27'}
    r = requests.get('https://goboardapi.azurewebsites.net/api/FacilityCount/GetCountsByAccount', params=payload)
    return r


def api_to_json():
    apiCall = get_api().text
    json_dict = json.loads(apiCall)
    apiParsed = parse_json(json_dict)
    return apiParsed


def parse_json(json_dict):
    parsed = []
    for i in range(5):
        parsed.append(json_dict[structures.tupleCount[i]])
    return parsed


def get_date(parsed_json):
    track = datetime.date(int(parsed_json[0]["LastUpdatedDateAndTime"][0:4]),
                          int(parsed_json[0]["LastUpdatedDateAndTime"][5:7]),
                          int(parsed_json[0]["LastUpdatedDateAndTime"][8:10]))

    level3 = datetime.date(int(parsed_json[1]["LastUpdatedDateAndTime"][0:4]),
                           int(parsed_json[1]["LastUpdatedDateAndTime"][5:7]),
                           int(parsed_json[1]["LastUpdatedDateAndTime"][8:10]))

    level2 = datetime.date(int(parsed_json[2]["LastUpdatedDateAndTime"][0:4]),
                           int(parsed_json[2]["LastUpdatedDateAndTime"][5:7]),
                           int(parsed_json[2]["LastUpdatedDateAndTime"][8:10]))

    level1 = datetime.date(int(parsed_json[3]["LastUpdatedDateAndTime"][0:4]),
                           int(parsed_json[3]["LastUpdatedDateAndTime"][5:7]),
                           int(parsed_json[3]["LastUpdatedDateAndTime"][8:10]))

    powerHouse = datetime.date(int(parsed_json[4]["LastUpdatedDateAndTime"][0:4]),
                               int(parsed_json[4]["LastUpdatedDateAndTime"][5:7]),
                               int(parsed_json[4]["LastUpdatedDateAndTime"][8:10]))

    return track, level3, level2, level1, powerHouse


def get_time(parsed_json):
    track = parsed_json[0]["LastUpdatedDateAndTime"][parsed_json[0]["LastUpdatedDateAndTime"].
                                                         index('T') + 1:parsed_json[0]["LastUpdatedDateAndTime"].index(
        '.')]

    if int(track[3:5]) > 30:  # rounds down to nearest half hour
        track = track[0:3] + "30"
    else:
        track = track[0:3] + "00"

    level3 = parsed_json[1]["LastUpdatedDateAndTime"][parsed_json[1]["LastUpdatedDateAndTime"].
                                                          index('T') + 1:parsed_json[1]["LastUpdatedDateAndTime"].index(
        '.')]

    if int(level3[3:5]) > 30:  # rounds down to nearest half hour
        level3 = level3[0:3] + "30"
    else:
        level3 = level3[0:3] + "00"

    level2 = parsed_json[2]["LastUpdatedDateAndTime"][parsed_json[2]["LastUpdatedDateAndTime"].
                                                          index('T') + 1:parsed_json[2]["LastUpdatedDateAndTime"].index(
        '.')]

    if int(level2[3:5]) > 30:  # rounds down to nearest half hour
        level2 = level2[0:3] + "30"
    else:
        level2 = level2[0:3] + "00"

    level1 = parsed_json[3]["LastUpdatedDateAndTime"][parsed_json[3]["LastUpdatedDateAndTime"].
                                                          index('T') + 1:parsed_json[3]["LastUpdatedDateAndTime"].index(
        '.')]

    if int(level1[3:5]) > 30:  # rounds down to nearest half hour
        level1 = level1[0:3] + "30"
    else:
        level1 = level1[0:3] + "00"

    powerHouse = parsed_json[4]["LastUpdatedDateAndTime"][parsed_json[4]["LastUpdatedDateAndTime"].
                                                              index('T') + 1:parsed_json[4][
                                                              "LastUpdatedDateAndTime"].index('.')]

    if int(powerHouse[3:5]) > 30:  # rounds down to nearest half hour
        powerHouse = powerHouse[0:3] + "30"
    else:
        powerHouse = powerHouse[0:3] + "00"

    return track, level3, level2, level1, powerHouse


def get_day(trackDate, lvl3Date, lvl2Date, lvl1Date, phDate):
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    return days[trackDate.weekday()], days[lvl3Date.weekday()], days[lvl2Date.weekday()], days[lvl1Date.weekday()], days[phDate.weekday()]


def get_last_count(parsed_json):
    track = parsed_json[0]['LastCount']
    level3 = parsed_json[1]['LastCount']
    level2 = parsed_json[2]['LastCount']
    level1 = parsed_json[3]['LastCount']
    powerHouse = parsed_json[4]['LastCount']
    return track, level3, level2, level1, powerHouse


def update_structure():
    parsed_json = api_to_json()
    trackTime, lvl3Time, lvl2Time, lvl1Time, phTime = get_time(parsed_json)
    trackDate, lvl3Date, lvl2Date, lvl1Date, phDate = get_date(parsed_json)
    trackDay, lvl3Day, lvl2Day, lvl1Day, phDay = get_day(trackDate, lvl3Date, lvl2Date, lvl1Date, phDate)
    trackLC, lvl3LC, lvl2LC, lvl1LC, phLC = get_last_count(parsed_json)

    structures.track_week[trackDay].times[trackTime][0] = structures.track_week[trackDay].times[trackTime][0] + trackLC
    structures.track_week[trackDay].times[trackTime][1] = structures.track_week[trackDay].times[trackTime][1] + 1

    structures.level3_week[lvl3Day].times[lvl3Time][0] = structures.level3_week[lvl3Day].times[lvl3Time][0] + lvl3LC
    structures.level3_week[lvl3Day].times[lvl3Time][1] = structures.level3_week[lvl3Day].times[lvl3Time][1] + 1

    structures.level2_week[lvl2Day].times[lvl2Time][0] = structures.level2_week[lvl2Day].times[lvl2Time][0] + lvl2LC
    structures.level2_week[lvl2Day].times[lvl2Time][1] = structures.level2_week[lvl2Day].times[lvl2Time][1] + 1

    structures.level1_week[lvl3Day].times[lvl1Time][0] = structures.level1_week[lvl1Day].times[lvl1Time][0] + lvl1LC
    structures.level1_week[lvl3Day].times[lvl1Time][1] = structures.level1_week[lvl1Day].times[lvl1Time][1] + 1

    structures.power_week[phDay].times[phTime][0] = structures.power_week[phDay].times[phTime][0] + phLC
    structures.power_week[phDay].times[phTime][1] = structures.power_week[phDay].times[phTime][1] + 1
    
    pass


def get_weeks():
    return structures.track_week, structures.level3_week, structures.level2_week, structures.level1_week, structures.power_week
