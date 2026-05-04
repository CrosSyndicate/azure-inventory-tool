import os
# Commenting out previous config to further break/fix practice
#
# Re-introducing this code will allow the app to run locally.
#
# USE_MOCK = os.getenv("USE_MOCK", "true").lower() == "true"

USE_MOCK_VALUE = os.getenv("USE_MOCK")

if USE_MOCK_VALUE is None:
    raise RuntimeError("USE_MOCK environment variable is required.")

USE_MOCK = USE_MOCK_VALUE.lower() == "true"
