# Project: Data Lake with Spark

## Introduction

<p>A music streaming startup, Sparkify, has grown their user base and song database even more and want to move their data warehouse to a data lake. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.</p>

<p>Sparkify want to build an ETL pipeline that extracts their data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables. This will allow their analytics team to continue finding insights in what songs their users are listening to.</p>


## Project Datasets

### Song Dataset

The first dataset is a subset of real data from the [Million Song Dataset](http://millionsongdataset.com/).
Each file is in JSON format and contains metadata about a song and the artist of that song. 

The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

>**s3://udacity-dend/song_data/A/B/C/TRABCEI128F424C983.json**<br>
>**s3://udacity-dend/song_data/A/A/B/TRAABJL12903CDCF1A.json**

Below is an example of what a single song file, **TRAABJL12903CDCF1A.json**, looks like.<br>
```
{
    "num_songs": 1, 
    "artist_id": "ARJIE2Y1187B994AB7", 
    "artist_latitude": null, 
    "artist_longitude": null, 
    "artist_location": "", 
    "artist_name": "Line Renaud", 
    "song_id": "SOUPIRU12A6D4FA1E1", 
    "title": "Der Kleine Dompfaff", 
    "duration": 152.92036, <br>
    "year": 0    
}
```
### Log Dataset

The second dataset consists of log files in JSON format generated by this [event simulator](https://github.com/Interana/eventsim) based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

The log files in the dataset are partitioned by year and month. For example, here are filepaths to two files in this dataset.

>**s3://udacity-dend/log_data/2018/11/2018-11-12-events.json**<br>
>**s3://udacity-dend/log_data/2018/11/2018-11-13-events.json**

Below is an example of what the data in a log file, **2018-11-12-events.json**, looks like.
![Log data example!](./image/log-data.png "Log data example")

## Data Modeling with Star Schema

![Star Schema for Song Play Analysis!](./image/song_play_analysis_with_star_schema.png "Star Schema for Song Play Analysis")

## <br>Data Lake to store extracted dimentional tables
>**"s3a://udacity-de-sparkify-data-warehouse-2/artists" <br>
>"s3a://udacity-de-sparkify-data-warehouse-2/songs" <br>
>"s3a://udacity-de-sparkify-data-warehouse-2/time" <br>
>"s3a://udacity-de-sparkify-data-warehouse-2/users" <br>
>"s3a://udacity-de-sparkify-data-warehouse-2/songplays"**<br>


## <br>Project Files

In addition to the data files, the project workspace includes 5 files:

**1. dl.cfg**                    contains the configuration settings for the database.<br>
**2. create_bucket.py**
**3. etl.py**  loading song data and log data from S3 to Redshift, transforms data into a set of dimensional tables <br>
**4. etl.ipynb**                 used to design ETL pipelines <br>
**5. README.md**                 provides project info<br>

## Configuration

Remember to set key and secret in **./aws/dl.cfg** before run **etl.py**<br>

[AWS]<br>
key = <br>
secret = <br>

## Build ETL Pipeline

**etl.py** will process the entire datasets.


## Instruction

1. Set **key** and **secrect** in **dwh.cfg** file <br><br>

2. Run **create_bucket.py**<br>
    python create_bucket.py <br> <br>
    
3. Use following command to start ETL process <br>
    python etl.py <br> <br>
   
    
## Author

**Xingya Zhou**
    


