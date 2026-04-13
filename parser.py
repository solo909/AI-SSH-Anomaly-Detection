import pandas as pd
import re

def parse_log(file_path):
    data = []

    with open(file_path, "r") as f:
        for line in f:
            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)

            if ip_match:
                ip = ip_match.group()
                status = "failed" if "Failed" in line else "success"

                data.append([ip, status])

    df = pd.DataFrame(data, columns=["ip", "status"])
    return df