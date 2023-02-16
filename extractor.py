from dataclasses import dataclass
from tqdm import tqdm

from acquire_text_from_file import Cleaner


@dataclass
class SkillExtractor:

    file_collection: list
    skill_list: list

    def __post_init__(self) -> dict:

        counter_skills = {}

        for index, job in enumerate(tqdm(self.file_collection)):

            matched_skills = []

            cleaned_post = Cleaner(job).__post_init__()

            for word in cleaned_post:
                if word in self.skill_list:

                    matched_skills.append(word)

                else:
                    continue

            counter_skills[index] = list(set(matched_skills))

        return counter_skills
