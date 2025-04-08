**Task 1**
## Local Area Network (LAN) Topologies
### Star Topology
The main premise of a star topology is that devices are individually connected via a central networking device such as a switch or hub. This topology is the most commonly found today because of its reliability and scalability - despite the cost.
Any information sent to a device in this topology is sent via the central device to which it connects. Let's explore some of these advantages and disadvantages of this topology below:
Because more cabling and the purchase of dedicated networking equipment is required for this topology, it is more expensive than any of the other topologies. However, despite the added cost, this does provide some significant advantages. For example, this topology is much more scalable in nature, which means that it is very easy to add more devices as the demand for the network increases.
Unfortunately, the more the network scales, the more maintenance is required to keep the network functional. This increased dependence on maintenance can also make troubleshooting faults much harder. Furthermore, the star topology is still prone to failure - albeit reduced. For example, if the centralised hardware that connects devices fails, these devices will no longer be able to send or receive data. Thankfully, these centralised hardware devices are often robust.

![Output](TryHackMe/Pre_Security_Path/Images/13.jpg)
### Bus Topology
This type of connection relies upon a single connection which is known as a backbone cable. This type of topology is similar to the leaf off of a tree in the sense that devices (leaves) stem from where the branches are on this cable.
Because all data destined for each device travels along the same cable, it is very quickly prone to becoming slow and bottlenecked if devices within the topology are simultaneously requesting data. This bottleneck also results in very difficult troubleshooting because it quickly becomes difficult to identify which device is experiencing issues with data all travelling along the same route.
However, with this said, bus topologies are one of the easier and more cost-efficient topologies to set up because of their expenses, such as cabling or dedicated networking equipment used to connect these devices.
Lastly, another disadvantage of the bus topology is that there is little redundancy in place in case of failures. This disadvantage is because there is a single point of failure along the backbone cable. If this cable were to break, devices can no longer receive or transmit data along the bus.

![Output](TryHackMe/Pre_Security_Path/Images/14.jpg)
### Ring Topology
The ring topology (also known as token topology) boasts some similarities. Devices such as computers are connected directly to each other to form a loop, meaning that there is little cabling required and less dependence on dedicated hardware such as within a star topology.
A ring topology works by sending data across the loop until it reaches the destined device, using other devices along the loop to forward the data. Interestingly, a device will only send received data from another device in this topology if it does not have any to send itself. If the device happens to have data to send, it will send its own data first before sending data from another device.
Because there is only one direction for data to travel across this topology, it is fairly easy to troubleshoot any faults that arise. However, this is a double-edged sword because it isn't an efficient way of data travelling across a network, as it may have to visit many multiple devices first before reaching the intended device.
Lastly, ring topologies are less prone to bottlenecks, such as within a bus topology, as large amounts of traffic are not travelling across the network at any one time. The design of this topology does, however, mean that a fault such as cut cable, or broken device will result in the entire networking breaking.

![Output](TryHackMe/Pre_Security_Path/Images/15.jpg)

- **Switch**: A switch is a networking device that connects multiple devices within the same network (usually a Local Area Network, or LAN). It uses MAC addresses to forward data to the correct device, ensuring efficient communication between devices in the network.
    
- **Router**: A router is a device that connects different networks (such as connecting a home network to the internet). It routes data between devices on different networks by using IP addresses and directs traffic, ensuring it reaches its correct destination across the network or internet.

Here's some quick definitions before I start giving answers.
What does LAN stand for?
```
Local Area Network
```
What is the verb given to the job that Routers perform?
```
Routing
```
What device is used to centrally connect multiple devices on the local network and transmit data to the correct location?
```
Switch
```
What topology is cost-efficient to set up?
```
Bus Topology
```
What topology is expensive to set up and maintain?
```
Star Topology
```
Complete the interactive lab attached to this task. What is the flag given at the end?
```
THM{TOPOLOGY_FLAWS}
```
I'm uh too lazy to do the lab so here's the flag

**Task 2**
Quick guide

| Type            | Purpose                                                                                                                                        | Explanation                                                                                                                                                                                                                                          | Example       |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| Network Address | This address identifies the start of the actual network and is used to identify a network's existence.                                         | For example, a device with the IP address of 192.168.1.100 will be on the network identified by 192.168.1.0\|                                                                                                                                        | 192.168.1.0   |
| Host Address    | An IP address here is used to identify a device on the subnet                                                                                  | For example, a device will have the network address of 192.168.1.1                                                                                                                                                                                   | 192.168.1.100 |
| Default Gateway | The default gateway address is a special address assigned to a device on the network that is capable of sending information to another network | Any data that needs to go to a device that isn't on the same network (i.e. isn't on 192.168.1.0) will be sent to this device. These devices can use any host address but usually use either the first or last host address in a network (.1 or .254) | 192.168.1.254 |


Subnetting provides a range of benefits, including:
- Efficiency
- Security
- Full control

What is the technical term for dividing a network up into smaller pieces?
```
Subnetting
```
How many **bits** are in a subnet mask?
```
32
```
What is the range of a section (octet) of a subnet mask?
```
0-255
```
What address is used to identify the start of a network?
```
Network Address
```
What address is used to identify devices within a network?
```
Host Address
```
What is the name used to identify the device responsible for sending data to another network?
```
Default Gateway
```
**Task 3**
How does ARP Work?
Each device within a network has a ledger to store information on, which is called a cache. In the context of the ARP protocol, this cache stores the identifiers of other devices on the network.
In order to map these two identifiers together (IP address and MAC address), the ARP protocol sends two types of messages:

1. **ARP Request**
2. **ARP Reply**

When an **ARP request** is sent, a message is broadcasted on the network to other devices asking, "What is the mac address that owns this IP address?" When the other devices receive that message, they will only respond if they own that IP address and will send an **ARP reply** with its MAC address. The requesting device can now remember this mapping and store it in its **ARP cache** for future use.

![Output](TryHackMe/Pre_Security_Path/Images/16.jpg)
What does ARP stand for?
```
Address Resolution Protocol
```
What category of ARP Packet asks a device whether or not it has a specific IP address?
```
Request
```
What address is used as a physical identifier for a device on a network?
```
MAC Address
```
What address is used as a logical identifier for a device on a network?
```
IP Address
```
**Task 4**
IP addresses can be assigned either manually, by entering them physically into a device, or automatically and most commonly by using a **DHCP** (**D**ynamic **H**ost **C**onfiguration **P**rotocol) server. When a device connects to a network, if it has not already been manually assigned an IP address, it sends out a request (DHCP Discover) to see if any DHCP servers are on the network. The DHCP server then replies back with an IP address the device could use (DHCP Offer). The device then sends a reply confirming it wants the offered IP Address (DHCP Request), and then lastly, the DHCP server sends a reply acknowledging this has been completed, and the device can start using the IP Address (DHCP ACK).

![Output](TryHackMe/Pre_Security_Path/Images/17.jpg)

What type of DHCP packet is used by a device to **retrieve an IP address?**
```
DHCP Discover
```
What type of DHCP packet does a device **send once it has been** **offered an IP address** by the DHCP server?
```
DHCP Request
```
Finally, **what is the last** DHCP packet that is sent to a device from a DHCP server?
```
DHCP ACK
```