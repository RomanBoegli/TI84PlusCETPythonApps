# TI 84 Plus CE-T Python Apps
Small (Circuit)Python programs that run on a [TI-84 Plus CE-T Python Edition](https://education.ti.com/en/products/calculators/graphing-calculators/ti-84-plus-ce-python) calculator. 
As storage is limited on these calculators, the programs might not be beautifully formatted.
 
## What is ``CircuitPython``?
Excerpt from [manual](https://education.ti.com/en/software/details/en/4C66F7E62A1846079881D7C0E372F874/Python-App): 
> _"TI-Python is based on CircuitPython, a variant of Python designed to fit in small microcontrollers. The original CircuitPython implementation has been adapted for use by TI."_

## What can it do?

App | Description | Functions
--|--|--
**``BASES``** | Simple conversion</br>functions | ``db``: decimal to binary conversion </br> ``bd``: binary to decimal conversion
**``EULPHI``** | Euler's totient</br>function to find</br>number of co-primes  | ``phi``: Euler's totient function $\varphi (n)$ or $\phi(n)$ </br> **``gcd``**: Euclidean algorithm</br> ``mod``: modulo calculations
**``MODARIT``** | Modular arithmetic | ``egcd``: extended Euclidean algorithm </br> ``mod``: modulo calculations (remainder) </br> ``modinv``: modulo inverse calculations </br> ``mmodinv``: modulo inverse matrix calculations
**``PMODARIT``** | Binary polynomial </br> arithmetic | ``p_mod``: Binary polynomial modulus</br> ``p_divmod``: Binary polynomial division</br> ``p_mul``: Binary polynomial multiplication</br> ``p_exp``: Binary polynomial exponentiation by squaring</br> ``p_gcd``: Binary polynomial Euclidean algorithm</br> ``p_egcd``: Binary polynomial extended Euclidean algorithm</br> ``p_mul_mod``: Binary polynomial modular multiplicative</br> ``p_mul_inv``: Binary polynomial modular multiplicative inverse

## How can I use it?

0. Make sure you have [TI Connect](https://education.ti.com/en/products/computer-software/ti-connect-sw) installed on your computer.
1. Download this repo.
2. Connect your calculator with your computer.
3. Use TI Connect to upload the app files you need (e.g. ``MODARIT.py``) to your calculator. The ``[NAME]_Test.py`` files serve only testing purposes during development and are not meant to use on your calculator.
4. The app should now be listed in your calculator's app inventory, ready to interact with.

