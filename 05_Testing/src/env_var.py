import os


def use_env_var():
    contract_class = os.environ["CONTRACT_CLASS"]
    if contract_class == "en_cloud":
        # do some processing
        return "this is en_cloud"
    if contract_class == "en_onprem":
        # do some processing
        return "this is en_onprem"
    raise ValueError(f"contract class {contract_class} not found")
