# check_IP_connectivity
Python script to check if a server's IP connectivity is working.

## How to use it ?

You must first create a .txt file and insert the different sites you want to test (one per line).

When running it, you have to give a parameter which is the name of the file name.

## Example
I'm going to create a "servers.txt" file that contains the different sites I want to test.
1. *ephec.be*
2. *ecam.be*
3. *pountokdo.com*
4. *google.be*
5. *helha.be*

Then I will run my script and provide the name of this file as a parameter.

> \>py main.py servers.txt
- *ephec.be UP*
- *ecam.be UP*
- *pountokdo.com DOWN*
- *google.be UP*
- *helha.be UP*

here is the output ;)
