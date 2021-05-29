import subprocess

raw_code = """
getlink guard 0
ubind @{unit}
uradar enemy any any distance 0 1 target
jump 10 notEqual target null
sensor stay_x guard @x
sensor stay_y guard @y
ucontrol boost 1 0 0 0 0
ucontrol approach stay_x stay_y {circle_size} 0 0
ucontrol targetp target 0 0 0 0
end
sensor tar_x target @x
sensor tar_y target @y
ucontrol approach tar_x tar_y {unit_range} 0 0
ucontrol boost 0 0 0 0 0
ucontrol targetp target 1 0 0 0
"""

UNIT_TYPES = {
    "flare": 17,
    "zenith": 23,
    "antumbra": 28,
    "poly": 28,
    "mega": 23,
    "nova": 21,
    "pulsar": 8,
    "quasar": 20,
    "vela": 23,
}

def defend(unit_type, circle_size=5):
    if not unit_type in UNIT_TYPES:
        raise "Cannot defend with this unit, use something else for land units that can't boost"
    unit_range = UNIT_TYPES[unit_type]
    code = raw_code.format(unit=unit_type, unit_range=unit_range, circle_size=circle_size)
    subprocess.run("pbcopy", universal_newlines=True, input=code)
