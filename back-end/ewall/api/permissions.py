from rest_framework.permissions import BasePermission,SAFE_METHODS

# set permission for author of post ( if currently user is author of post , this user access to send request with post method)
# and if currently user is not author of post , this users can not access to post method and it can access to SAFE_METHODS
class IsAuthorOrReadOnly(BasePermission):
    # for set permission
    def has_object_permission(self,request,view,obj):
        # if currently user is not author , access to SAFE_METHODS
        if request.method == SAFE_METHODS:
            return True
        
        return bool(
            # if currently user is authenticated and is super user , or is author of this post, its can to access to post method
            request.user.is_authenticated and request.user.is_superuser or
            request.user == obj.author
        )