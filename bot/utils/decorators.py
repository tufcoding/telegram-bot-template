from database.database import Session, User
from logger.logger import logger

from pyrogram.types import Message, CallbackQuery
from typing import Callable, Union
from functools import wraps

def get_user():
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(client, update: Union[Message, CallbackQuery], *args, **kwargs):
            session = Session()
            try:
                user_id = update.from_user.id
                user = session.query(User).filter_by(user_id=user_id).first()
                if not user:
                    user = User(
                        user_id=user_id,
                        username=update.from_user.username,
                        first_name=update.from_user.first_name,
                        last_name=update.from_user.last_name
                    )
                    session.add(user)
                    session.commit()
                
                return await func(client, update, user, session, *args, **kwargs)
            except Exception as e:
                session.rollback()
                logger.error(f"Error in decorator: {e}")
                raise
            finally:
                session.close()
        return wrapper
    return decorator
