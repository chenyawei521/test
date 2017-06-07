import ConfigParser

def read_config():
    config = ConfigParser.ConfigParser()
    with open(config_path, "r") as cfg_file:
        config.readfp(cfg_file)
        bson_path = config.get("local", "bson_path")
        knowledge_path = config.get("local", "knowledge_path")
    return bson_path, knowledge_path
