import numpy as np
import decimal
import hashlib
from Crypto.Cipher import AES

print(0.1 + 1.1 == 1.2)

print(np.double(0.1) + np.double(1.1) == np.double(1.2))  # type: ignore

print(decimal.Decimal("0.1") + decimal.Decimal("1.1") == decimal.Decimal("1.2"))

# get python version
import sys

print(
    str.format(
        "Python {}.{}.{}",
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro,
    )
)
