from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    def has_permissions(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )

        if not model_permission_codename:
            return False
        return request.user.has_perm(model_permission_codename)

    # Retorna o nome do app, da ação e do model para compor a permissão do usuário
    def __get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model.__meta.model_name
            app_label = view.queryset.model.__meta.app_label
            action = self.__get_action_sufix(method)
            return f"{app_label}.{action}_{model_name}"
        except AttributeError:
            return None

    # Retorna a ação do metodo recebida da requisição.
    def __get_action_sufix(self, method):
        method_action = {
            "GET": "view",
            "OPTIONS": "view",
            "HEAD": "view",
            "POST": "add",
            "PUT": "change",
            "PUTCH": "change",
            "DELETE": "delete",
        }
        return method_action.get(method, "")
