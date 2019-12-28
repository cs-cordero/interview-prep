Let's assume there is a 50:1 read/write ratio
Let's assume there is 100M writes per month

There are 5B reads per month
There are ~38 writes per second
There are ~1900 reads per second

Let's say we store for 2 weeks

There are 100M writes per month, so we'd have to store 50M pastes, each of size
1MB. So 50M MB or 50K GB or 50TB

Let's say we allow up to 1MB in the textbox

Down 38MB per second
Up 1900MB per second

Let's say we cache maybe 20% of the incoming daily traffic.  So if there is
1900 reads per second, that translates to 164M reads per day or 164M MB or 164
TB of data we need to cache.
    Unfortunately this is way to big to store in memory as the biggest RAM
    storage is 256GB.  We could use a system of computers, but even then that
    would take 600+ servers each with 256GB in it to store 164TB.  Let's just
    assume we've got Google scale and can handle that no problem.

Traffic: 38 writes/s, 1900 reads/s
Storage: 50TB
Bandwidth:  38MB/s, 1900MB/s
Memory: 164TB

System APIs:

getPaste(key: int, user: User) -> str: ...
createPaste(user: User, body: str, expiry: datetime, alias: str) -> str: ...


pastes
| key | user | created | expiration | body |

users
| uuid | username | ... |

I'm choosing PostgreSQL, but I'm sure there's an argument to be made for using
a key-value NoSQL solution since there aren't many relations

Basic Design:
1. Upon creating the paste, we have to generate a unique link.
    1. We could hash the body of the text appended with the user to make it
       unique for each user.
    1. We could hash the body of the text and make it namespaced in the url
       under the user. (would this count as being guessable?, I argue no)

1 If we use a base64 encoding, we have to worry about the space representing
the full set of creatable unique strings, which is 64^N, where N is the number
of characters in the unique string we wish to create.

Concurrency shouldn't really be problematic with this approach since the data
cannot be updated.  If it could be updated without having to generate a new
paste, then yes, it could cause some problems, given that and subsequent
read/update after write could yield either the original, the updated, or some
frankenstein of the two.

No SPOFs.

We could cache between the client and the app server to serve subsequent reads
in an LRU fashion

For Partitioning, we will want to partition based on a consistent hashing
algorithm.  We could hash the user with the key together and then use the
ring'd consistent hashing approach to find the correct partition.

We should think about using a data storage like Amazon S3 if it helps to store
it that way.
