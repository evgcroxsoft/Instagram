#________________________________________________________ENUM MODEL__________________________________________________________________________________

from enum import Enum


class AccessType(Enum):
    LIMITED = 'limited'
    FULL = 'full'


class StatusType(Enum):
    VISIBLE = 'visible'
    UNVISIBLE = 'unvisible'
    ARCHIVED = 'archived'
