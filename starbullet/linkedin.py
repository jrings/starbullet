"""Query your LinkedIn profile through the APIon3
Sadly, the Python library is Python 2 only...
TODO: Recode to work in Pyth
"""

import os

from linkedin import linkedin


def _authenticate(fname=os.expanduser("~/.linkedin")):
    """
    Get authentication for the LinkedIn API
    Parameters
    ----------
    fname: Filename containing two lines - the API user and secret key. It's assumed to be in ~/.linkedin

    Returns
    -------
    LinkedIn authentication object
    """
    with open(fname) as _in:
        u = _in.readline().strip()
        k = _in.readline().strip()
    authentication = linkedin.LinkedInAuthentication(u, k, "localhost:8000")
    return authentication


def get_app():
    """
    Get the LinkedIn API application
    Returns
    -------
    LinkedIn API application
    """

    auth = _authenticate()
    return linkedin.LinkedInApplication(auth)


if __name__ == "__main__":
    print(get_app().get_profile())

