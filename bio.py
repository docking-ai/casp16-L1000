import yaml

with open('bio.yaml', 'r') as file:
    yaml_content = yaml.safe_load(file)

target_raw = yaml_content['target'].split("|")

target_info = target_raw[0]
target = target_raw[1]

