# CloudChallenge

***The Architecture:***

**Your own technical design goals as decided before beginning implementation (which may just be a translation of this document into your own words.)**


*System goals:*

Fault-Tolerant: It can recover from component failures without performing incorrect actions. For example, if one of our machine fails, new machine can be created to replace the machine without any interruption for the system.

Highly Available: It can restore operations, permitting it to resume providing services even when some components have failed. 

Consistent: The system can coordinate actions by multiple components for concurrency.

Scalable: It can operate correctly when the system is scaled to large size. For example, the system can auto-scale when the number of users increases exponentially. Performance: The system can provide responsiveness in a timely manner. 

Secure: The system authenticates access to services.

*Programming goals:*

1. User-Friendly: The script commands should be similar to Docker Linux commands, so that old Docker users can intuitively issue commands via python scripts.
2. Extensible: The script should be modularized and extensible, so that users can easily customize the scripts or add new functions in future.
 
**Any failings to meet those goals within the time limit.**

The script meets the programming goals, but cannot meet the system goals. The distributed system like this requires much longer hours of work. 

**Considerations for future development:  What possible problems an
d failure cases are there?  How likely are they?**

1. Limited commands available: the current python scripts are too basic and covers only around 10% of Docker commands.
2. No deployment feature: it is not able to issue commands to deploy and manage the application in the container.
2. No maintenance feature: it is not able to do the health check of the container and replace the container in case of breakdown.
4. No scaling support: it is not able to issue commands to scale the container to 10 times or 100 times more instantly. 

**How would you solve those (succinctly), and how is this architecture set up for success in handling those cases?**

1. With our architecture, the additional features can be added to the scripts in independent modules.
2. To achieve scalability, we can communicate with Docker Swarm to turn a pool of Docker hosts into a single, virtual Docker host. We can also use multiple machines to handle the user requests concurrently. We can have a master node to receive the user requests, and dispatch these requests to different slave nodes. For example, a user may want to create 100 containers in multiple machines instantly, our master node receive this request, and instruct each one of the 10 slave nodes to create 10 containers concurrently. Our current script can be used in each slave node to execute different request, and we need to have another python load balancing script to dispatch request on the master node.

***Future Considerations/Inspiration:***

**We don’t expect you to complete these stretch goals, but perhaps consider them in your design & architecture.  Please be free to contribute to the list as well.**

**Collect live stats on resource utilization (which resources and how?)**

Statistics such as CPU, Memory and Disk utilization for should be collected. 
As a distributed system, the log script should be separated from other parts of the program. The logging script and statistics should be replicated in different machines to ensure the logging is working and data is being collected in case of machine failure.
As some existing Docker management tools already provide comprehensive statistics on Docker resource utilization, the easiest way is to use the tools such as Kubernetes.

**Constrain resources for containers**

We can have system manager working with container managers to constrain and allocate resources for containers. The system manager is concerned only with the allocation of resources between containers. The container manager is part of a container, and has more information about the requirements and communication patterns for container it manages. Thus, the container manager is in a better position to allocate resources to tasks once resources have been allocated to the container.


**Have multiple containers running simultaneously.  One should be producing files which another should continually consume.**

We can use publish-subscribe messaging system like Kafka. It is a pull based system, where the consumers/subscribers can express interest in specific classes of data and receive only those messages. The producer container can send data directly to the broker container, and the consumer container works by issuing "fetch" requests to the brokers leading the partitions it wants to consume. 


**Deploy somewhere to the cloud**

We can deploy it as a Docker manager application to AWS or Azure instances. In terms of scaling to multiple machines, we can have one machines as a master instance, and other machines as slave instances.


**Integration with Big Data frameworks**

Hadoop framework can be integrated with Docker. It will benefits from the simplicity of containers and the performance of bare-metal servers. Docker containers provide better I/O performance than traditional VMs. Therefore Hadoop clusters may run faster when deployed on Docker. Other technologies such as Kafka, Spark and Cassandra can also be deployed with Docker containers.




