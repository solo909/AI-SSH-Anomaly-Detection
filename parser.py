import pandas as pd
import re
from datetime import datetime

PASSWORD_PATTERN = re.compile(
    r'^(?P<timestamp>\w{3}\s+\d+\s+\d+:\d+:\d+)'
    r'.*sshd\[\d+\]:\s+(?P<auth>Failed|Accepted) password for (?:invalid user )?(?P<user>\S+)'
    r' from (?P<ip>\d+\.\d+\.\d+\.\d+)'
)

INVALID_USER_PATTERN = re.compile(
    r'^(?P<timestamp>\w{3}\s+\d+\s+\d+:\d+:\d+)'
    r'.*sshd\[\d+\]:\s+Invalid user (?P<user>\S+)'
    r' from (?P<ip>\d+\.\d+\.\d+\.\d+)'
)

def parse_log(file_path):
    data = []

    with open(file_path, "r") as f:
        for line in f:
            m = PASSWORD_PATTERN.search(line)
            if m:
                timestamp = datetime.strptime(m.group("timestamp"), "%b %d %H:%M:%S").replace(year=datetime.now().year)
                status = "success" if m.group("auth") == "Accepted" else "failed"
                data.append([timestamp, m.group("ip"), m.group("user"), status])
                continue

            m = INVALID_USER_PATTERN.search(line)
            if m:
                timestamp = datetime.strptime(m.group("timestamp"), "%b %d %H:%M:%S").replace(year=datetime.now().year)
                data.append([timestamp, m.group("ip"), m.group("user"), "failed"])

    df = pd.DataFrame(data, columns=["timestamp", "ip", "user", "status"])
    return df