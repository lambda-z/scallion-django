from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ScallionPagination(PageNumberPagination):
    page_size_query_param = 'size'
    page_query_param = 'current'
    max_page_size = 100
    # 设置默认的页大小为10
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            # 获取动态的page_size
            'size': self.page_size,
            'current': self.page.number,
            'pages': self.page.paginator.num_pages,
            'total': self.page.paginator.count,
            'records': data
        })


    def get_page_size(self, request):
        # 获取用户传入的 page_size
        page_size = request.query_params.get(self.page_size_query_param)
        if page_size:
            try:
                page_size = int(page_size)
                # 不能超过最大限制
                if page_size > self.max_page_size:
                    page_size = self.max_page_size
                elif page_size < 1:
                    page_size = self.page_size  # 小于1也用默认
            except (ValueError, TypeError):
                page_size = self.page_size  # 非法值则用默认
        else:
            page_size = self.page_size  # 未传值时用默认
        self.page_size = page_size
        return page_size
