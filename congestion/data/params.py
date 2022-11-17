import os

LTA_API_HEADERS = {'AccountKey' : os.environ["LTA_ACCOUNT_KEY"]}
LOCAL_DATA_PATH = os.path.expanduser(os.environ["LOCAL_DATA_PATH"])

PROJECT = os.environ["PROJECT"]
DATASET = os.environ["SPEEDS_DATASET"]
BUCKET_NAME = os.environ["BUCKET_NAME"]
VM_DATA_PATH = os.environ['VM_DATA_PATH']
MACHINE = os.environ['MACHINE']


# TODO: Validations
# ################## VALIDATIONS #################

# env_valid_options = dict(
#     DATASET_SIZE=["1k", "10k", "100k", "500k", "50M", "new"],
#     VALIDATION_DATASET_SIZE=["1k", "10k", "100k", "500k", "500k", "new"],
#     DATA_SOURCE=["local", "big query"],
#     MODEL_TARGET=["local", "gcs", "mlflow"],)

# def validate_env_value(env, valid_options):
#     env_value = os.environ[env]
#     if env_value not in valid_options:
#         raise NameError(f"Invalid value for {env} in `.env` file: {env_value} must be in {valid_options}")


# for env, valid_options in env_valid_options.items():
#     validate_env_value(env, valid_options)
