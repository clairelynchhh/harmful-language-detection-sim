'''
FILE TOO BIG FOR RAM -- IT CRASHES
A MODEL CAN USE BETWEEN 50K AND 100K FOR GOOD OUTPUT.
'''

# export part of the file
import gzip

input_path = "tar_data/gab_posts_jan_2018.json.tar.gz"
output_path = "data/gab_sample_50k.json"
n = 50_004  # exact number of posts to keep
count = 0


with gzip.open(input_path, "rt", encoding="utf-8") as infile, \
     open(output_path, "w", encoding="utf-8") as outfile:
   
    for line in infile:
        outfile.write(line)
        count += 1
        if count >= n:
            break


print(f"Saved exactly {count} lines to {output_path}")

# check file and remove initial .tar.gz metadata rows
import pandas as pd
import json


file_path = r"data\gab_sample_50k.json"
rows = []


with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)  # parse JSON
            rows.append(obj)
        except json.JSONDecodeError:
            continue  # skip non-JSON lines (like tar headers)


# create DataFrame from rows
df = pd.DataFrame(rows)


# extract the text content from each post
df['text'] = df['post'].apply(lambda x: x.get('body', '') if isinstance(x, dict) else '')


# keep only the text column
df = df[['text']]


# display settings
pd.set_option('display.max_colwidth', None)


# check the shape and first few rows
print(df.shape)
print(df.head(25))
