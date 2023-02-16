import numpy as np
import os

from acquire_text_from_file import FileReader
from extractor import SkillExtractor
from matcher import SkillMatcher


if __name__ == '__main__':

    job_posts_df = FileReader('./job_posts/job_posts.csv', 'csv').__post_init__()
    job_posts_df = job_posts_df.replace(np.nan, '')

    it_job_posts_df = job_posts_df.copy()

    # Was used to make a subset of only it job posts, this will not be needed anymore.
    # it_job_posts_df = it_job_posts_df[it_job_posts_df['IT'] == np.True_].reset_index()

    it_job_posts_df['total_text'] = \
        it_job_posts_df['JobDescription'] + it_job_posts_df['JobRequirment'] + it_job_posts_df['RequiredQual']

    skills = ['python', 'aws', 'google', 'gcp', 'pyspark', 'terraform', 'pentaho', 'powerbi', 'tableau', 'docker',
              'git', 'php', 'html', 'css', 'java', 'javascript', 'sql', 'postgresql', 'nosql', 'pytorch', 'tensorflow',
              'machine learning', 'bash', 'agile', 'scrum', 'microsoft', 'azure', 'qlikview', 'cloud', 'quicksight',
              'ci/cd', 'linux', 'matlab', 'nlp', 'jira']

    job_posts = it_job_posts_df['total_text'].tolist()

    extracted_job_skills = SkillExtractor(job_posts, skills).__post_init__()

    file_directory = 'incentro_cvs'
    cv_text_strings = []
    consultant_names = []

    for file_name in os.listdir(file_directory):

        consultant_name = file_name.replace('CV - ', '').replace('.txt', '').replace(' ', '_')
        consultant_names.append(consultant_name)

        file_path = f"{file_directory}/{file_name}"
        file_text = FileReader(file_path, 'txt').__post_init__()
        cv_text_strings.append(file_text)

    extracted_cv_skills = SkillExtractor(cv_text_strings, skills).__post_init__()

    # Zip the names of the consultant and the skills of the dictionary
    zip_names_cv_skills = {name: key_value[1] for key_value, name in zip(extracted_cv_skills.items(), consultant_names)}

    best_matches_by_index = SkillMatcher(
        zip_names_cv_skills,
        extracted_job_skills,
        'Thierry_Ernest',
        5
    ).__post_init__()

    print(it_job_posts_df['total_text'][best_matches_by_index[0][0]])
    print(best_matches_by_index[1])
    print(best_matches_by_index[2])

    # Code snippet for ontology/taxonomy
    # skills_df = FileReader('./skill_taxonomy/digitalSkillsCollection_en.csv', 'csv').__post_init__()
    #
    # skills_dict = {}
    #
    # for _, name in skills_df.iterrows():
    #     clean_label = re.sub(r'\(.+\)', '', name['preferredLabel'])
    #
    #     try:
    #         if '|' in name['altLabels']:
    #             skill_synonyms = name['altLabels'].split('|')
    #             skills = [Cleaner(skill).__post_init__() for skill in skill_synonyms]
    #
    #             skills.append(Cleaner(clean_label).__post_init__())
    #
    #             skills_dict[Cleaner(clean_label).__post_init__()] = list(set(skills))
    #
    #         else:
    #
    #             skills = [Cleaner(name['altLabels']).__post_init__(), Cleaner(clean_label).__post_init__()]
    #             skills_dict[Cleaner(clean_label).__post_init__()] = list(set(skills))
    #
    #     except TypeError:
    #         continue
    #
    # print(skills_dict.keys())
