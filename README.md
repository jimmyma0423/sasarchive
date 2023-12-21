# Archive/Verify/Re-store Procedure
HEOR files archiving to S3
## Archiving
`cd <directory with files to archive>
archive
`
## Verification
`cd <directory with files to verify>
verify
`
## Restoring 
`restore`

## list all contents of a specific directory in S3
`python3 s3list.py "dm-analytical-projects-rwd-333697094175-us-east-1-non-prod" "restricted/DGOS/SAS Data Archive/"`