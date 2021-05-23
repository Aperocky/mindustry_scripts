import subprocess

raw_code = """
getlink target 0
ubind @{unit}
sensor flag @unit @flag
jump 1 lessThan flag {beginFlag}
jump 1 greaterThanEq flag {endFlag}
sensor carry @unit @{itemType}
jump 11 greaterThanEq carry {capacity}
ulocate ore core true @{itemType} outx outy found building
ucontrol approach outx outy 5 0 0
ucontrol mine outx outy 0 0 0
end
sensor x target @x
sensor y target @y
ucontrol approach x y 5 0 0
ucontrol itemDrop target 999 0 0 0
"""

UNITS = {
    "mega": 60,
    "mono": 20,
    "poly": 30,
    "pulsar": 40,
    "nova": 30,
    "quasar": 40,
}

RESOURCES = [
    "copper",
    "lead",
    "coal",
    "scrap",
    "titanium"
]

def mine(unit, beginFlag, endFlag, itemType):
    """
    mindu mine $unit $beginFlag $endFlag $itemType
    """
    if not unit in UNITS:
        raise ValueError("UNIT TYPE CANNOT MINE")
    if not itemType in RESOURCES:
        raise ValueError("RESOURCE TYPE NOT FOUND")
    capacity = UNITS[unit]
    code = raw_code.format(unit=unit, beginFlag=beginFlag, endFlag=endFlag, itemType=itemType, capacity=capacity)
    subprocess.run("pbcopy", universal_newlines=True, input=code)
