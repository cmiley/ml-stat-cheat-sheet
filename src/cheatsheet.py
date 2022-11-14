import json
from pathlib import Path
import operator


class Topic:
    def __init__(self, title: str, description: str, tags: list, equation: str = None):
        self.title = title
        self.description = description
        self.tags = tags
        self.equation = equation

    def generate_topic_markdown(self):
        pass


TOPICS_FILE = 'topics.yaml'
TOPIC_TITLES = 'topics.txt'
EMPTY_TOPIC_JSON = 'empty_topics.json'


def generate_topic_json_from_txt(list_of_topics: Path or str, output_file: Path or str):
    with open(list_of_topics, "r") as f:
        topics = []

        for topic in f.readlines():
            topic_dict = {
                "title": topic.replace('\n', ''),
                "description": "",
                "tags": [],
                "equation": None,
                "resources": []
            }
            topics.append(topic_dict)

    topics = sorted(topics, key=lambda d: d['title'])

    with open(output_file, "w") as out_f:
        json.dump(topics, out_f, indent=4, sort_keys=False)


def main():
    generate_topic_json_from_txt(TOPIC_TITLES, EMPTY_TOPIC_JSON)


if __name__ == "__main__":
    main()
