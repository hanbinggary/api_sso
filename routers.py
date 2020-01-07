from views.users_view import UsersView, UserView, LogoutView
from views.roles_view import RolesView, RoleView
from views.menus_view import MenusView, MenuView
from views.components_view import ComponentsView, ComponentView
from views.functions_view import FunctionsView, FunctionView
from views.auth_view import AuthView

routers = [
    (UsersView.as_view(), '/users'),
    (UserView.as_view(), '/user/<uid:int>'),
    (LogoutView.as_view(), '/logout'),
    (RolesView.as_view(), '/roles'),
    (RoleView.as_view(), '/role/<rid:int>'),
    (MenusView.as_view(), '/menus'),
    (MenuView.as_view(), '/menu/<mid:int>'),
    (ComponentsView.as_view(), '/components'),
    (ComponentView.as_view(), '/component/<cid:int>'),
    (FunctionsView.as_view(), '/functions'),
    (FunctionView.as_view(), '/function/<fid:int>'),
    (AuthView.as_view(), '/auth'),
]
