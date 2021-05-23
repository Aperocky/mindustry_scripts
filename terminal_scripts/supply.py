import subprocess

raw_code = """
getlink target 0
ubind @{unit}
sensor flag @unit @flag
jump 1 lessThan flag {beginFlag}
jump 1 greaterThanEq flag {endFlag}
sensor storage target @{itemType}
sensor carry @unit @{itemType}
jump 1 greaterThan storage {storage}
jump 14 equal carry 0
sensor vx target @x
sensor vy target @y
ucontrol move vx vy 0 0 0
ucontrol itemDrop target 99 0 0 0
end
ulocate building core false @copper outx outy found core
ucontrol move outx outy 0 0 0
ucontrol itemDrop core 99 0 0 0
ucontrol itemTake core @{itemType} {capacity} 0 0
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

def create_supply(unit, beginFlag, endFlag, itemType, storage=800):
    """
    mindu supply $unit $beginFlag $endFlag $itemType [$storage]
    """
    if not unit in UNITS:
        raise ValueError("UNIT TYPE NOT FOUND")
    if not itemType in RESOURCES:
        raise ValueError("RESOURCE TYPE NOT FOUND")
    capacity = UNITS[unit]
    code = raw_code.format(unit=unit, beginFlag=beginFlag, endFlag=endFlag, itemType=itemType, storage=storage, capacity=capacity)
    subprocess.run("pbcopy", universal_newlines=True, input=code)
