# Problem Statement and Approach
Given data with information regarding different features associated with network, the task is to recognize whether a connection is normal connection, or a type of attack on the network.

### Why is there a need to develop a robust adaptive approach to detect anomalies in the network?
The traditional methods that are commonly deployed to detect anomalies in network rely on predefined set of rules based on known attack patterns. The problem with these is that they fail at recognizing threats that previously have not been encountered. 

Cyber threats are evolving continuously, as in attackers find new ways to find bypass traditional security measures. Also, the network is forever growing, as in, new devices get added to the environment every now and then. Hence maintaining and monitoring theses devices becomes crucial as the network grows in size.

These are the fundamental reasons why there is a need for a system that is both adaptive and robust in detecting such threats in the network. Adaptive, because it has to continuously evolve by learning from the new data, and recognize new threats. Robust, because it has to cater to the need of threat detection in a network that is growing continuously.

### Approach
The suggestion is to take a Machine Learning based approach towards addressing the problem by building an ML model that can be fed with relevant features, and it classifies the connection as either normal or attack. This type of task in ML is called as classification task, more specifically, a binary classification task.

### Additional project info and dataset
Google Docs Link: [link](https://docs.google.com/document/d/1LCHFUQ0cULGp1zC7MrfVBTWWmnZ4L9zgYsULVCdOo5g/edit).


# Data Dictionary
### Basic connection features
- `duration`: Represents the length of time a specific network connection was active for.
- `protocoltype`: Represents the specific commumication protocol used in each connection.
- `service`: Represents the destination network service used in a connection.
- `flag`: Represents the status of a connection as either "Normal" or "Error".
- `srcbytes`: Represents the number of data bytes transferred from the source to the destination in a single connection.
- `dstbytes`: Represents the number of data bytes transferred from the destination to the source in a single connection.
- `land`: Indicates whether the source and destination IP addresses and port numbers are equal (1 if equal, 0 otherwise).
- `wrongfragment`: Represents the total number of wrong fragments received in a connection.
- `urgent`: Represents the number of urgent packets in this connection. Urgent packets are packets with the urgent bit activated.

### Content related features
- `hot`: Represents the number of "hot" indicators in the content, such as entering a system directory, creating programs, and executing programs.
- `numfailedlogins`: Represents the count of failed login attempts.
- `loggedin`: Indicates whether a successful login occurred in a connection (1 if successfully logged in, 0 otherwise).
- `numcompromised`: Represents the number of "compromised" conditions in a connection.
- `rootshell`: Indicates whether root shell access was obtained in a connection (1 if yes, 0 otherwise).
- `suattempted`: Indicates whether the "su root" command was attempted or used in a connection (1 if yes, 0 otherwise).
- `numroot`: Represents the count of root operations performed in a connection.
- `numfilecreations`: Represents the count of file creation operations in a connection.
- `numshell`: Represents the count of shell prompts in a connection.
- `numaccessfile`: Represents the count of operations on access control files in a connection.
- `numoutboundcmds`: Represents the count of outbound commands in an FTP session.
- `ishostlogin`: Indicates whether a login belongs to the host list i.e., root or admin (1 if yes, 0 otherwise).
- `isguestlogin`: Indicates whether a login belongs to the guest list (1 if yes, 0 otherwise).

### Time related traffic features
- `count`: Represents the number of connections to the same destination host as the current connection in the past 2 seconds.
- `srvcount`: Represents the number of connections to the same service as the current connection in the past 2 seconds.
- `serrorrate`: Represents the percentage of connections that have activated the flag s0, s1, s2, or s3, among the connections aggregated in `count`.
- `srvserrorrate`: Represents the percentage of connections that have activated the flag s0, s1, s2, or s3, among the connections aggregated in `srvcount`.
- `rerrorrate`: Represents the percentage of connections that have activated the flag REJ, among the connections aggregated in `count`.
- `srvserrorrate`: Represents the percentage connections that have activated the flag REJ, among the connections aggregated in `srvcount`.
- `samesrvrate`: Represents the percentage of connections that were to the same service, among the connections aggregated in `count`.
- `diffsrvrate`: Represents the percentage of connections that were to different services, among the connections aggregated in `count`.
- `srvdiffhostrate`: Represents the percentage of connections that were to different destination machines, among the connections aggregated in `srvcount`.

### Host based traffic features
- `dsthostcount`: Represents the number of connections having the same destination host IP address.
- `dsthostsrvcount`: Represents the number of connections having the same destination port number.
- `dsthostsamesrvrate`: Represents the percentage of connections that were to the same service, among the connections aggregated in `dsthostcount`.
- `dsthostdiffsrvrate`: Represents the percentage of connections that were to different services, among the connections aggregated in `dsthostcount`.
- `dsthostsamesrcportrate`: Represents the percentage connections that were to the same source port, among the connections aggregated in `dsthostsrvcount`.
- `dsthostsrvdiffhostrate`: Represents the percentage connections that were to different destination machines, among the connections aggregated in `dsthostsrvcount`.
- `dsthostserrorrate`: Represents the percentage connections that have activated the flag s0, s1, s2, or s3, among the connections aggregated in `dsthostcount`.
- `dsthostsrvserrorrate`: Represents the percentage connections that have activated the flag s0, s1, s2, or s3, among the connections aggregated in `dsthostsrvcount`.
- `dsthostrerrorrate`: Represents the percentage connections that have activated the flag REJ, among the connections aggregated in `dsthostcount`.
- `dsthostsrvrerrorrate`: Represents the percentage connections that have activated the flag REJ, among the connections aggregated in `dsthostsrvcount`.

### Others
- `attack`: Represents the specfic attack types.
- `lastflag`: Undefined.


# Data Cleaning
- Dataset used: [network_anomaly_dataset](datasets/network_anomaly_dataset.csv)
- Notebook used: [data_cleaning.ipynb](notebooks/data_cleaning.ipynb)

### Cleaning the `attack` column
The following are the unique elements in the `attack` column:
```
array(['normal', 'neptune', 'warezclient', 'ipsweep', 'portsweep',
       'teardrop', 'nmap', 'satan', 'smurf', 'pod', 'back',
       'guess_passwd', 'ftp_write', 'multihop', 'rootkit',
       'buffer_overflow', 'imap', 'warezmaster', 'phf', 'land',
       'loadmodule', 'spy', 'perl'], dtype=object)
```
The `attack` column represents the type of attack at a much granular level.

Attacks are majorly classified as follows,
1. Normal ("normal"): These connections are considered benign and do not pose a threat.
2. Denial of Services ("dos"): These attacks aim to disrupt the normal operation of a network or system by overwhelming it with excessive traffic or malicious requests. Examples include, "back", "land", "neptune", "pod", "smurf", and "teardrop".
3. User to Root ("u2r"): These attacks exploit vulnerabilities in a system to gain unauthorized root-level access. Examples include, "buffer_overflow", "loadmodule", "perl", and "rootkit".
4. Remote to Local ("r2l"): These attacks attempt to gain unauthorized access to a system from a remote location. Examples include, "ftp_write", "guess_passwd", "imap", "multihop", "phf", "spy", "warezclient", and "warezmaster".
5. Probe ("probe"): Probing attacks, which aim to gather information about a network or system. This category includes attacks like, "ipsweep", "nmap", and "satan" that scan networks for vulnerabilities and gather information.

A high level classification of these attack types can be created, and elements in the `attack` column can be assigned to one of the high level classes.

Considering all of the above, a new column, namely `attack_hlc`, has been created. Wherein each of the element in the `attack` column has been assigned to its respective high level class.

```
attackhlc = {
    "normal": "normal",
    "neptune": "dos",
    "warezclient": "r2l",
    "ipsweep": "probe",
    "portsweep": "probe",
    "teardrop": "dos",
    "nmap": "probe",
    "satan": "probe",
    "smurf": "dos",
    "pod": "dos",
    "back": "dos",
    "guess_passwd": "r2l",
    "ftp_write": "r2l",
    "multihop": "r2l",
    "rootkit": "u2r",
    "buffer_overflow": "u2r",
    "imap": "r2l",
    "warezmaster": "r2l",
    "phf": "r2l",
    "land": "dos",
    "loadmodule": "u2r",
    "spy": "r2l",
    "perl": "u2r"
}
```

### Cleaning the `suattempted` column
The column `suattempted`, according to the data dictionary (https://github.com/vidishsirdesai/network_anomaly_detection?tab=readme-ov-file#data-dictionary), is supposed to have only 2 values, i.e., 0 and 1. But, as seen in the output of cell number `14` in the jupyter notebook ([link](notebooks/data_cleaning.ipynb)), it has 3 values, i.e., 0, 1, and 2.

Assuming that the presence of 2 in the column is a typo, all the rows in the column `suattempted` where there was a 2 present is changed to 1.

### Removing the undefined and redundant columns
There is no description available for the feature `lastflag` in the data dictionary. Hence it has been dropped from the list of columns.

Also, the column `numoutboundcmds` has all zeros. This column can also be dropped from the list of columns.

### Final shape of the data after all the above changes made
```
(125973, 42)
```

### Dataset post data cleaning
The dataset with all the changes made during data cleaning is stored in: [link](datasets/network_anomaly_dataset_cleaned.csv).

The above cleaned dataset is used to create the Tableau dashboard.


# Analysis of Factors Associated with Intrusions in a Network using Tableau
- Dataset used: [link](datasets/network_anomaly_dataset_cleaned.csv).
- Tableau Viz: 


# EDA
- Dataset used: [network_anomaly_dataset.csv](datasets/network_anomaly_dataset.csv)
- Notebook used: [eda.ipynb](notebooks/eda.ipynb)

