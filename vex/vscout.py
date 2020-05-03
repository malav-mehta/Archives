import requests
from operator import itemgetter

team_file = open("teams.txt", 'r')
team_list = []
teams = []

for team in team_file:
    team_list.append(team)

event = team_list[0][:-1]
team_list = team_list[1:]

for i in range(len(team_list)):
    team_list[i] = team_list[i][:-
                                1] if i != len(team_list) - 1 else team_list[i]


season = "Tower Takeover"
program = "VRC"
options = {
    "info": {
        "disable": len(team_list) != 1,
        "desc": True,
        "rank": True,
        "skills": True,
        "stats": True,
    },
    "rank": {
        "disable": len(team_list) == 1,
        "season_rank": True,
        "events_rank": True,
        "custom_rank": False,
    }
}

sku = "RE-VRC-" + event
api_ref = "https://api.vexdb.io/get_"
api_key = "result"
api_attrs = {
    't': ("team", team_list),
    's': ("season", season),
    'p': ("program", program),
    'k': ("sku", sku)
}


def fetch_data(aspect, attrs, team):
    url = api_ref + aspect + '?'
    all_attrs = ""

    for x in list(attrs):
        all_attrs += '&' + api_attrs[x][0] + '='
        all_attrs += team_list[team] if x == 't' else api_attrs[x][1]

    url += all_attrs[1:]
    return requests.get(url).json()[api_key]


def max_key(arr, key):
    x = arr[0][key]
    index = 0
    rank = 0

    for i in range(1, len(arr)):
        if arr[i][key] >= x:
            index = i
            x = arr[i][key]
        if arr[i]["sku"] == sku:
            rank = arr[i]["rank"]

    return x, arr[index]["sku"], rank


def ave_key(arr, key):
    count = len(arr)
    result = 0

    for i in range(len(arr)):
        result += arr[i][key]

    return round(result/count, 6)


def retrieve(index):
    team = {}

    description = fetch_data("teams", "t", index)[0]
    keys = ["number", "team_name", "organisation", "city", "region"]
    for key in keys:
        team[key] = description[key]

    rank = fetch_data("season_rankings", "tsp", index)[0]
    keys = ["vrating", "vrating_rank"]
    for key in keys:
        team[key] = rank[key]

    skills = fetch_data("skills", "ts", index)
    team["total"], team["robot"], team["auton"], team["event_rank"] = 0, 0, 0, 0

    if skills != []:
        team["total"], skills_sku, team["event_rank"] = max_key(
            skills, "score")
        team["robot"] = requests.get("https://api.vexdb.io/get_skills?team={0}&sku={1}&type=0".format(
            team_list[index], skills_sku)).json()["result"][0]["score"]
        team["auton"] = requests.get("https://api.vexdb.io/get_skills?team={0}&sku={1}&type=1".format(
            team_list[index], skills_sku)).json()["result"][0]["score"]

    stats = fetch_data("rankings", "tsp", index)
    team["event_rank"] = dict_search(stats, sku)
    keys = ["wins", "losses", "ties", "wp", "ap",
            "sp", "max_score", "opr", "dpr", "ccwm"]
    for key in keys:
        team[key] = ave_key(stats, key)

    return team


def dict_search(arr, value):
    for x in arr:
        if x["sku"] == value:
            return x["rank"]
    return 5000


def list_teams(teams, key):
    for i, team in enumerate(teams):
        print("%s:\033[92m %4s\033[96m %6s\033[00m | %s" %
              (i + 1, round(team[key], 2) if team[key] != 5000 else "N/A", team["number"], team["team_name"]))


def show(team):
    to_show = options["info"]

    if to_show["desc"]:
        print("DESCRIPTION " + "\033[91m {}\033[00m".format(team["number"]))
        print("Team: %s // %s\nFrom: %s (%s, %s)\n" %
              (team["number"], team["team_name"], team["organisation"], team["city"], team["region"]))

    if to_show["rank"]:
        print("RANKINGS")
        print("VRating: %s\nVRtRank: %s\nEventRk: %s\n" %
              (team["vrating"], team["vrating_rank"], team["event_rank"]))

    if to_show["skills"]:
        print("SKILLS")
        print("Robot: %s\nAuton: %s\nTotal: %s\n" %
              (team["robot"], team["auton"], team["total"]))

    if to_show["stats"]:
        print("AV STATS")
        print("Wins: %s\tLosses: %s\tTies: %s\nWP: %s\tAP: %s\tSP: %s\nOPR: %s\tDPR: %s\tCCWM: %s" %
              (team["wins"], team["losses"], team["ties"], team["wp"], team["ap"], team["sp"], team["opr"], team["dpr"], team["ccwm"]))


def fill_teams():
    tmp_teams = []
    for i in range(len(team_list)):
        tmp_teams.append(retrieve(i))
    return tmp_teams


teams = fill_teams()
if not options["info"]["disable"]:
    for team in teams:
        show(team)

if not options["rank"]["disable"]:
    if options["rank"]["season_rank"]:
        teams = sorted(teams, key=itemgetter('vrating'), reverse=True)
        print("SEASON RANKED LIST")
        list_teams(teams, 'vrating')
        print()
    if options["rank"]["events_rank"]:
        teams = sorted(teams, key=itemgetter('event_rank'))
        print("EVENT RANKED LIST")
        list_teams(teams, 'event_rank')
        print()
    if options["rank"]["custom_rank"]:
        print("CUSTOM RANKED LIST")
        teams = sorted(teams, key=itemgetter('wp'), reverse=True)
        print()
        list_teams(teams, 'wp')
