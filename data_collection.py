import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/juadi/Workspace/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 10, False, path, 5)

df.to_csv('glassdoor_jobs.csv', index = False)