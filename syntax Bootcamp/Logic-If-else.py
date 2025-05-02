import os

DEVELOPER_MODE = "DEVELOPER_MODE"
PRODUCTION_MODE = "PRODUCTION_MODE"

if os.getenv("MODE") == DEVELOPER_MODE:
    print("Running in developer mode")
elif os.getenv("MODE") == PRODUCTION_MODE:
    print("Running in production mode")
else:
    print("Running in unknown mode")