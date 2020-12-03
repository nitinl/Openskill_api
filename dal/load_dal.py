from dal.jobs_dal import JobsDAL
from dal.skills_dal import SkillsDAL
from dal.models import db, Job, Skill
import requests
def load_data_from_externalapi():
    try:
        if len(db.session.query(Job).all()) == 0:
            response = requests.get(f"http://api.dataatwork.org/v1/jobs")
            jobs_results = response.json()
            print(jobs_results)
            print(len(jobs_results))
            if jobs_results and len(jobs_results) > 0:
                for each_job in jobs_results:
                    if each_job.get("uuid", None):
                        jobs_dal = JobsDAL()
                        created_job = jobs_dal.create_job(each_job)

        if len(db.session.query(Skill).all()) == 0:
            response = requests.get(f"http://api.dataatwork.org/v1/skills")
            skills_results = response.json()
            print(skills_results)
            print(len(skills_results))
            if skills_results and len(skills_results) > 0:
                for each_skill in skills_results:
                    if each_skill.get("uuid", None):
                        skills_dal = SkillsDAL()
                        created_skill = skills_dal.create_skill(each_skill)
        else:
            print("Job Information already exist in table")
    except Exception as excp:
        print(dict(error_message=str(excp)))
