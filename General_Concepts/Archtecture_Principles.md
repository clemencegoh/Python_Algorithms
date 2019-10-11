# Monolithic vs Microservices Architechture

## Monolithic
- Traditional method for web applications

| Advantages | Disadvantages |
| --- | --- |
| Simple to Develop, Test, Deploy, Scale | As development grows, associated code base grows too, overloads development environment each time it loads application, reducing developer productivity |
|  | Change of tech stack is difficult |
|  | Refactoring becomes difficult, unpredictable |
|  | If single application fails, entire application goes down | 
|  | Horizontal scaling only, additional servers required with same amount of underlying resources | 
|  | Due to integrated nature, developers are unable to work independently and are dependent on others |


## Microservices
- Improve fault isolation: 
	- Larger applications can remain mostly unaffected by the failure of a single module.
- Eliminate vendor or technology lock-in: 
	- Microservices provide the flexibility to try out a new technology stack on an individual service as needed. There won’t be as many dependency concerns and rolling back changes becomes much easier. With less code in play, there is more flexibility.
- Ease of Understanding: 
	- With added simplicity, developers can better understand the functionality of a service.

- Deployed with containers (Docker) and virtual machines

| Advantage | Disadvantage | 
| --- | --- |
| Improve fault isolation: Larger applications can remain mostly unaffected by the failure of a single module. | Testing could be cumbersome |
| Eliminate vendor or technology lock-in: Microservices provide the flexibility to try out a new technology stack on an individual service as needed. There won’t be as many dependency concerns and rolling back changes becomes much easier. With less code in play, there is more flexibility. | |
| Ease of Understanding: With added simplicity, developers can better understand the functionality of a service.| Increased complexity in communication between microservices |
|  | Multiple databases and transaction management can be painful |
|  | Deploying microservices could be complex, require coordination between multiple services | 

## Containers and VMs
| Containers | Virtual Machines |
| --- | --- |
| Only contains environment, shares OS | Runs its own OS |
| Fast start, shares OS with other containers, reduce management overhead | Takes longer to start, high overhead due to different OSes |

- Recommended to run Container on VM for security reasons
- Hacker will be able to break out of container into VM and not the entire network
