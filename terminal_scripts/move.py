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
sensor capacity @unit @itemCapacity
ucontrol move x_loc y_loc 0 0 0
ucontrol itemTake target @{itemType} capacity 0 0
"""

to_code = """
getlink target 0
ubind @{unit}
sensor flag @unit @flag
jump 1 lessThan flag {beginFlag}
jump 1 greaterThanEq flag {endFlag}
sensor carry @unit @{itemType}
sensor storage target @{itemType}
sensor targetcap target @itemCapacity
op sub sgoal targetcap 100
jump 1 equal carry 0
jump 1 greaterThan storage sgoal
sensor x_loc target @x
sensor y_loc target @y
ucontrol move x_loc y_loc 0 0 0
ucontrol itemDrop target 999 0 0 0
"""

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

def move(direction, unit, beginFlag, endFlag, itemType):
    """
    mindu move (from|to) $unit $beginFlag $endFlag $itemType [storage]
    """
    if itemType not in RESOURCES:
        raise ValueError("Resource type does not exist")
    if not direction in ["from", "to"]:
        raise ValueError("Direction argument must be from or to")
    if direction == "from":
        code = from_code.format(unit=unit, beginFlag=beginFlag, endFlag=endFlag, itemType=itemType)
    else:
        code = to_code.format(unit=unit, beginFlag=beginFlag, endFlag=endFlag, itemType=itemType)
    subprocess.run("pbcopy", universal_newlines=True, input=code)

