# from flask import current_app
# from webapp.db import db
# from webapp.logging.model import ActionType, ObjectType, Planer_History

# def log_action(
#     user_id: int,
#     action: ActionType,
#     object_type: ObjectType,
#     object_id: int = None,
#     details: str = None
# ) -> None:
#     """Логирует действия пользователя в БД"""
#     try:
#         log_entry = Planer_History(
#             user_id=user_id,
#             action=action,
#             object_type=object_type,
#             object_id=object_id,
#             details=details
#         )
#         db.session.add(log_entry)
#     except Exception as e:
#         current_app.logger.error(f"Ошибка логирования: {str(e)}")
#         raise