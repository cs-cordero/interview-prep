# Grokking the System Design Interview

## Step-by-Step Guide to System Design Interviews

### Requirements clarifications
* Ask questions to get the exact scope of the problem we are solving.
* For example, let's say you were designing a Twitter-like service.  What
  questions would you ask?
    * Will users of our service be able to post tweets and follow other people?
    * Should we also design to create and display the user's timeline?
    * Will tweets contain photos and videos?
    * Are we fodusing on the backend only or are we developing the front-end too?
    * Will users be able to search tweets?
    * Do we need to display hot trending topics?
    * Will there be any push notification for new (or important) tweets?

### Back-of-the-envelope estimation
* It is always good to estimate the scale of the system we're going to design.
    * What scale is expected from the system (e.g., number of new tweets,
      number of tweet views, number of timeline generations per sec., etc.)?
    * How much storage will we need?  We will have different storage
      requirements if users can have photos and videos in their tweets.
    * What network bandwidth usage are we expecting?  This will be crucial in
      deciding how we will manage traffic and balance load between servers.

### System interface definition
* Define what APIs are expected from the system.  This will not only establish
  the exact contract expected form the system but will also ensure if we
  haven't gotten any requirements wrong.
    * For example:
        * postTweet(user_id, tweet_data, tweet_location, user_location, timestamp, ...)
        * generateTimeline(user_id, current_time, user_location, ...)
        * markTweetFavorite(user_id, tweet-id, timestamp, ...)

### Defining data model
* Defining the data model in the early part of the interview will clarify how
  data will flow between different components of the system.
* Later, it will guide for data partitioning and management.
* You need to identify the various entities in the system, how they will
  interact with each other, and the different aspects of data management like
  storage, transportation, encryption, etc.
    * For example, for the current Twitter example, here are the entities:
        * User: UserID, Name, Email, DoB, CreationData, LastLogin, etc.
        * Tweet: TweetID, Content, TweetLocation, NumberOfLikes, TimeStamp, etc.
        * UserFollowo: UserID1, UserID2
        * Favorite Tweets: UserID, TweetID, TimeStamp
* Which database system should we use?
    * NoSQL like Cassandra?
    * Or MySQL-like solution?
    * What kind of block storage should we use to store photos and videos?

### High-level design
* Draw a block diagram with 5-6 boxes representing the core components of our
  system.  WE should identify enough components that are needed to solve the
  actual problem, end-to-end.
* For example:
    * For Twitter, at a high level, we need multiple application servers to
      serve al the read/write requests with load balancers in front of them for
      traffic distributions.
    * If we assume that we will have more read traffic than write traffic, we
      can have separate servers for handling these scenarios.
    * On the backend we need an efficient database that can store all the
      tweets and can support a huge number of reads.
    * We also need a distributed file storage system for storing photos and videos.

### Detailed design
* Dig deeper into two or three major components; interviewer's feedback should
  always guide us to what parts of the system need further discussion.
* We should be able to present different approaches, their pros and cons, and
  explain why we will prefer one approach over the other.  There is no signle
  answer; the only important thing is to consider tradeoffs between different
  options while keeping the constraints in mind.
    * We will be storing a massive amount of data, how should we partition our
      data to distribute it to multiple databases?  Should we try to store all
      the data of a user on the same database?  What issue could it cause?
    * How will we handle hot users who tweet a lot or follow lots of people?
    * Since users' timeline will contain the most recent (and relevant) tweets,
      shoudl we try to store our data in such a way that is optimized for
      scanning the latest tweets?
    * How much and at which layer should we introduce cache to speed things up?
    * What components need better load balancing?

### Identifying and resolving bottlenecks
* Try to discuss as many bottlenecks as possible and different approaches to
  mitigate them.
    * Is there any single point of failure in our system?  What are we doing to
      mitigate it?
    * Do we have enough replicas of the data so that if we lose a few servers,
      we can still serve our users?
    * Similarly, do we have enough copies of different services running such
      that a few failures will not cause total system shutdown?
    * How are we monitoring the performance of the service? Do we get alerts
      whenever critical components fail or their performance degrades?


## Key Characteristics of Distributed Systems

The key characteristics of a distributed system are:
1. Scalability
1. Reliability
1. Availability
1. Efficiency
1. Maintainability/Manageability

### Scalability
The capability of a system, process, or network to grow and manage increased
demand.  If the proces can evolve to support the growing amount of work, it is
said to be scalable.

Generally, the performance of a system declines with the system size due to the
management or environment cost.

Some tasks in the system may not be distributed, either because of their
inherent atomic nature or because of some flaw in the system design.
    * A scalable architecture avoids this situation and attempts to balance the
      load on all the participating nodes evenly.

#### Horizontal vs Vertical scaling
Horizontal scaling means that you scale by adding more servers into your pool
of resources whereas Vertical scaling means that you scale by adding more power
(CPU, RAM, Storage, etc.) to an existing server.

It is often easier to scale horizontally by adding more machines to the
existing pool.  Vertical scaling is usually limted to the capacity of a single
server and scaling beyond that capactiy often involves downtime and comes with
an upper limit.
    * Cassandra and MongoDB provide and easy way to scale horizontally by
      adding more machines.
    * MySQL is a good example of vertical scaling because it gives an easy way
      to switch from smaller to bigger machines, with the cost of downtime.

### Reliability
Reliability is the probability a system will fail in a given period.  In simple
terms, a distributed system is considered reliable if it keeps delivering its
services even when oneor several of its hardware or components fail.

Reliability is achieved through redundancy.  Redundancy has a cost involved and
could be difficult to achieve if there is complex state that needs to be
replicated.  In the end the goal is to avoid any single point of failures in
the system.

### Availability
Availability is the time a system remains operational to perform its required
function in a specific period.  It is a simple measure of the percentage of
time that a system, service, or machine remains operational under normal
conditions.

If a system is reliable, it is available.  If it is available, it is not
necessarily reliabe.  It is possible to achieve a high availability even with
an unreliable product by minimizing repair time and ensuring that spares are
always available when they are needed.

### Efficiency
Efficiency is measured by its response time (latency) that denotes the delay to
obtain the first item, and the throughput (or bandwidth) which denotes the
number of items delivered in a given time unit (e.g., a second).

These two correspond to the following unit costs:
* Number of messages globally sent by the nodes of the system regardless of
  message size.
* Size of messages representing the volume of data exchanges.

Operations supported by distributed data structures can be characterized as a
function of one of these cost units.

### Maintainability (Manageability)
Represented as how easy the system is to operate and maintain.  This represents
the simplicity and speed with which a system can be repaired or maintained.  If
the time to fix a failed system increases, then availability will decrease.
* The ease of diagnosing and understanding problems when they occur.
* The ease of making updates or modifications
* How simple the system is to operate (i.e., does it routinely operate without
  failure or exceptions?)

## Load Balancing
Load balancing is a critical component to any distributed system.
* Helps to spread traffic across a cluster of servers and improve
  responsiveness and availibility of applications, websites, or databases.
* Keeps track of the status of all the resources while distributing requests.
  If a resource is not responding or has an elevated error rate, the LB will
  stop sending traffic to that resource.

LBs usually sit between the client and the server accepting incoming network
and application traffic and distributes traffic across mutliple backend
servers.
* A load balancer reduces individual server load and prevents any one
  application server form becoming a single point of failure, thus improving
  overall application availability and responsiveness.
* An LB can be placed at three places:
    * Between the users and the web servers
    * Between the web servers and an internal platform layer, like application
      servers or cache servers.
    * Between the internal platform layer and the database

### Pros of Load Balancing
* Users experience faster, uninterrupted service, since they won't have to wait
  for a single struggling server to finish its queue of tasks.
* Service providers experience less downtime and higher throughput. Even a full
  server failure won't affect the end user experience as the load balancer will
  simply route around it to a healthy server.
* Makes it easier for sysadmins to handle incoming requests while decreasing
  wait time for users.
* Smart load balancers provide benefits like predictive analytics that
  determine traffic bottlenecks before they happen.  Which means that you might
  get actionable insights, which are key to automation and can help drive
  business decisions.
* Sysadmins experience fewer failed or stressed components, since LBs makes it
  so that several devices perform a little bit of work

### Load Balancing Algorithms
Load balancers consider two factors before forwarding a request to a backend
server.  They will first ensure that the server they choose is actually
responding appropriately to requests and then use a pre-configured algorithm to
select from the set of healthy servers.

*Health Checks* - Load balancers should only forward traffic to healthy backend
servers. To monitor the health of a backend server, "health checks" regularly
attempt to connect to backend servers to ensure that servers are listening.
    * If a server fails a health check, it is automatically removed from the
      pool, and traffic will not be forwarded to it until it responds to the
      health checks again

#### Load balancing method
* Least connection method
    * Directs traffic to the server with the fewest active connections.  This
      is useful when there are a large number of persistent client connections
      which are unevenly distributed between the servers.
* Least response time method
    * Directs traffic to the server with the fewest active connections and the
      lowest average response time.
* Least bandwidth method
    * Directs traffic that is currently serving the least amount of traffic
      measured in megabits per second (Mbps).
* Round Robin method
    * Cycles through a list of servers and sends each new request to the next
      server.  When it reaches the end of the list, it starts over at the
      beginning.  It is most useful when the servers are of equal specification
      and there are not many persistent connections.
* Weighted Round Robin method
    * Designed to better handle servers with different processing capacities.
      Each server is assigned a weight (an integer value).  Servers with higher
      weights receive new connectiosn before those with less weights and
      servers with higher weights get more connections than those with less
      weights.
* IP Hash method
    * A hash of the IP address is calculated to redirect the request to a server.

### Redudant Load Balancers
* If you only have one LB, it becomes yet another single point of failure that
  you were hoping to remove.  To avoid this, you could just have multiple load
  balancers forming a cluster.
* Within the cluster, each LB monitors the health of the other, and since both
  of them are equally capable of serving traffic and failure detection, in the
  event the main load balancer fails, the second load balancer takes over.

#### Additional reading
1. [What is Load Balancing?](https://avinetworks.com/what-is-load-balancing/)
1. [Introduction to Architecting Systems for Scale](https://lethain.com/introduction-to-architecting-systems-for-scale/)
1. [Load Balancing](https://en.wikipedia.org/wiki/Load_balancing_(computing))


## Caching
Caching enables you to make vastly better use of the resources you already have
as well as making otherwise unattainable product requirements feasible.

Caches take advantage of the _locality of reference principle_: recently
requested data is likely to be requested again.

Caches are used in almost every layer of computing:  hardware, operating
systems, web browsers, web applications, and more.  A cache is like short-term
memory: it has a limited amount of space, but is typically faster than the
original data source and contains the most recently accessed items.

Caches can exist at all levels but are often found at the level nearest to the
front end where they are implemented to return data quickly without taxing
downstream levels.

### Application server cache
Placing a cache directly on a request layer node enables the local storage of
response data.  Each time a request is made to the service, the node will
quickly return local cached data if it exists.

If the request is not in the cache, then the requesting node will query the
data from disk.

The cache on one request layer node could also be located both in memory (which
is very fast) and on the node's local disk (faster than going to network
storage).

**What happens when you expand this to many nodes?** If the request layer is
expanded to multiple nodes, it is still quite possible to have each node host
its own cache.
* However, if your load balancer randomly istributes requests across the nodes,
  the same request will go to different nodes, thus increasing cache misses.
* Two choices for overcoming this hurdle: *global cache*s and *distributed
  cache*s.

### Content Distribution Network (CDN)
CDNs are a kind of cache that comes into play for sites serving large amounts
of static media.  In a typical CDN setup, a request will first ask the CDN for
a piece of static media; the CDN will serve that content if it has it locally
available. If it isn't available, the CDN will query the back-end servers for
the file, cache it locally, then serve it to the user.

If the system we're building isn't yet large enough to have its own CDN, we can
ease a future transition by serving the static media off a separate subdomain
(e.g., static.yourservice.com) using a lightweight HTTP server like Nginx, and
cut-over the DNS from your servers to a CDN later.

### Cache Invalidation
Caching requires maintenance for keeping cache coherent with the source of truth.

If the data is modified in the database, it should be invalidated in the cache;
if not, this can cause inconsistent application behavior.

Solving this probelm is known as cache invalidation; there are three main schemes that are used:
1. *Write-through cache*:  Data is written into the cache and the corresponding
   database at the same time.  The cached data allows for fast retrieval and
   since the same data gets written in the permanent sotrage, we will have
   complete data consistency between the cache and the storage.  Also this
   scheme ensures that nothing will get lost in case of a crsah, power failure,
   or other system disruptions.
1. *Write-around cache*:  This technique is similar to write-through cache but
   data is written directly to permanent storage, bypassing the cache.  This
   can reduce the cache being flooded with write operations that will not
   subsequently be re-read but has the disadvantage that a read request for
   recently written data will create a "cache miss" and must be read form
   slower back-end stoage and experience higher latency.
1. *Write-back cache*:  Data is written to the cache alone and completion is
   immediately confirmed to the client.  the write to the permanent storage is
   done after specified intervals or under certain conditions.  This results in
   low latency and high throughput for write-intensive applications.  This
   speed comes with the risk of data loss in case of a crash or other adverse
   event because the only copy of the written data is in the cache.

### Cache eviction policies
1. *FIFO*: Evicts the first block accessed without any regard to how often or how
   many times it was accessed before.
1. *LIFO*: Evicts the block accessed most recently first without any regard to
   how often or how many times it was accessed before.
1. *LRU*: Discards the least recently used items first
1. *MRU*: Discards the most recently used items first.
1. *LFU*: Counts how often an item is needed.  Discards the least frequently used
   data first.
1. *RR*: Randomly selects a candidate item and discards it to make space when
   necessary.


#### Additional reading
1. [Cache](https://en.wikipedia.org/wiki/Cache_(computing))
1. [Introduction to Architecting Systems for Scale](https://lethain.com/introduction-to-architecting-systems-for-scale/)


## Data Partitioning
Data partitioning is a technique to break up a big database into many smaller
parts.  It is the process of slitting up a DB/table across multiple machines to
improve the manageability, performance, availability, and load balancing of an
application.  The justification for data partitioning is that, after a certain
scale point, it is cheaper and more feasible to scale horizontally by adding
more machines than to grow it vertically by adding beefier servers.

### Partitioning Methods
1. Horizontal partitioning (Sharding)
    * We put different rows into different tables.
    * For example, if we are storing different places in a table, we can decide
      that locations with ZIP codes less than 10000 are stored in one table and
      places with ZIP codes greater than 10000 are stored in a separate table.
      This is also called a range based partitioning as we are storing
      different ranges of data in separate tables.
    * This is also called *Data Sharding*.
    * The problem with this approach is that if the value whose range is used
      for partitioning isn't chosen carefully, then the partitioning scheme
      will lead to unbalanced servers.
1. Vertical partitioning
    * We put different tables on different servers.
    * For example, if we were building Instagram, we can decide to place user
      profile information on one DB server, friend lists on another and photos
      on a third server.
    * Vertical partitioning is straightforward to implement and has low impact
      on the application.
    * The problem with this approach is that if our application experiences
      additional growth, then it may be necessary to further partition a
      feature specific DB across various servers.
1. Directory-based parititioning
    * A loosely coupled approach is to create a lookup service which knows your
      current partitioning scheme and abstracts it away from the DB access
      code.  So, to find out where a particular data entity resides, we query
      the directory server that holds the mapping between each tuple key to its
      DB server.
    * This approach means we can perform tasks like adding servers to the DB
      pool or changing our partitioning scheme without having an impact on the
      application.

### Partitioning Criteria
1. *Key or hash-based partitioning*
    * Apply a hash function to some key attribute of the entity we are storing;
      that yields the partition number.  For example if we have 100 DB servers
      and our ID is a numeric value that gets incremented by one each time a
      new record is inserted.
    * This approach should ensure a uniform allocation of data among servers.
    * The problem with this approach is that it effectively fixes the total
      number of DB servers, since adding new servers means changing the hash
      function, which would require redistribution of data and downtime for the
      service.  You can get around this by using *consistent hashing*.
1. *List partitioning*
    * Each partition is assigned a list of values so whenever we want to insert
      a new record, we will see which partition contains our key and then store
      it there.
1. *Round-robin partitioning*
    * With `N` paritions, the `i` tuple is assigned to partition `i % n`.
1. *Composite paritioning*
    * We combine any of the above partitioning schemes to devise a new scheme.
      For example, first applying a list partitioning scheme and then hash
      based partitioning.
    * Consistent hashing could be considered a composite of hash and list
      partitioning where the hash reduces the key space to a size that can be
      used.

### Common problems of data partitioning
Partitioned databases have extra constraints on the different operations that
can be performed.

Most of these constraints are due to the fact that operations across multiple
tables or rows in teh same table will no longer run on the same server.

1. Joins and denormalization
    * Performing joins on a database which is running on one server is
      straightforward, but once a database is partitioned and spread across
      multiple machines, it is often not feasible to perform joins that span
      database partitions.
    * Such joins will not be performant efficient since data has to be compiled
      from multiple servers.
    * A common workaround for this problem is to denormalize the database so
      that queries that previously required joins can be performed from a
      single table.
        * Of course, by doing so, we open ourselves up to data inconsistency.

1. Referential integrity
    * Performing a cross-partition query on a partitioned database is not
      feasible.  Similarly, trying to enforce data integrity constaints such as
      foreign keys on a partitioned database can be extremely difficult.
    * Most RDBMS do not support foreign key constraints across databases on
      different database servers.
    * Applications that require referential integrity on partitioned databases
      often have to enforce it in application code.
    * Often in such cases, applications have to run regular SQL jobs to clean
      up dangling references.

1. Rebalancing
    * We may need to change our partitioning scheme because the data
      distribution is not uniform, e.g., there are a lot of places for a
      particular ZIP code that cannot fit into one database partition.
    * There is a lot of load on a partition, e.g., there are too many requests
      being handled by the DB partition dedicated to user photos.
    * In such cases, either we have to create more DB parittions, or have to
      rebalance existing partitions, which means the partitioning scheme
      changed and all existing data moved to new locations.
    * Rebalancing without downtime is extremely difficult.  Using a scheme like
      directory based partitioning does make it more palatable, but at the cost
      of increasing the complexity of the system and creating a new single
      point of failure (the lookup service/database)


## Indexes
One of the first things you should turn to when the performance of a database
is lacking is database indexing.

The goal of creating an index on a particular table in a database is to make it
faster to search through the table and to find the row or rows that we want.

Indexes can be created using one or more columns of a database table, providing
the basis for both rapid random lookups and efficient access of ordered
records.

### What is an index?
An index is a data structure that can be perceived as a table of contents that
points us to the location where actual data lives.  So when we create an index
on a column of a table, we store that column and a pointer to the whole row in
the index.
* When we create an index on a column of a table, we store that column and a
  pointer to the whole row in the index.
* The trick with indexes is that we must carefully consider how users will
  access the data.
* If the data sets are many TB in size, but have very small payloads (e.g., 1
  KB), indexes are a necessity.
* It is also likely that once you reach a certain size of DB, the dataset is
  spread over several physical devices.  This means we need some way to find
  the correct physical location of the desired data.  Indexes are the best way
  to do this.

### Indexes decrease write performance
Indexes dramatically speed up data retrieval but could slow down data insertion
& updates if the index itself is large.

Every time an insert, update, or delete occurs we have to write to the DB but
also need to update the index.  This will decrease write performance.

Adding unnecessary indexes on tables should be avoided and indexes that are no
longer being used should be removed.

#### Additional reading
1. [Database index](https://en.wikipedia.org/wiki/Database_index)

## Proxies
A proxy server is an intermediate server between the client and the back-end
server.

Clients connect to proxy servers to make a request for a service like a web
page, file, connection, etc.  In short, a _proxy server_ is a piece of software
or hardware that acts as an intermediary for requests from clients seeking
resources from other servers.

Proxies are used to:
1. Filter requests
1. Log requests
1. Transform requests (by adding/removing headers, encrypting/decrypting, or
   compressing a resource)
1. Proxy server cache can serve a lot of requests.

### Proxy Server Types
1. Open Proxy
    * A proxy server that is accessible by any Internet user.  Generally a
      proxy server only allows users within a network group (i.e., a closed
      proxy) to store and forward Internet services such as DNS or web pages to
      reduce and control the bandwidth used by the group.
    * With an open proxy, any user on the Internet is able to use the server as
      a forwarding service.
    * Anonymous Proxy - this proxy reveals its identity as a server but does
      not disclose the initial IP address.  Though this proxy server can be
      discovered easily it can be beneficial for some users as it hides their
      IP address.
    * Transparent Proxy - this proxy again identifies itself and with the
      support of HTTP headers, the first IP address can be viewed.  The main
      benefit of using this sort of server is its ability to cache the
      websites.
1. Reverse Proxy
    * A reverse proxy retrieves resources on behalf of a client from one or
      more servers.  These resources are then returned to the client, appearing
      as if they originated from the proxy server itself.


#### Additional reading
1. [Open proxy](https://en.wikipedia.org/wiki/Open_proxy)
1. [Reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy)

## Redundancy and Replication
*Redundancy* is the duplication of critical components or functions of a
system with the intention of increasing the reliability of the system, usually
in the form of a backup or fail-safe, or to improve actual system performance.

When one instance of a service running in production fails, the system can
failover to the other one.

*Replication* means sharing information to ensure consistency between redundant
resources, such as software or hardware components, to improve reliability,
fault tolerance or accessibility.

Replication usually occurs in database management systems (DBMS) with a
master-slave relationship between the original and the copies.  The master gets
all the updates, which then ripple through to the slaves.

## SQL vs. NoSQL
There are two main types of solutions for databases:  SQL and NoSQL, aka
relational databases and non-relational databases.

Relational databases are structured and have predefined schemas like phone
books that store phone numbers and addresses.  Non-relational databases are
unstructured, distributed, and have a dynamic schema like file folders that
hold everything from a person's address and phone number to their Facebook
'likes' and online shopping preferences.

### SQL
Relational databases store data in rows and columns.  Each row contains all the
information about one entity and each column contains all the separate data
points.

Popular relational databases: MySQL, Oracle, MS SQL Server, SQLite, Postgres,
MariaDB.

### NoSQL
The following are the most common types of NoSQL:
* Key-Value Stores
    * Data is stored in an array of key-value pairs.  The 'key' is an attribute
      name which is linked to a 'value'.  Well-known key-value stores include
      Redis, Voldemort, and Dynamo.
* Document Databases
    * Data is stored in documents instead of rows and columns in a table.
      These documents are grouped together in collections.  Each document can
      have an entirely different structure.  Includes CouchDB and MongoDB.
* Wide-Column Databases
    * Instead of tables, in columnar databases we have column families, which
      are containers for rows.  Unlike relational databases, we dont' need to
      know all the columns up front and each row doesn't have to have the same
      number of columns.  Columnar databases are best suited for analyzing
      large datasets.  Includes Cassandra and HBase.
* Graph Databases
    * Data is stored with its relations represented in a graph.  Data is saved
      in graph structures with nodes (entities), properties (information about
      the entities), and lines (connections between the entities).  Includes
      Neo4J and InfiniteGraph.

### Differences
* Storage
    * SQL stores data in tables where each row represents an entity and each
      column represents a data point about that entity.
    * NoSQL databases have different data storage models. The main ones are
      key-value, document, graph, and columnar.
* Schema
    * SQL records conform to a fixed schema, meaning the columns must be
      decided and chosen before data entry and each row must have data for each
      column.  The schema can be altered later, but it involves modifying the
      whole database and going offline.
    * NoSQL schemas are dynamic.  Columns can be added on the fly and each
      'row' (or equivalent) doesn't have to contain data for each 'column'.
* Querying
    * SQL databases use SQL for defining and manipulating the data, which is
      very powerful.
    * NoSQL database queries are focused on a collection of documents.
      Sometimes it is called UnQL (Unstructured Query Lanage).  Different
      databases have different syntax.
* Scalability
    * SQL databases are vertically scalable.  While it is possible to scale it
      horizontally across multiple servers, it is challenging and
      time-consuming.
    * NoSQL databases are horizontally scalable.  Any cheap commodity hardware
      or cloud instance can host NoSQL databases, thus making it a lot more
      cost effective than vertical scaling.
* Reliability or ACID Compliancy
    * Most, nearly all, SQL databases are ACID compliant, so the data is
      reliable and safe and can perform transactions.
    * Most NoSQL solutions sacrifice ACID compliance for performance and
      scalability.

### Pros for SQL databases
1. We need to ensure ACID compliance.  Usually for e-commerce and financial
   applications, an ACID-compliant database remains the preferred option.
1. Your data is structured and relatively unchanging.

### Pros for NoSQL databases
1. You're storing large volumes of data that have little to no structure.
1. You're interested in making hte most of cloud computing and storage, which
   involves having data that can be easily spread across multiple servers to
   scale up.
1. You need rapid development.  NoSQL databases don't need to be prepped ahead
   of time.

#### Additional reading
1. [HackerNews: NoSQL...](https://news.ycombinator.com/item?id=12529310)

## CAP Theorem
It is impossible for a distributed software system to simulataneously provide
more than two out of three of the following CAP guarantees:  _Consistency_,
_Availability_, and _Partition tolerance_.

When we design a distributed system, trading off among CAP is almost the first
thing we want to consider.

* *Consistency*:  All nodes see the same data at the same time.  Consistency is
  achieved by updating several nodes before allowing further reads.
* *Availability*:  Every requests gets a response on success/failure.
  Availability is acheived by replicating the data across different servers.
* *Partition tolerance*:  The system continues to work despite message loss or
  partial failure.  A system that is partition-tolerant can sustain any amount
  of network failure that doesn't result in a failure of the entire network.
  Data is sufficiently replicated across combinations of nodes and networks to
  keep the system up through intermittent outages.

## Consistent Hashing
Distribued Hash Table (DHT) is a fundamental component used in distributed scalable systems.  Hash Tables need a key, a value, and a hash function where hash function maps the key to a location where the value is stored.

`index = hash_function(key)`

Given 'n' cache servers, an intuitive hash function would be `key % n`,
however,  this has two major drawbacks:
1. It is NOT horizontally scalable.  Whenever a new cache host is added to the
   system, all existing mappings are broken.  It will be a pain point in
   maintenance if the caching system contains a lot of data.  Practically, it
   becomes difficult to schedule a downtime to update all caching mappings.
1. It may NOT be load balanced, especially for non-uniformly distributed data.
   In practice, it can be easily assumed that the data will not be distributed
   uniformly.  For the caching system, it translates into some caches becoming
   hot and saturated while the others idle and are almost empty.

### What is Consistent Hashing?
Consistent hashing is a very useful strategy for distributed caching system and
DHTs.  It allows us to distribute data across a cluster in such a way that will
minimize reorganiziation when nodes are added or removed.  Hence, the caching
system will be easier to scale up or down.

When a hash table is resized, only `k/n` keys need to be remapepd where `k` is
the total number of keys and `n` is the total number of servers.  Recall that
in a caching system, using the `mod` as a function, all the keys need to be
remapped.

In consistent hashing, objects are mapped to the same host if possible.  When a
host is removed the system, the objects on that host are shared by other hosts;
when a new host is added  it takes its share from a few hosts without touching
other's shares.

### How it works
1. Given a list of cache servers, hash them to integers in the range.
1. To map a key to a server,
    1. Hash it to a single integer.
    1. Move clockwise on the ring until finding the first cache it encounters.
    1. That cache is the one that contains the key.

## Long-Polling vs WebSockets vs Server-Sent Events
These are popular communcatino protocols between a client like a web browser
and a web server.

### Ajax Polling
Polling is a standard technique used by the vast majority of AJAX applications.
The basic idea is that the client repeated polls (or requests) a server for
data.  If no data is available, an empty response is returned.
1. The client opens a connection and requests data from the server using
   regular HTTP.
1. The requested webpage sends requests to the server at regular intervals
   (e.g., 0.5 seconds).
1. The server calculates the response and sends it back, just like regular HTTP
   traffic.
1. The client repeats the above three steps periodically to get updates from
   the server.

The problem with polling is that the client has to keep asking the server for
any new data.  As a result, a lot of responses are empty, creating HTTP
overhead.

### HTTP Long-Polling
This is a variation of the traditional polling technique that allows the server
to push information to a client when the data is available.  With long-polling,
the client requests information from the server in the same way as in normal
polling, but with the expectation that the server may not respond immediately.

This technique is also known as the "hanging GET".

* If the server does not have any data available for the client, instead of
  sending an empty response the server holds the request and waits until some
  data does become available.
* Once the data becomes available, a full response is sent to the client.  The
  client then immediately re-requests information from the server so that the
  server will almost always have an available waiting request that it can use
  to deliver data in response to an event.

1. Client makes initial request using HTTP
1. Server delays response until update is available or timeout has occurred.
1. When an update is available, server sends full response to client.
1. Client typically sends a new long-poll request, either immediately or after
   a pause.
1. Each long-poll request has a timeout, the client has to reconnect
   periodically after the connection is closed due to timeouts.

### WebSockets
WebSocket provides _full duplex_ communication channels over a single TCP
connection.  It provides a persistent connection between client and server that
both parties can use to start sending data at any time.

To establish a WS connection, it must occur through a WebSocket handshake.  If
the handshake succeeds then either side can send the other data at any time.

### Server-Sent Events (SSEs)
Client establishes a persistent and long-term connection with the server.  The
server uses this connection to send data to a client.  If the client wants to
send data to the server, it would require the use of another
technology/protocol to do so.

1. Client requests data from a server using HTTP.
1. The requested webpage opens a connection to the server.
1. The server sends the data to the client whenever there is new information
   available.

#### Additional reading
1. [Duplex](https://en.wikipedia.org/wiki/Duplex_(telecommunications)#Full_duplex)
