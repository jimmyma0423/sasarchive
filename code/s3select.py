import boto3
import sys
import warnings

warnings.filterwarnings("ignore")
BUCKET = sys.argv[1]
PREFIX = sys.argv[2]

# list prefixes in a bucket
def list_prefixes(bucket_name, prefix):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter='/')
    prefixes = []
    for content in response.get('CommonPrefixes',[]):        
        prefixes.append(content.get('Prefix').replace(prefix,'').strip('/'))    
    return prefixes

# list prefixes in a bucket and ask user to select one, invalid input will raise an exception
def select_prefix(bucket_name, prefix):
    prefixes = list_prefixes(bucket_name, prefix)
    for i, prefix in enumerate(prefixes):
        print ("\t", i, ":", prefix, file=sys.stderr)
    print ("Enter a number:", end=" ", file=sys.stderr)
    selected = int(input())
    return prefixes[selected]

try:
    print(select_prefix(BUCKET, PREFIX))
except:
    print("")
