# internal file
import config
# standard libraries
import os
import json
# non-standard libraries
import requests


def url_request():
    headers = {"apikey": config.apikey}
    params = (("league_id", "236"),)
    response = requests.get('https://app.sportdataapi.com/api/v1/soccer/seasons', headers=headers, params=params)
    return response.json()


def save_object(file_name, saved_object, writing_method):
    saved_object = json.dumps(saved_object, indent=4, ensure_ascii=False)
    with open(file_name, writing_method) as handler:
        handler.writelines(saved_object)


def main():
    if not os.path.exists("data"):
        os.mkdir("data")

    response_json = url_request()
    save_object("data/premier_league_season.json", response_json, "w")


if __name__ == "__main__":
    main()
