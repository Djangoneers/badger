from tortoise import fields

from .common import CommonFields


class Member(CommonFields):
    discord_id = fields.CharField(max_length=18)
