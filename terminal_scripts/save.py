import subprocess

raw_code = """
getlink target 0
ubind @{unit}
sensor health @unit @health
sensor maxHealth @unit @maxHealth
op div vitality health maxHealth
jump 7 lessThan vitality 0.6
end
sensor x_loc target @x
sensor y_loc target @y
ucontrol move x_loc y_loc 0 0 0
"""

def save(unit_type):
    code = raw_code.format(unit=unit_type)
    subprocess.run("pbcopy", universal_newlines=True, input=code)
