from dataclasses import dataclass


@dataclass
class CV:

    full_name: str
    cv_text: str
    skills_on_cv: list


@dataclass
class CVCollection:

    cv_dict: dict


@dataclass
class Job:

    function: str
    company_name: str
    job_description: str


@dataclass
class JobCollection:

    job_name: str
    job_skills: list


@dataclass
class Skill:

    skill_name: str
    skill_type: str


@dataclass
class SkillsCollections:

    skills_dict: dict
