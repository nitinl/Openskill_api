from dal.models import db, Skill
class SkillsDAL():
    def __init__(self):
        self.session = db.session

    def create_skill(self, skill_dict):
        db_skill = Skill(
            uuid = skill_dict.get("uuid",""),
            description = skill_dict.get("description",""),
            name = skill_dict.get("name",""),
            normalized_name = skill_dict.get("normalized_name",""),
            onet_element_id = skill_dict.get("onet_element_id",""),
            type = skill_dict.get("type",""),
            )
        self.session.add(db_skill)
        created_skill = self.session.commit()
        return created_skill

    def delete_skill(self):
        return skill_uuid

    def get_all_skills(self):
        skills = Skill.query.all()
        return Skill.serialize_list(skills)

    def get_skill(self, uuid):
        skill = Skill.query.filter_by(uuid=uuid).first()
        if skill:
            return Skill.serialize(skill)
        else:
            return None
    
