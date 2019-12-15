# System Design Interview Approach

## Step 1: Gather requirements and goals of the system
**You should always clarify requirements at the beginning of the interview.  Be
sure to ask questions to find the exact scope of the system that the
interviewer has in mind.**

Identify the following:
1. Functional requirements
    * Given X, the system should do Y
    * When X happens, the system should do Y
    * Users should be able to do X
    * After some time, the records do X (or X occurs to records that fit Y criteria)
1. Non-functional requirements
    * These examples are pretty business-logic-specific, but can be geared
      towards "should" language.
    * The system should be highly available/etc.
    * The system should not be guessable.
1. Extended requirements
    * Analytics/Telemetry
    * Should we expose an external REST API?
1. Out of scope requirements
    * Things that the interviewer definitively doesn't care to talk about

## Step 2:  Make estimates for capacity and constraints
**Discuss with the interviewer the capacity and the constraints of the problem.
This might be revealed to you, or you might have to make some estimates of your
own.**

Instructions:
1. Start with a ratio of reads to writes.  In the TinyURL example of the class,
   we just arbitrarily assumed a 100:1 ratio between read and write.
1. Then assume a number of writes and/or reads in a time frame (like a month is
   OK to start with), which will inform the rest of the discussion.
1. Boil down to estimates by _second_.  This will inform how performant we need
   this system to be.
1. For traffic estimates and for memory/caching estimates, don't forget the
   **80-20 rule**, which states that 80% of outcomes (or outputs) result in 20%
   of all causes (or inputs) for a given event.
    * 20% of users cause 80% of all traffic
    * 20% of generated tinyURLs cause 80% of all traffic.

Identify the following:
1. Traffic estimates
    * For example, assuming 500M writes per month and a 100:1 read/write ratio,
      we can expect 50B reads during the same period:  \\(100 * 500M = 50B\\)
    * Breaking down the assumed 500M writes per month down to seconds, we can
      assume around 200 writes per second: \\(\frac{500\ million}{30\ days *
      24\ hours * 3600\ seconds} = ~200\ writes/second\\)
    * Using the read/write ratio, we can then estimate the number of reads per
      second:  \\(100 * 200\ writes/second = 20K\ reads/second\\)
1. Storage estimates
    * For example, assuming we store every write for a minimum of 5 years, we
      can expect to store 30B objects on average:  \\(500M\ writes\ per\ month *
      12 months * 5 years = 30B\\)
    * Assume each object has 500 bytes (which is just a ballpark), we will
      therefore need 15TB of total storage:  \\(30B * 500\ bytes = 15TB\\)
1. Bandwidth estimates
    * Since we are assuming 500 bytes per object, on writes, we estimate
      100KB/second:  \\(200\ writes/second * 500\ bytes = 100\ KB/s\\)
    * For read requests, we assume 20K reads per second, so total outgoing data
      for the system would be 10MB per second:  \\(20K * 500\ bytes = ~10
      MB/s\\)
1. Memory estimates
    * Is memory required for the system itself?  For the TinyURL example, no -
      other than the DB, the application is mostly stateless.
    * One way to introduce memory into the application is through a cache, and
      you'd do this to imrpove performance.
    * If you wanted to cache some of the hot URLs that are frequently being
      accessed, you can follow the 80-20 rule, which states that 20% of
      URLs uses up 80% of the total traffic.  You'd want to cache these 20%.
    * Since we have 20K reads per second, on a daily basis, this becomes 1.7B
      per day:  \\(20K * 3600\ seconds * 24\ hours = ~1.7B\\)
    * To cache 20% of the daily requests, we would need 170GB of memory:
      \\(0.2 * 1.7B * 500\ bytes = ~170GB\\)
1. High level estimates
    * Once you've completed the estimation process for the above, you may want
      to pull them aside for easy reference in the future.


## Step 3:  Declare the system APIs
**Once we've finalized our requirements it's always a good idea to define the
system APIs.  This should explicitly state what is expected from the system.**

We can have SOAP or REST APIs to expose the functionality of the service.

You basically want to declare the function signatures of the service interface.

If you're exposing a public interface, you may want to comment on how to detect
and prevent abuse.  In the TinyURL example, the solution provided was to limit
a certain number of URL creations and redirections per some time period per API
key.

## Step 4:  Design the database
**Defining the DB schema in the early stages of the interview would help to
understand the data flow among various components and later would guide towards
data partitioning**

Discuss the tables you'd need and the relationships between them.

Discuss what kind of database should you use?  SQL vs NoSQL?

## Step 5:  Basic System Design and Algorithm
This the meat and bones part where you illustrate how the system design works
at a high level.  For the TinyURL question the actual mechanics for how you hash
original URLs to their tiny URLs is really important so you'd be expected to
figure that out.

You can consider setting up a service that handles the creation of tiny URLs
offline for you.  Similarly if there's a way to take some complex calculation
offline, definitely consider it and bring it up.

Questions to be wary about:
1. Can concurrency cause problems?
1. Do you have any single points of failure?  How do you solve it?
1. Can you use caching?  Where? How would it work?
1. How does one round-trip request go through your system?
1. Should we impose size limits on any custom requests?

## Step 6:  Data Partitioning and Replication
What partitioning scheme would you use to divide and store your data into
different DB servers?

1. Non-hash-based partitioning (Range-based partitioning)
    * We could store items based on specific attributes or properties, like the
      first value of the hash key of the TinyURL.
    * Be wary as this could potentially cause unbalanced partitions.
1. Hash-based partitioning
    * Consistent Hashing can help solve overloaded partitions.

## Step 7:  Cache and Load Balancing
If we decided to go with a caching solution, how should we go about it?

Options:
1. Memcached

Questions to be wary about:
1.  How much cache memory should we have?  Look above in the estimates section
    for how we went about it.
1.  What cache eviction policy would best fit our needs?
1.  How can each replica be updated?  It could be updated as part of a read
    from the DB upon a cache miss, for example.

We can add a load balancing layer at three places in the system:
1. Between clients and application servers
1. Between application servers and database servers
1. Between application servers and cache servers

## Step 8:  Purging or DB cleanup, Telemetry, Security, etc.
What do we do with really really old data?

Some options:
1. Lazy deletions
    * Only delete if they're accessed again
1. Separate service
    * Run a job or service that periodically removes expired/dead data.  It
      should be lightweight and should run only when user traffic is expected
      to be low.
1. Self-deletion
    * The data itself could keep track of an expiration date and which would
      invalidate itself after the time has passed.
1. In the case in the TinyURL example, where the inventory of hash keys are
   technically finite, you may want to think about reusing them.
1. Should we delete at all?
    * Perhaps the storage really is so cheap that deletion is more trouble than
      it's worth.
    * Perhaps we should delete data that might not be old as per some
      pre-defined definition, but it hasn't been used in a very long time.

Statistics that would be worth keeping track of:
1. Country of the visitor
1. Date and time of access
1. Web page that refers the click
1. Browser/platform used where the page was accessed

Should certain sections of the service be made private?  How do we keep track
of users that can and cannot access a resource?
* We may need to augment our schema in order to keep track of this kind of
  mapping, like a new table that maps userIds to the resources they can access.
