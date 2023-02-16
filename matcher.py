from dataclasses import dataclass


@dataclass
class SkillMatcher:

    cv_skills_dict: dict
    job_skills_dict: dict
    consultant_name: str
    top_n: int

    def __post_init__(self):

        consultant_skills = self.cv_skills_dict[self.consultant_name]

        jobs_n_matches = []

        for index, job_skills in self.job_skills_dict.items():

            n_matches = sum(word in consultant_skills for word in job_skills)
            jobs_n_matches.append(n_matches)

        index_top_n = sorted(range(len(jobs_n_matches)), key=lambda i: jobs_n_matches[i])[-self.top_n:]

        return index_top_n, self.job_skills_dict[index_top_n[0]], consultant_skills
