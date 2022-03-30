from enum import Enum


class Position(Enum):
    CEO = 'Chief Execution Officer'
    HEAD_OF_DEPARTMENT = 'Head of Department'
    TEAM_LEADER = 'Team Leader'
    DEVELOPER = 'Engineer'


class Growth(Enum):
    HIRED = 'Hired'
    FIRED = 'Fired'
    PROMOTED = 'Promoted'
    MOVED = 'Moved to another department'
