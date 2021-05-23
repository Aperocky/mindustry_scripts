import subprocess

from_code = """
getlink target 0
ubind @{unit}
sensor flag @unit @flag
jump 1 lessThan flag {beginFlag}
jump 1 greaterThanEq flag {endFlag}
sensor carry @unit @{itemType}
sensor storage target @{itemType}
jump 1 greaterThan carry 0
jump 1 lessThan storage 100
sensor x_loc target @x
sensor y_loc target @y
ucontrol move x_loc y_loc 0 0 0
ucontrol itemTake target @{itemType} {capacity} 0 0
"""

to_code = """
getlink target 0
ubind @{unit}
sensor flag @unit @flag
jump 1 lessThan flag {beginFlag}
jump 1 greaterThanEq flag {endFlag}
sensor carry @unit @{itemType}
sensor storage target @{itemType}
jump 1 equal carry 0
jump 1 greaterThan storage {storage}
sensor x_loc target @x
sensor y_loc target @y
ucontrol move x_loc y_loc 0 0 0
ucontrol itemDrop target 999 60 0 0
"""

UNITS = {
    "flare": 20,
    "horizon": 30,
    "zenith": 80,
    "mega": 60,
    "mono": 20,
    "poly": 30,
}

RESOURCES = [
    "silicon",
    "thorium",
    "blast-compound",
    "surge-alloy",
    "metaglass",
    "graphite",
    "titanium",
    "copper",
    "lead",
    "phase-fabric",
    "coal",
    "sand",
    "pyratite",
    "plastanium",
    "spore-pod"
]

def move(direction, unit, beginFlag, endFlag, itemType, storage=900):
    """
    mindu move (from|to) $unit $beginFlag $endFlag $itemType [storage]
    """
    if not direction in ["from", "to"]:
        raise ValueError("Direction argument must be from or to")
    capacity = UNITS[unit]
    if direction == "from":
        code = from_code.format(unit=unit, beginFlag=beginFlag, endFlag=endFlag, itemType=itemType, capacity=capacity)
    else:
        code = to_code.format(unit=unit, beginFlag=beginFlag, endFlag=endFlag, itemType=itemType, storage=storage)
    subprocess.run("pbcopy", universal_newlines=True, input=code)

