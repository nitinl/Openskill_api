from dal.skills_dal import SkillsDAL

def get_all_skills():
    skills_dal = SkillsDAL()
    skills = skills_dal.get_all_skills()
    return skills

def get_skill(request):
    if 'uuid' in request.args:
        uuid = str(request.args['uuid'])
    else:
        return "Error: No uuid field provided. Please specify a valid id."
    skills_dal = SkillsDAL()
    skill = skills_dal.get_skill(uuid)
    if not skill:
        return "Error: No skill with given uuid found. Please specify a valid id."
    else:
        return skill
    return skill









