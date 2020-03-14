import os
import re

REF_PREFIX = "refs/tags/"

github_ref = os.environ["GITHUB_REF"]
VERSION=re.sub(REF_PREFIX, '',github_ref)
