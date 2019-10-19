Installation.

Download python on python.org and install. Recomendate version 3.7.5
When installing, select "for all users" and "register path"
Copy the metahash.py library to the lib folder where python got up.
For ease of use, it is also recommended to install Far manager.
The folder with scripts can be put in any arbitrary place.

Running scripts.

Start by checking your balance. In Far manager, open balance.py on F4.
Enter your address there. Or any balance that you want to find out.
To start in Far, just press Enter on the balance.py file.

When you first start, you will receive an error that the modules are not installed.
They must be installed by typing the command:
pip install cryptography
pip install requests
You can also update pip (a message will be written in yellow).

For other operations, you will also need in the script in the upper block
fix the address and also put your private key. Keyless delegation and
sending will not work and the script will display an error message.

balance.py - checks balance.
delegate.py - delegates funds to a node (if not specified how much then delegates everything).
ecpriv_to_der.py - convert *.ec.priv to DER key (for nodes)
example.py - examples of using various library functions. Default - generate new address.
reinvest.py - removes the last transaction from the delegation and delegates all funds to the node.
sending.py - sending MHC to the selected address.
undelegate.py - removes the last trans from the delegation.
undelegate_self.py - if you delegated to yourself (an error in Metagate) then removes this trans.
