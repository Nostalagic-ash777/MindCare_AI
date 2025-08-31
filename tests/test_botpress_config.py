import json
def test_config_keys():
    with open('../config/config.json') as f:
        config = json.load(f)
    required_keys = ["botId", "hostUrl", "clientId"]
    for key in required_keys:
        assert key in config, f"{key} missing in config.json"
