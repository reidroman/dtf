import brownie
import os

os.system('git clone --depth 0 https://github.com/curvefi/curve-contract.git')

# load up brownie console (be in curve-contract repo)
from brownie import *
p = project.load('.', name="CurveContractProject") # dir is curve-contract root
p.load_config()
from brownie.project.CurveContractProject import *
network.connect('development')
run('deploy')

project.get_loaded_projects()[1].close()
chain.reset()

# b /Users/reidroman/.asdf/installs/python/3.10.0/lib/python3.10/site-packages/brownie/project/scripts.py:69
# b /Users/reidroman/.asdf/installs/python/3.10.0/lib/python3.10/site-packages/brownie/project/scripts.py:70
# b /Users/reidroman/.asdf/installs/python/3.10.0/lib/python3.10/site-packages/brownie/network/contract.py:586
# b /Users/reidroman/.asdf/installs/python/3.10.0/lib/python3.10/site-packages/brownie/network/account.py:457
# b /Users/reidroman/.asdf/installs/python/3.10.0/lib/python3.10/site-packages/web3/providers/rpc.py:85

print(brownie.__file__)
# /Users/reidroman/.asdf/installs/python/3.10.0/lib/python3.10/site-packages/brownie/_cli/run.py

# TODO: fiddle with curve-contract/contracts/pools/3pool/pooldata.json
# contract deploy seems to be failing on construction of curve-contract/contracts/tokens/CurveTokenV2.vy
# TODO: check what the real deployment did for its pool coin?


# TODO: setup git/jupyter hooks for jupytext (deflate notebook for storage and version control)
# also look at nbconvert and nbdime