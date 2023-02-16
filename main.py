import numpy as np
import re

from acquire_text_from_file import Cleaner, FileReader


if __name__ == '__main__':

    job_posts_df = FileReader('./job_posts/data_job_posts.csv', 'csv').__post_init__()
    job_posts_df = job_posts_df.replace(np.nan, '')

    it_job_posts_df = job_posts_df.copy()
    it_job_posts_df = it_job_posts_df[it_job_posts_df['IT'] == np.True_].reset_index()
    it_job_posts_df['total_text'] = \
        it_job_posts_df['JobDescription'] + it_job_posts_df['JobRequirment'] + it_job_posts_df['RequiredQual']

    example_post = it_job_posts_df['total_text'][4]
    cleaned_post = Cleaner(example_post).__post_init__()

    skills_df = FileReader('./skill_taxonomy/digitalSkillsCollection_en.csv', 'csv').__post_init__()

    skills_dict = {}

    for _, name in skills_df.iterrows():
        clean_label = re.sub(r'\(.+\)', '', name['preferredLabel'])

        try:
            if '|' in name['altLabels']:
                skill_synonyms = name['altLabels'].split('|')
                skills = [Cleaner(skill).__post_init__() for skill in skill_synonyms]

                skills.append(Cleaner(clean_label).__post_init__())

                skills_dict[Cleaner(clean_label).__post_init__()] = list(set(skills))

            else:

                skills = [Cleaner(name['altLabels']).__post_init__(), Cleaner(clean_label).__post_init__()]
                skills_dict[Cleaner(clean_label).__post_init__()] = list(set(skills))

        except TypeError:
            continue

    print(skills_dict.keys())
