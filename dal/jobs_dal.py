from dal.models import db, Job

class JobsDAL():
    def __init__(self):
        self.session = db.session
    
    def create_job(self,job_dict):
        db_job = Job(
            title=job_dict.get("title",""),
            uuid=job_dict.get("uuid",""),
            normalized_title=job_dict.get("normalized_job_title",""),
            parent_uuid=job_dict.get("parent_uuid",""),
            )
        self.session.add(db_job)
        created_job = self.session.commit()
        return created_job
    
    def delete_job(self):
        return job
    
    def get_all_jobs(self):
        jobs = Job.query.all()
        return Job.serialize_list(jobs)
    
    def get_job(self,uuid):
        job = Job.query.filter_by(uuid=uuid).first()
        if job:
            return Job.serialize(job)
        else:
            return None
    











