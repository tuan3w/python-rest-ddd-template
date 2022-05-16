from multiprocessing import AuthenticationError
from app.core.exceptions import UserNotFound
from app.core.usecase import AppUsecase
from app.modules.auth.exceptions import InvalidPassword, UserExistedError
from app.modules.auth.model import User
from ..utils import check_password


class LoginUsecase(AppUsecase):
    def login(self, username: str, passwd: str) -> User:
        user = self.repo.user.get_user_by_username(username)
        if not user:
            raise UserNotFound()
        if not check_password(passwd, user.password):
            raise InvalidPassword()
        return user
