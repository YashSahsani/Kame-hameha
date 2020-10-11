# Kame-hameha
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
> Python based network worm that spreads on the local network and encrypts everything with symmetric algorithm AES and than encrypts decryption key with assymmetric alogrithm RSA.
So, basically its a mixture of worm and ransomware.

# Disclaimer

# Methods used:
- For infecting windows machine on a network we use psexec.
- For infecting linux machine on a network we use ssh bruteforce.


# Technologies used
* python  
* psexec
* ssh
* bash
* cryptography


# How to use
- Run it on linux
First install all requirements\
```bash
$ pip install -r requirements.txt
$ cd propagation 
$ bash run.sh
```


## Contributing

1. Fork it (<https://github.com/YashSahsani/Kame-hameha/fork>)
2. Create your feature branch (`git checkout -b feature/new-feature-name`)
3. Commit your changes (`git commit -am 'commit message'`)
4. Push to the branch (`git push origin feature/new-feature-name`)
5. Create a new Pull Request
