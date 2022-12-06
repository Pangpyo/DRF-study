from rest_framework import permissions


# 안전한 메소드 종류. 이 METHOD만으로는 단순조회만 될 뿐, 데이터 파괴(추가/수정/삭제) 불가
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAuthorOrReadOnly(permissions.BasePermission):
   # 인증된 유저에 한해, 목록조회/포스팅등록 허용
   def has_permission(self, request, view):
       return request.user.is_authenticated

   # 작성자에 한해 레코드에 대한 수정/삭제 허용
   def has_object_permission(self, request, view, obj):
       # 조회 요청(GET, HEAD, OPTIONS) 에 대해 인증여부 상관없이 허용
       if request.method in permissions.SAFE_METHODS:
          return True
       # PUT, DELETE 요청에 대해 작성자일 경우 요청 허용
       return obj.author == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모든 요청에 ​​허용되며,
        # 그래서 GET, HEAD, OPTIONS 요청을 허용 할 것입니다.
        if request.method in permissions.SAFE_METHODS:
            return True

        # 인스턴스에는`owner`라는 속성이 있어야합니다.
        return obj.author == request.user

# 비인증 요청에게는, 읽기 권한만 허용
class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # 안전한 METHOD요청이면, 인증여부에 상관없이, 뷰 호출 허용
        if request.method in SAFE_METHODS:
            return True
        # 안전하지 않은 METHOD일 경우, 인증유저에게만, 뷰 호출 허용
        elif request.user and request.user.is_authenticated:
            return True
        # 안전하지 않은 METHOD일 경우, 비인증유저에게는, 뷰 호출 제한
        return False