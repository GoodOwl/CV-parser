import os
import pandas as pd
from resume_parser import resumeparse

CV_FOLDER = "/tmp/cv_folder"
EXCEL_PATH = "/tmp/cv_folder/summary.xls"

data = {"email": [], "phone": [], "name": [], "total_exp": [], "university": [], "designition": [], "degree": [], "skills": [], "Companies worked at": []}

for filename in os.listdir(CV_FOLDER):
    parsed_resume = resumeparse.read_file('/path/to/resume/file')

    # Maybe some more processing will be required, i.e ', '.join(parsed_resume["skills"])
    data["email"].append(parsed_resume["email"])
    data["phone"].append(parsed_resume["phone"])
    data["name"].append(parsed_resume["name"])
    data["total_exp"].append(parsed_resume["total_exp"])
    data["university"].append(parsed_resume["university"])
    data["designition"].append(parsed_resume["designition"])
    data["degree"].append(parsed_resume["degree"])
    data["skills"].append(parsed_resume["skills"])
    data["Companies worked at"].append(parsed_resume["Companies worked at"])


df = pd.DataFrame(data)
df.to_excel(EXCEL_PATH, index=False)
