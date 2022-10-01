#________________________________________________________ENUM MODEL__________________________________________________________________________________

from enum import Enum

#for account
class AccountStatus(Enum):
    LIMITED = 'limited'
    FULL = 'full'


class PostStatus(Enum):
    VISIBLE = 'visible'
    INVISIBLE = 'invisible'
    ARCHIVED = 'archived'


class SubcribeStatus(Enum):
    NEW = 'new'
    OK = 'ok'
    DECLINED = 'declined'


class LikeStatus(Enum):
    LIKE = 'like'
    DISLIKE = 'dislike'

