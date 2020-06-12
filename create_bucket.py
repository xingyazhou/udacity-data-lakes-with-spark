import boto3

def create_s3_bucket(s3, bucket_root, keys):
    '''Create the bucket root and the folders in AWS S3
    s3(object): resource object
    bucket_root(string): The name of the bucket to be created
    keys(list): a list of folder_names(string) to create within the bucket
    '''
    # Create the root bucket
    try:
        s3.create_bucket(ACL='private',Bucket=bucket_root,
                             CreateBucketConfiguration={'LocationConstraint':'us-west-2'})
    except Exception as e:
        if 'BucketAlreadyOwnedByYou' in str(e):
            print(f'{bucket_root} already exists')
        else:
            raise e
    buck = s3.Bucket(bucket_root)

    # Create folders for the tables
    for key in keys:
        key_name = f'{key}/'
        try: 
            buck.put_object(Key=key_name)
        except Exception as e:
            raise e
    print('Keys created')
            
if __name__=='__main__':
    
    s3 = boto3.resource('s3', region_name='us-west-2')
    
    create_s3_bucket(s3, bucket_root='udacity-sparkify-data-lake', 
                     keys = ['songs','songplays','time','artists','users'])