Let's assume a 20:1 read/write ratio (read/upload)
Let's assume 500M uploads a month

10B reads/views a month
192 uploads per second
3840 views a second

Let's assume that we will allow up to 20MB images to be sent, but we then
downsize them. To say, 1MB.  This equates to 192 MB/s needing to be stored.  If
we store this forever, then we will definitely need a lot a lot of storage.
    Let's say that at some point we can move files from S3 to some arctic
    storage service after say 2 years. 192 MB/s equates to 500M MB or 500K GB
    or 500 TB per month.  After 2 years, this is 500 * 24 == 12000 TB of storage


3840 * 60 * 60 * 24 == 331M views per day
20% of 331M = 66M photos to cache


Traffic: 192 uploads/s, 3840 visit/s
Storage: 12000 TB/2 years
Bandwidth: 192 uploads * 20 MB == 3840 MB per second. 3840 views * 1 MB ==
           3840 MB per second.
Memory: 66M MB = 66K GB = 66 TB 


API

getPhoto(uuid: str, requester: User) -> List[str]: ...
downloadPhoto(uuid: str, requester: User) -> ...
uploadPhoto(image: Image, title: str, uploader: User) -> bool: ...
searchPhotos(query: str, requester: User) -> List[str]: ...

followUser(followee: User, follower: User) -> bool: ...
getTopPhotos(user: User) -> List[Image]: ...


Database

Photo
| uuid | uploader | created | title | location_key

Users
| uuid | username | ...

Followers
| PK | userID1 | userID2 |


We could partition based on Photo IDs.  Suppose we had 10 shards, then we could
do PhotoID % 10 to get the partition.  This would evenly distribute the photos.
    * If we partition based on Photo IDs then generating photo IDs becomes
      challenging, because some outside service must generate the photo ID
      before the shard is selected.
    * One solution is to create a separate DB instance to generate
      auto-incrementing DBs.  You could use two or more and then make sure that
      their auto incrementing values do not overlap by having them count by an
      increment and start at a different number.
    * Then you can stick an LB in front of the DB instance service.
    * Alternatively, you could have a key generation service similar to what we
      did in TinyURL.
