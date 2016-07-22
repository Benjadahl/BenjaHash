# BenjaHash
*[Github Repository Link](https://github.com/Benjadahl/BenjaHash)*
###About
BenjaHash is an open source hashing algorithm made in python3.

The way it works is by using the modulus operation in python to create an irreversible calculation. 

This way the program will effectively hash the binary input, and return a 1 byte intenger as a result. 
*(The target size for the hash will be user specific in a later version)*

> TODO: a more detailed explanation of the hashing process

###Demo
The repository includes a demo of the software, to use this demo simply download the current release of the repository or clone it using git.

    git clone https://github.com/Benjadahl/BenjaHash.git

Or you can check out the [releases](https://github.com/Benjadahl/BenjaHash/releases)

To experience the demo enter the demo folder using your favorite terminal and type

    python3 demo.py int 123456789

You can then change the number to whatever you want, *the hashing functions better with larger numbers.*

You can also change the **int** value to **str** or **bin**, for string or binary input.

###Usage/Implementation
To intergrate the hashing algorithm into your python applications you need to import the file **BenjaHash.py** into your python script, and then call the *hash()* function.

```python
#Import the hashing algorihtm
import BenjaHash.py

#Call the hashing function
hashedData = BenjaHash.hash(input)
print(hashedData)
```

###Docs
The documentation for the software can be found in the [Github Wiki](https://github.com/Benjadahl/BenjaHash/wiki)
It will also be present in the docs folder, located in top level of the repository.

###License
This software is released under the GNU GPL v3 license, more details in the LICENSE.md file.

*-Benjadahl 2016*
