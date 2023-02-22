import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/juadi/Workspace/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 5, False, path, 10)

df.to_csv('glassdoor_jobs_TEST2.csv', index = False)