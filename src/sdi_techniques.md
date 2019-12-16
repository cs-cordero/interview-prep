# Techniques and Tricks

## Key Generation Service
* A microservice that generates random strings that can be used as a
  reference key for some resource.
* Everytime a key from here is used, it should be marked or removed from
  the service storage so that it it is not used again.
* One way to mark them as used is to use two tables, one for used and one
  for available.  This helps to handle concurrency problems.  The KGS could
  load some keys in memory and immediately move them to used.  This ensures
  any requesting server would get unique keys.

## Auto-incrementing ID Generator DB
* A microservice that runs one or more DB instances that basically just has
  a single table with a single 64-bit int auto-incrementing column in it.
* If you run two or more in order for reliability, you would need to avoid
  having two DB instances generaate the same keys.  To avoid this, you
  could use an offset and an auto incrementing amount.  For example, if
  using two DBs, one could be set to start at 1 and count every 2 and the
  second DB could be set to start at 2 and count every 2.
* Place a LB in front of these DBs to help manage any failovers.

## Pre-generation
* If speed is of the essence (generating a news feed for Instagram for
  example), and you don't want the user to wait for seconds before the news
  feed comes up, you can think about pre-generating them and storing the
  results in a separate table.
* Dedicated servers could continuously generate news feeds and upsert them
  into some table.

## Baking information into the partition ID of a resource
* Suppose you have partitioned a bunch of photo resources across a set of
  shards.  You need to query for all the photos uploaded by a given user
  and sorted by their latest creation times.
* Imagine the Photo ID in its binary form.  You could specify a certain
  number of bits as an epoch time (number of seconds from some epoch).
* In the Instagram example given in the course, they specified that they
  wanted to be able to represent the number of seconds from an epoch for 50
  years.  There are 1.6 billion seconds in 50 years, so they need 31 bits
  to represent that number.  Then they could use an autoincrementer to
  increment the last 9 bits.
    * Thus, with a 40-bit photo ID, they are able to know the creation time
      baked right into the photo ID.

## Client Applications
* Client applications can be trusted to do many things, and you should consider
  breaking them down by their operations.
* Examples:
    * Uploading/downloading fiels
    * Detecting file changes in a file system.
    * Handling change conflicts in a synchronization step
    * Interacting with any of the services you have deployed.
    * Chunking files to prepare them for upload/download
    * Holding and storing metadata to minimize server requests and also support
      offline updating.
* When clients have to sync with the server, you have to consider push/pull
  options carefully.
    * Pull requires the server to request the server for metadata changes to
      know whether a diff exists.
        * Wastes bandwidth, since most of the time there will be no changes.
        * Keeps the server busy since you are sending frequent requests.
        * Could use long polling in a pull manner.
* Clients could and (maybe should) store its own internal DB.
* Ideas for components _within_ the client:
    * Chunker
        * A service that splits larger blobs of data into chunks and groups
          many chunks back into the original blob.
        * Could also be improved to detect chunks that were modified by the
          user and transfer only those parts to the Cloud Storage.
    * Watcher
        * A service that monitors the state of the environment that it's in.
          In the Dropbox example, the watcher keeps an eye on changes to the
          file system or changes broadcasted by the Synchronization service.
        * As explained above, a watcher service could also monitor state held
          externally, like for broadcasts from a server.
    * Indexer
        * A service that listens for events and does a lot of the heavy lifting
          and coordinatiion between the other components.  In the Dropbox
          example, this service uses the chunker and communicates to the
          external service to perform upload/downloads, updating metadata
          locally and on the metadata server, and uses the Synchronization
          service to broadcast changes.
    * Internal Metadata DB
        * A DB instance that keeps track of the metadata (versions, chunks,
          filenames, filesystem locations) that the application is tracking.

## Checking of a chunk of data matches another chunk of data
* Generate a SHA-256 of both chunks and compare the hashes, if they match then
  your data matches.
* Chunks that match even across different users do not need to be replicated.

## Communication Middleware
### Messaging Middleware
* A message queueing service is helpful for handling a substantial number of requests.
* Supports asynchronous, loosely coupled message-based communication
  message-based communication between distributed components of the system.
* It would be critical that the queue itself is highly available, reliable, and
  scalable.
* It is important to consider how many queues would need to be created, you
  could separate them into different types, like a Request queues and Response
  queues.
* You can also consider some queues to be global and shared across all clients.
  In the Dropbox example, all clients share a global request queue, but there
  are separate queues for each individual client.

## Data deduplication
* A technique used for eliminating duplicate copies of data to improve storage
  utilization.
* Implementations:
    * *Post-process deduplication*: New chunks are first stored on the storage
      device and later some process analyzes the data looking for
      deduplication.
        * Pros:  Clients don't have to wait for hash calculation/lookup to
          complete before storing data.
        * Cons:  In the meantime, we are storing duplicate data.  Duplicate
          data will be consuming bandwidth.
    * *In-line deduplication*:  Hash calculations are performed on the fly.  If
      the hash matches something that already exists in the metadata, then a
      reference to the existing chunk is made instead of the full chunk itself.
        * Pros:  Better network and sotrage usage
        * Cons:  If the hash calculation is slow, then uploads/downloads get slower.


## Long-Lived Connections
* If a client needs to maintain a long-lived connection to our system, we need
  to remember that servers have a limited number of connections that it can
  support concurrently.
* In order to quickly identify users to the server that they have a connection
  to, we could keep a hashmap of users to a connection object.
* Where to store this hashmap?  If we place a software LB in front of the
  connection servers, then we can store the hashmap there, and also replicate
  the hashmap data in other servers.
    * It could also be a microservice that sits internally that helps map user
      IDs to the server/gateway that user is serviced by.
* Mechanically, the connection can be maintained by HTTP long polling or with
  WebSockets.


## Push notifications
* Typically, a user must opt-in to receive push notifications.  Each
  manufacture for the environment that the client is operating on (mobile,
  browser, etc.)  maintains a set of servers that handles actually pushing the
  notification to the device/user.
* You can set up a separate Notification service that sends information to the
  manufacturer's push notification server.


## Handling Expensive Calculations
### Using a Queue for asynchronous processing
* A queue is a great tool for setting up expensive calculations that can happen
  asynchronously.  For example, in the Netflix example, videos uploaded to the
  server need to be compressed and encoded in multiple formats and resolutions.
* Furthermore, in the Netflix example, the encoding step must also generate
  many thumbnails, which are requested even moreso than the videos.

### Offline updating
* In the Typeahead example, we faced a situation where the input data for
  calculating frequencies was coming in at an incredible speed (every search
  query).
* Instead of performing the extremely expensive calculation, you can log all
  the inputs and then batch process them every hour.
* However, the servers are using a version of the trie they need to update in
  memory, so how do you update them without taking them down?
    * Use a master-slave system.  Update the slave, then swap them.

### Offline reloading (Permanent storage)
* If we need to be able to reload the trie that we created from the expensive
  calculation using logs that are ephemeral (aka we lose the logs after
  processing them in the batch process, or we don't want to re-read those logs),
  then we should think about how to serialize them to a file.


## When choosing between two options
* If it is not clear what the correct answer is, either present the options to
  the interviewer and ask them what they think.
* Failing that just say that it's hard to choose one without testing.


## Balancing load between cache servers
* You can use Consistent Hashing to help an LB balance load to a series of
  cache servers.
* In the Netflix example, this still doesn't solve the problem all the way
  because if a video gets hot, then the server it is cached too will experience
  a lot of hits.  You could choose to redirect clients to less busy servers,
  but this has some drawbacks, mainly related to latency.


## Data Partitioning
### Vertical Partitioning
* Partition the database in such a way that groups of tables related by feature
  are colocated on the same server.
* For example, all user related tables go in one database on one server, and
  all files/chunks related tables go in another database on another server.
* Pros:
    * Straightforward to implement
* Cons:
    * Could end up having drastic non-uniform distribution of data between your
      servers.  Usually one feature will generate more data than another.
    * You might need to further partition a feature if a server fails to store
      all of its data.
    * Joining tables between separate databases can cause performance and
      consistency issues.

### Range Based Partitioning
* Partition using a key that can be placed on a specified range.  For example,
  you could use the first letter of the key and partition based on the letter,
  or if your data was zip codes, you could partition based on if a zip code was
  between certain ranges.
* Pros:
    * Straightforward to implement
* Cons:
    * If the data you are using is not uniformly distributed along the ranges
      specified, then you also can end up with unbalanced servers.
    * Scaling it out if one server starts to get too large can be difficult

### Round Robin Partitioning
* Partition using `i % n` calculation in insertion order.
* Pros:
    * Probably the easiest to implement.
* Cons:
    * Difficult to further partition a given row of data into additional segments.
    * Joins could end up taking a performance hit.

### Hash Based Partitioning
* Partition using the hash value of some object or object attribute.
* Pros:
    * If coupled with Consistent Hashing, then you can achieve a uniform
      distribution of data among your servers.
* Cons:
    * Might need to come up with your own hashing function scheme.
    * The hash function you use should also still uniformly distribute data
      among its hash space.

### Partition based on maximum capacity of the server
* Partition a data structure based on the maximum memory capacity of the
  servers.  You basically fill up the server until it reaches capacity, and
  then you move to the next server.
* Requires a load balancer in front of the servers that keeps track of the map
  of the partition to the server.
* Pros:
    * Easier to work with for certain data structures, like tries.
* Cons:
    * Can still lead to hotspots.

### Logical Partitioning
* Just because you want to start off with one server doesn't mean you can't
  set a large partition count.  You could use a logical partition, which
  tricks the application in thinking that two partitions are separate, but
  then you could store multiple partitions on a single server.
* This is helpful as an approach because then once you grow, you can roll
  out logical partitions onto different servers as you needed it.
* To do this, you will need to maintain a config file or separate database
  to map logical partitions to the real servers.

## Search
* The trouble with setting up a system to support search is that you need to
  generate a massive, distributed search index that maps words to individual
  system objects that they could refer to.
* This requires a ton of space to maintain.  Special consideration must be made
  to understand how much space is required to maintain the system.
    * This usually looks like:  time in years to keep data * daily data generation * 365
    * Special consideration is needed to make sure you generate new IDs that
      are unique across teh whole system.
    * The Index looks like a big distributed hash table, where the key is a
      word and the value is a list of IDs that it points to.
    * Special consideration must be made to how to shard the index.
        * Either shard based on words (if specific words get hot then you can
          get nonuniformity)
        * Or shard based on the tweet objects (words can be duplicated across
          shards, but a given tweet ID is modded across the shards)

## Partitioning for Threading
* Sometimes you may want to partition a job by thread number.
* The use case for this is in the web crawler discussion where, in order to
  avoid overloading a given server, we could route all pages to the same domain
  to a single thread so that at any given time your system is only sending one
  request to that domain at a time.

## Throttling
### Types
* *Hard Throttling*:  The number of API requests cannot exceed the throttle
  limit.
* *Soft Throttling*:  We can set the API request limit to exceed a certain
  percentage.  For example if we have a rate-limit of 100 messages a minute and
  10% exceed-limit, our rate limiter will allow up to 110 messages per minute.
* *Elastic or Dynamic Throttling*:  The number of requests can go beyond the
  threshold if the system has resources available.  For example, if a user is
  allowed only 100 messages a minute, we can let the user send more than 100
  messages a minute when there are free resources available in the system.

### Algorithms
* *Fixed Window Algorithm*:  The time window is considered from the start of
  the time-unit to the end of the time-unit.  For example, a period would be
  considered 0-60 seconds for a minute irrespective of the time frame at which
  the API request has been made.
* *Rolling Window Algorithm*:  The time window is considered from the fraction
  of the time at which the request is made plus the time window length.  For
  example, if there are two messages sent at the 300th millisecond and the
  400th millisecondof a second, we'll count them as two messages from the 300th
  millisecond to the 300th millisecond of the next second.

### Actor Identification
* *By IP-address*:  We could throttle requests per IP, but the problem occurs
  when multiple users share a single public IP like in an internet cafe or
  smartphone users using the same gateway.
    * One bad user can cause throttling to other users.
    * Another issue is that if we cache based on IP addresses, and if we allow
      IPv6 addresses, there are a huge number of IPv6 addresses available for a
      hacker to use that could cause a server to run out of memory.
* *By User ID*:  We could require all users to authenticate themselves.  But
  then does that mean we have to rate limit the login API itself?  A would-be
  hacker can perform a DDoS against a user by entering the wrong credentials up
  to a limit.
* *By Hybrid Approach*: We could do both per-IP and per-user rate limiting as
  they both have weaknesses when implemented alone.  This will result in more
  cache entries with more details per entry requiring more memory and storage.

#### To look up later:
1. Wide-column databases like HBase.
1. Bigtable, which "combines multiple files into one block to store on the disk"
1. Map-Reduce (MR) jobs  (https://en.wikipedia.org/wiki/MapReduce)
